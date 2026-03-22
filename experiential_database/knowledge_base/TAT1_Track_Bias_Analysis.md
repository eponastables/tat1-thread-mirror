# TAT1 Knowledge Base: Track Bias Analysis

**Source**: RC Research Report, ISSUE-016 (2026-03-22)

---

## 1. Core Principle

Track bias is a deviation from a track's historical performance norm. The goal is to quantify this deviation for a specific race day, not just identify historical patterns. A track that always favours inside barriers is a feature; a track that favours inside barriers *more than usual* on a given day is a bias.

## 2. Primary Methodology: Finishing Speed % (FS%) Deviation Analysis

This is the most robust method for detecting track bias from sectional times. It measures how a horse's closing speed compares to its own average speed for the race, providing a pace-adjusted measure of performance.

### 2.1. Formula: Finishing Speed %

```
FS% = (100 * sectional_distance * overall_time) / (sectional_time * overall_distance)
```

### 2.2. Implementation Steps

1.  **Calculate FS% for Every Horse:** Apply the formula to every runner in the historical dataset.
2.  **Establish Par FS% Tables:** Group the data by `track`, `distance`, and `going`. The median FS% for each combination becomes the **par**.
3.  **Calculate FS% Deviation:** For each horse in a new race, calculate `fs_deviation = actual_fs_pct - par_fs_pct`.
4.  **Detect Bias with Statistical Tests:**
    *   Group horses by running lane (inside, middle, outside).
    *   Use a **Mann-Whitney U test** to compare the distribution of `fs_deviation` between the groups.
    *   A statistically significant p-value (p < 0.05) indicates a genuine track bias.

## 3. Secondary Methodology: Winner Profiling

This is a qualitative method for identifying pace bias (e.g., front-runner vs. closer bias).

1.  **Classify Winners:** For each race, classify the winner's running style (Leader, On-Pace, Midfield, Backmarker).
2.  **Identify Patterns:** A disproportionate number of winners with the same running style suggests a pace bias.

## 4. Visualisation

The most effective visualisation is a **scatter plot** for each race meeting:

*   **X-axis:** Barrier Draw or Running Lane
*   **Y-axis:** `fs_deviation`
*   **Hue:** Finishing Position

A clear trend in this plot provides strong visual evidence of bias.

## 5. Best Practices

*   **Minimum Sample Size:** A full day's meeting (8-10 races) is the minimum for a reliable reading.
*   **Avoid Confirmation Bias:** Systematically document the results for every meeting, regardless of the outcome.
*   **Distinguish Bias from Feature:** A genuine bias is a deviation from the historical norm, isolated by the `fs_deviation` from par.
