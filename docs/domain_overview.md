# Ride-Hailing Domain Overview

### What is ride-hailing demand in practice?
Ride-hailing demand represents the number of people who need a ride at different times of day and in different parts of the city.

### Why does it vary by time and location?
- **Time:** Demand fluctuates according to daily routines, such as commuting in the morning, returning home in the evening, and low activity during the night.  
- **Location:** Demand depends on population density, the presence of key facilities (schools, hospitals, malls, stadiums), and special events in the area.

### Why do companies care about predicting it ahead of time?
Accurate demand predictions enable companies to **plan driver distribution proactively**, maximizing operational efficiency and ensuring high customer satisfaction.

### Defining Demand for This Project
- **One-sentence definition:** In this project, demand is defined as the number of completed rides per zone per hour.  
- **Why this proxy is used:** This metric is observable in the dataset and provides a practical estimate of where and when riders are requesting trips.  
- **Limitations:** It does not capture unmet demand, cancellations, or potential riders who do not request rides, and may be affected by data quality issues.

### Key Demand Drivers
- Season  
- Time of day  
- Weekday vs. weekend  
- Neighborhood / zone  
- Weather conditions  
- Special events  
- Holidays  

These factors influence the number of ride requests and their geographic distribution, and will be incorporated as features in predictive models.

### Decisions Supported by the Platform
If predictions are reliable, the platform can inform **driver allocation and distribution** across different parts of the city, ensuring supply meets expected demand while minimizing idle time and maximizing service efficiency.
