
-- create external table
CREATE OR REPLACE EXTERNAL TABLE taxidata2024.taxidata_2024_01_06
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://taxi-data-2024/*.parquet']
);

--  create a materialized table
CREATE TABLE taxidata2024.taxidata_2024_01_06_materialised AS
SELECT * FROM `de-sandbox-448915.taxidata2024.taxidata_2024_01_06`;


-- Check yellow trip data
select count(*)
from taxidata2024.taxidata_2024_01_06_materialised;


--- External table
-- 0 MB
select count(distinct PULocationID) 
from taxidata2024.taxidata_2024_01_06

--- Materialised table
-- 155.12 MB
select count(distinct PULocationID) 
from taxidata2024.taxidata_2024_01_06_materialised 


select PULocationID 
from taxidata2024.taxidata_2024_01_06_materialised

-- 310.24 MB
select PULocationID, DOLocationID
from taxidata2024.taxidata_2024_01_06_materialised

-- 8,333
select count(*)
from taxidata2024.taxidata_2024_01_06_materialised
where fare_amount = 0

-- Partition by tpep_dropoff_datetime and Cluster on VendorID
CREATE TABLE taxidata2024.taxidata_2024_01_06_optimised
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM taxidata2024.taxidata_2024_01_06;

-- 310.24 MB for non-partitioned table
SELECT DISTINCT VendorID
FROM `taxidata2024.taxidata_2024_01_06_materialised`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

-- 26.84 MB for the partitioned table
SELECT DISTINCT VendorID
FROM `taxidata2024.taxidata_2024_01_06_optimised`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';


-- 0 MB
SELECT COUNT(*)
FROM `taxidata2024.taxidata_2024_01_06_materialised`;

