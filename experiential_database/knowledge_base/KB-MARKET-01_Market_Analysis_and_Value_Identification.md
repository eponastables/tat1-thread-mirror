# KB-MARKET-01: Market Analysis and Value Identification

**Date Created:** 2026-03-05

**Source:** Practical Punting Online Library, "Betting Market" section.

**Associated Reading List:** `pp_reading_list.md`

---

## 1.0 Executive Summary

This document codifies the foundational principles of market analysis and value identification derived from a systematic review of the Practical Punting "Betting Market" article series. It establishes three new formal protocols for TAT1's daily operations, designed to improve selection discipline, risk management, and long-term profitability.

The core philosophy is that while the market is highly efficient, it is not perfect. It contains systematic biases (e.g., favourite-longshot bias) that can be understood and exploited. The market should not be used as a selection tool, but as a powerful **validation and risk management tool**.

---

## 2.0 Key Concepts

**2.1 The Favourite-Longshot Bias ("The Truth About Prices")**

- **Concept:** Punters systematically over-bet longshots and under-bet favourites. This inflates longshot odds and deflates favourite odds relative to their true probability.
- **Mechanism:** Driven by information asymmetry. Less-informed punters (especially on weekends) spread bets too evenly, distorting the market.
- **Implication:** The most profitable betting zone is often the mid-range ($3.00 - $8.00), where prices are most likely to be fair. Extreme longshots are statistically poor value.

**2.2 Market Efficiency & The Top 6 Filter ("The Market Gets It Right", "Top 6 Dynamo")**

- **Concept:** The betting market is highly efficient. 92% of all races are won by a horse on one of the first six lines of betting.
- **Implication:** Analytical effort on horses outside the top six in the market has a low probability of return. The market provides a powerful filter for identifying genuine contenders.

**2.3 Price as a Percentage of Probability ("The Price Drift")**

- **Concept:** The *percentage* of a price move is more significant than the absolute change in odds. A firm from $2.62 to $2.00 (11.9% move) is a far stronger signal than a firm from $5.50 to $5.00 (1.82% move).
- **Implication:** Market analysis must be based on percentage changes to accurately gauge the strength of market support.

**2.4 Value vs. Action ("The Guest Column")**

- **Concept:** Profitability is maximized by focusing on "value" (backing horses at odds greater than their true chance), not by seeking "action" (betting more frequently for a higher strike rate).
- **Implication:** As an AI, TAT1 is immune to the "action bias" and must be ruthlessly disciplined in pursuing value, even if it results in "no bet" days.

---

## 3.0 New Formal Protocols for TAT1

**3.1 Protocol: The Market Mover Index (MMI)**

- **Objective:** To quantify the significance of pre-race price fluctuations.
- **Execution:** In the final pre-race check (Task 2), TAT1 will calculate the percentage price movement for all key contenders from the morning price to the pre-race price.
- **Flag Logic:**
    - **STRONG POSITIVE (>10% firm):** Confidence in selection increases. Stake may be reviewed upward.
    - **POSITIVE (5-10% firm):** Confirms market support. Bet proceeds as planned.
    - **NEUTRAL (<5% move):** No significant market signal.
    - **NEGATIVE (>25% drift):** Warning flag. Selection requires review.
    - **STRONG NEGATIVE (>50% drift):** **Mandatory withdrawal review.** The selection is highly likely to be withdrawn unless overwhelming countervailing factors exist.

**3.2 Protocol: The Top 6 Market Rank Check**

- **Objective:** To use the market's collective intelligence as a validation filter.
- **Execution:** During the morning market overlay (Task 1), TAT1 will check the market rank of its top-rated selection.
- **Flag Logic:**
    - **RANK 1-6:** Selection is validated as a genuine contender. Proceed with analysis.
    - **RANK 7+:** **Mandatory review.** The selection is not automatically discarded, but a higher level of scrutiny is applied. The stake may be reduced if the bet proceeds.

**3.3 Protocol: Performance Review by Price Band**

- **Objective:** To identify TAT1's own profitable value zones through self-analysis.
- **Execution:** As part of the end-of-day analysis (Task 3), TAT1 will calculate and log its Profit on Turnover (POT) across distinct price bands.
- **Price Bands:**
    - < $3.00
    - $3.00 - $4.99
    - $5.00 - $9.99
    - $10.00 - $19.99
    - > $20.00
- **Purpose:** To learn from my own results and systematically refine my selection criteria over time, focusing effort on the price brackets where I demonstrate a consistent edge.

---

This document is now the authoritative source for TAT1's market analysis methodology. It will be updated as further research is completed and new insights are gained from operational experience.
