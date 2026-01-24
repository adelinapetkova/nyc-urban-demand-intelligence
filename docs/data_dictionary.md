# Data Dictionary

## 1. Overview

This project uses publicly available **NYC Taxi & Limousine Commission (TLC)** trip data as a proxy for ride-hailing demand.

Each row in the dataset represents a **single completed trip**.

The dataset is used to:
- Analyze historical ride demand patterns
- Build predictive models for zone-level hourly demand
- Perform statistical inference and clustering
- Simulate business decisions for ride-hailing operations

---

## 2. Dataset Scope

**Initial slice**  
- Time range: January-March 2019 
- Geography: New York City  
- Granularity: Individual ride records  

**Aggregated modeling grain**  
- Zone × Hour  
- Demand = number of completed rides per zone per hour  

---

## 3. Raw Fields

| Column Name              | Type      | Description                                                                 |
|--------------------------|-----------|-----------------------------------------------------------------------------|
| `vendorid`               | Integer   | Code identifying the TLC-licensed provider                                  |
| `tpep_pickup_datetime`  | Datetime  | Date and time when the trip started                                         |
| `tpep_dropoff_datetime` | Datetime  | Date and time when the trip ended                                          |
| `passenger_count`       | Integer   | Number of passengers in the vehicle                                         |
| `trip_distance`         | Float     | Trip distance in miles                                                  |
| `pickup_longitude`      | Float     | Longitude of pickup location                                        |
| `pickup_latitude`       | Float     | Latitude of pickup location                                |
| `dropoff_longitude`     | Float     | Longitude of dropoff location                                     |
| `dropoff_latitude`      | Float     | Latitude of dropoff location                                 |
| `pulocationid`          | Integer   | TLC taxi zone ID for pickup location                                    |
| `dolocationid`          | Integer   | TLC taxi zone ID for dropoff location                                     |
| `ratecodeid`            | Integer   | Final rate code applied                                |
| `store_and_fwd_flag`    | String    | Indicates whether trip record was stored before sending to server           |
| `payment_type`          | Integer   | Payment method code                                                          |
| `fare_amount`           | Float     | Fare amount in USD                                                           |
| `extra`                 | Float     | Extra charges (e.g., night surcharge)                                    |
| `mta_tax`               | Float     | MTA tax                                                           |
| `tip_amount`            | Float     | Tip amount                                                               |
| `tolls_amount`          | Float     | Toll charges                                                        |
| `improvement_surcharge` | Float     | TLC improvement surcharge                                                    |
| `total_amount`          | Float     | Total charged amount                                                         |
| `congestion_surcharge`  | Float     | Congestion charge                                            |

---

## 4. Key Derived Features

| Feature Name          | Type     | Description                                                              |
|-----------------------|----------|--------------------------------------------------------------------------|
| `pickup_hour`        | Integer  | Hour of day extracted from pickup timestamp (0–23)                      |
| `pickup_day`         | Integer  | Day of month                                                             |
| `pickup_weekday`     | Integer  | Day of week (0=Monday, 6=Sunday)                                         |
| `pickup_month`       | Integer  | Month number                                                             |
| `pickup_year`        | Integer  | Year                                                                      |
| `trip_duration_min`  | Float    | Trip duration in minutes (dropoff − pickup)                             |
| `is_weekend`         | Boolean  | True if pickup day is Saturday or Sunday                                 |
| `zone_pair`          | String   | Pickup zone - dropoff zone combination                                   |

---

## 5. Aggregated Modeling Tables

### 5.1 Hourly Zone Demand Table

| Column Name    | Type     | Description                                                  |
|----------------|----------|--------------------------------------------------------------|
| `zone_id`      | Integer  | TLC taxi zone ID                                             |
| `hour`         | Integer  | Hour of day (0–23)                                           |
| `date`         | Date     | Calendar date                                                |
| `ride_demand`  | Integer  | Number of completed rides in that zone and hour              |

---

### 5.2 Demand + Feature Table

| Column Name           | Type     | Description                                                 |
|-----------------------|----------|-------------------------------------------------------------|
| `zone_id`             | Integer  | TLC taxi zone ID                                            |
| `datetime_hour`      | Datetime | Start of the hour bucket                                    |
| `ride_demand`        | Integer  | Number of completed rides                                   |
| `avg_trip_distance`  | Float    | Average trip distance in the hour                           |
| `avg_fare`           | Float    | Average fare in the hour                                    |
| `is_weekend`         | Boolean  | Weekend indicator                                           |
| `hour`               | Integer  | Hour of day                                                 |
| `weekday`            | Integer  | Day of week                                                 |
| `month`              | Integer  | Month                                                       |

---

## 6. Target Variables

| Target Name    | Type     | Description                                                  |
|----------------|----------|--------------------------------------------------------------|
| `ride_demand`  | Integer  | Number of completed rides (Zone × Hour)                      |
| `wait_time`*   | Float    | Proxy metric for service delay                               |
| `churn`*       | Binary   | Proxy rider disengagement indicator                          |

Wait time and churn will be proxied using derived and aggregate metrics.

---

## 7. Data Quality Considerations

| Issue                       | Description                                                      |
|-----------------------------|------------------------------------------------------------------|
| Missing timestamps          | Trips with missing pickup/dropoff times must be dropped         |
| Zero or negative distances  | Must be filtered out                                             |
| Unrealistic trip durations  | Outliers (e.g., > 3 hours) should be removed                     |
| Missing zone IDs            | Records without valid pickup zones should be excluded from zone modeling  |
| Duplicate rows              | Must be deduplicated                                             |

---

## 8. Known Limitations

- Dataset contains **only completed rides**, not failed or canceled requests  
- True wait time is not available  
- Rider-level identity is not available (limits churn modeling)  
- Taxi data is a **proxy** for ride-hailing services (Uber/Lyft)  
- External factors (weather, events) not included initially  

---
