#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine

zone_dtype_map = {
    "LocationID": "Int64",
    "Borough": "string",
    "Zone": "string",
    "service_zone": "string"
}

dtype_map = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]



def create_header(df, table_name, engine):
    df.head(0).to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"Table '{table_name}' initialized.")


def insert_rows(df, table_name, engine, total_rows):
    rows = len(df)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    total_rows += rows
    print(
        f"Table '{table_name}': "
        f"inserted {rows:,} rows "
        f"(total {total_rows:,})"
    )

    return total_rows


def parquet_to_db(file_path, pg_table, engine, batch_size):
    parquet_file = pq.ParquetFile(file_path)
    first = True
    total_rows = 0
    chunk_no = 1

    print(f"\nStarting Parquet ingestion: {file_path}")

    for batch in parquet_file.iter_batches(batch_size=batch_size):
        df_chunk = batch.to_pandas()

        if first:
            create_header(df_chunk, pg_table, engine)
            first = False

        total_rows = insert_rows(
            df_chunk, pg_table, engine, total_rows
        )

        print(f"Parquet chunk {chunk_no} completed.")
        chunk_no += 1

    print(
        f"Completed Parquet ingestion for '{pg_table}'. "
        f"Total rows inserted: {total_rows:,}\n"
    )


def csv_to_db(df_iter, pg_table, engine):
    first = True
    total_rows = 0
    chunk_no = 1

    print(f"\nStarting CSV ingestion into '{pg_table}'")

    for df_chunk in df_iter:
        if first:
            create_header(df_chunk, pg_table, engine)
            first = False

        total_rows = insert_rows(
            df_chunk, pg_table, engine, total_rows
        )

        print(f"CSV chunk {chunk_no} completed.")
        chunk_no += 1

    print(
        f"Completed CSV ingestion for '{pg_table}'. "
        f"Total rows inserted: {total_rows:,}\n"
    )


@click.command()
@click.option('--pg_user', default='postgres', show_default=True)
@click.option('--pg_pass', default='postgres', show_default=True)
@click.option('--pg_host', default='host.docker.internal', show_default=True)
@click.option('--pg_port', default='5433', show_default=True)
@click.option('--pg_db', default='ny_taxi', show_default=True)
@click.option('--chunksize', default=100_000, type=int, show_default=True)
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, chunksize):

    engine = create_engine(
        f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}',
        pool_pre_ping=True
    )

    try:
        parquet_to_db(
            file_path='./data/green_tripdata_2025-11.parquet',
            pg_table='green_taxi_trips',
            engine=engine,
            batch_size=chunksize,
            dtype=dtype_map,
            parse_dates=parse_dates
        )

        df_iter = pd.read_csv(
            './data/taxi_zone_lookup.csv',
            dtype=zone_dtype_map,
            iterator=True,
            chunksize=chunksize
        )

        csv_to_db(
            df_iter=df_iter,
            pg_table='taxi_zone_lookup',
            engine=engine
        )

        print(f"All data successfully ingested into '{pg_db}'.")

    except Exception as e:
        print(f"Ingestion failed: {e}")


if __name__ == '__main__':
    run()
