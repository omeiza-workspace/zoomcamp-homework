## [DRAFT] Module 4 Homework

## Question 1:

If you run `dbt run --select int_trips_unioned`, what models will be built?

- `stg_green_tripdata`, `stg_yellow_tripdata`, and `int_trips_unioned` (upstream dependencies)
- Any model with upstream and downstream dependencies to `int_trips_unioned`
- `int_trips_unioned` only
- `int_trips_unioned`, `int_trips`, and `fct_trips` (downstream dependencies)

### Answer:
```txt
int_trips_unioned only

-- The --select flag only builds the selected model without its dependencies
-- Use --select +model to include upstream dependencies
-- Use --select model+ to include downstream dependencies
```

---

## Question 2:

What happens when you run `dbt test --select fct_trips`?

- dbt will skip the test because the model didn't change
- dbt will fail the test, returning a non-zero exit code
- dbt will pass the test with a warning about the new value
- dbt will update the configuration to include the new value

### Answer:
```txt
dbt will fail the test, returning a non-zero exit code

-- Generic tests run on the model table itself, not the source
-- New values not in accepted_values will cause the test to fail
```

---

## Question 3:

What is the count of records in the `fct_monthly_zone_revenue` model?

- 12,998
- 14,120
- 12,184
- 15,421

### Answer:
```sql
-- 12,184
SELECT COUNT(*) FROM prod.fct_monthly_zone_revenue;
```

---

## Question 4:

Which zone had the highest revenue for Green taxis in 2020?

- East Harlem North
- Morningside Heights
- East Harlem South
- Washington Heights South

### Answer:
```sql
-- East Harlem North
SELECT pickup_zone, 
       SUM(revenue_monthly_total_amount) AS total_amount
FROM prod.fct_monthly_zone_revenue
WHERE service_type = 'Green' 
  AND YEAR(revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY total_amount DESC;
```

---

## Question 5:

What is the **total number of trips** (`total_monthly_trips`) for Green taxis in October 2019?

- 500,234
- 350,891
- 384,624
- 421,509

### Answer:
```sql
-- 384,624
SELECT SUM(total_monthly_trips) AS total_trips
FROM prod.fct_monthly_zone_revenue
WHERE service_type = 'Green' 
  AND revenue_month = '2019-10-01';
```

---

## Question 6:

What is the count of records in `stg_fhv_tripdata`?

- 42,084,899
- 43,244,693
- 22,998,722
- 44,112,187

### Answer:
```sql
-- 43,244,693
SELECT COUNT(*) 
FROM prod.stg_fhv_tripdata;
-- Or from raw table: SELECT COUNT(*) FROM prod.fhv_tripdata WHERE dispatching_base_num IS NOT NULL;
```

---

## Submitting the solutions

Form for submitting: https://courses.datatalks.club/de-zoomcamp-2026/homework/hw4
