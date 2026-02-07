# Statistical Report

---

## 1. Objective of this analysis

The objective of this report is to quantify and statistically validate patterns in ride-hailing demand in New York City using classical inferential statistics and Bayesian methods.

The focus is on understanding:

- whether demand differs systematically across time
- whether weather conditions influence demand
- when peak demand occurs
- how uncertain our estimates of demand truly are

The analysis is performed on aggregated ride demand at the zone–hour level.

---

## 2. Data description

The dataset consists of NYC Yellow Taxi trip records (January–March 2019) aggregated to pickup zone and hourly time resolution.

Each observation represents the number of completed rides in a specific zone during a specific hour.

Additional features include:
- hour of day
- day of week
- weekend indicator
- weather information (precipitation, temperature, and a bad weather indicator)

---

## 3. Hypotheses investigated

This study investigates several business-relevant hypotheses regarding ride demand.

### 3.1 Temporal demand differences

**Null hypothesis (H0):**  
Mean ride demand is equal across the compared time periods.

**Alternative hypothesis (H1):**  
Mean ride demand differs between the compared time periods.

The comparisons include, for example:
- peak hours versus off-peak hours
- weekdays versus weekends

---

### 3.2 Weather impact on demand

**Null hypothesis (H0):**  
Mean ride demand is the same during bad weather and normal weather.

**Alternative hypothesis (H1):**  
Mean ride demand differs during bad weather.

---

## 4. Confidence interval analysis

Confidence intervals were constructed for the mean ride demand.
The intervals quantify the uncertainty around the estimated average demand.

The confidence interval represents a range of plausible values for the true population mean demand, given the observed data. This allows conclusions to be based not only on point estimates but also on the uncertainty associated with those estimates.

---

## 5. Hypothesis testing results

Formal hypothesis tests were applied to compare demand distributions between selected groups.

For each test:

- a test statistic was computed
- a p-value was obtained

The results indicate whether the observed differences are statistically significant under standard significance thresholds.

The tests provide statistical evidence for:
- systematic temporal variation in demand
- differences between selected time-based categories

---

## 6. Weather impact analysis

Hourly weather data was merged with the demand data.

The following variables were used:
- precipitation (mm)
- temperature (°C)
- a binary bad weather indicator

Demand under bad weather conditions was compared to demand under normal conditions.
The analysis shows that weather conditions have a measurable but limited impact on aggregated hourly demand. The magnitude of the weather effect is substantially smaller than the effect of time-of-day patterns.

---

## 7. Peak hour analysis

Peak demand was defined as the hour of day with the highest average ride demand.

The analysis shows that:

- demand follows a clear daily cycle
- a consistent evening peak is observed across the city

This confirms that temporal structure is one of the dominant drivers of demand variability.

---

## 8. Bayesian inference of mean demand

A Bayesian model was fitted to estimate the underlying distribution of hourly demand.

The model assumes that the observed demand follows a Normal distribution with unknown mean and standard deviation.

Posterior distributions were estimated for:
- the mean demand
- the standard deviation

This provides a full probabilistic description of uncertainty rather than a single point estimate.
Credible intervals were computed directly from the posterior distributions.

---

## 9. Posterior predictive validation

Posterior predictive sampling was performed in order to assess the adequacy of the Bayesian model.

Simulated demand values generated from the fitted model were compared to the observed demand distribution.
The posterior predictive distribution captures the central tendency of the observed demand well, while extreme values are less accurately reproduced.

This indicates that the simple Normal model is suitable as a baseline probabilistic model,
but more expressive models may be required to better capture extreme demand spikes.

---

## 10. Business interpretation

From an operational perspective, the results show that:

- ride demand exhibits strong and stable time-of-day structure
- peak hours can be reliably identified
- weather effects exist but are secondary compared to temporal drivers

The Bayesian estimates allow planners to reason in terms of ranges of expected demand rather than fixed values.

This supports:

- capacity planning
- risk-aware driver allocation
- scenario-based operational decision-making

---

## 11. Limitations

Several limitations must be acknowledged:
- spatial interactions between neighboring zones are not considered
- only a short time horizon (three months) is analyzed
- the Bayesian model assumes normally distributed demand

