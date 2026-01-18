# Initial Dataset Slice

## Data Source
NYC Taxi & Limousine Commission (TLC) Trip Record Data — Yellow Taxi trips.

## Time Range
January 2019 to March 2019.

## Geographic Scope
All NYC TLC taxi zones.

## Target Variable
Ride demand, defined as the number of completed rides per zone per hour.

## Rationale

While a full year of data is computationally feasible, the project intentionally starts with a three-month slice to enable rapid iteration and pipeline validation. This approach allows assumptions, preprocessing logic, and modeling pipelines to be validated before expanding the scope of the analysis.

This project uses pre-pandemic NYC taxi data to model stable urban mobility patterns. The focus is on methodological rigor and interpretability rather than real-time deployment, avoiding distortions caused by extraordinary external events such as the COVID-19 pandemic. The analysis will later be extended to longer time horizons to capture seasonal and holiday effects.
