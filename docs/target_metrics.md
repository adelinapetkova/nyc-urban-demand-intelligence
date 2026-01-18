# Target Metrics

This document defines the key metrics used in the NYC Urban Demand Intelligence Platform.  
These metrics reflect how ride-hailing performance is evaluated from both an operational and customer-experience perspective.

---

## 1. Ride Demand

- **Metric:** Ride demand  
- **Definition:** Number of completed rides  
- **Unit:** Count  
- **Granularity:** NYC zone × hour  
- **Business meaning:** Proxy for customer demand and overall service load  

Ride demand is the primary target metric of this project. It represents how many rides are successfully completed within a given zone and time window. At an aggregated level, this metric serves as a practical approximation of how many customers are requesting transportation services and how much load the system is experiencing.

While ride demand does not capture unmet or canceled requests, it provides a consistent and observable signal that can be modeled and analyzed using historical data. Predicting ride demand enables better planning of driver allocation, identification of high-demand areas, and anticipation of demand spikes.

---

## 2. Wait Time

### Conceptual Definition
Wait time represents the time interval between a customer submitting a ride request and the arrival of the vehicle at the pickup location.

### Business Relevance
Wait time is a critical indicator of:
- Operational efficiency  
- Supply–demand balance  
- Customer satisfaction  

Longer wait times often lead to frustration, reduced trust in the service, and potentially lost customers, while shorter wait times are associated with higher service quality and user retention.

### Data Limitations
Accurately measuring wait time requires access to detailed request-level data, including:
- Timestamp of ride request creation  
- Timestamp of vehicle arrival  

In real-world ride-hailing systems, this data is typically collected through mobile applications. However, in publicly available trip datasets, such information is often unavailable or incomplete. As a result, wait time is treated in this project as a **conceptually important but not directly observable metric**, acknowledged as a limitation of the dataset.

---

## 3. Churn

### Conceptual Definition
In the context of ride-hailing, churn refers to a sustained decrease in platform usage over time, indicating that users are becoming less active or abandoning the service.

### Who Churns?
While churn can apply to both riders and drivers, this project primarily focuses on **rider churn**, as rider behavior is more directly reflected in aggregated trip data.

### Proxy Definition Using Aggregate Data
Since individual user identifiers are not available, churn is approximated using **aggregate demand patterns**, such as:
- Persistent decreases in ride demand within specific zones  
- Declining demand during previously high-activity time periods  
- Seasonal or time-based demand drop-offs that are not explained by known external factors  

These patterns can serve as indirect indicators of reduced user engagement at the zone or temporal level.

### Limitations
This proxy does not capture individual user behavior and cannot distinguish between true churn and temporary demand fluctuations caused by external factors. As a result, churn analysis in this project is exploratory and illustrative rather than definitive.

---

## Summary

The metrics defined above establish a clear analytical foundation for the project. Ride demand serves as the primary measurable target, while wait time and churn provide important conceptual context for evaluating service quality and long-term platform health. Together, these metrics guide the modeling, analysis, and interpretation of results throughout the project.
