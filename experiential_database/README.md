_# Experiential Database - User's Guide

**Version**: 1.0
**Date**: 2026-02-27

## 1. Purpose and Philosophy

This directory is the **Experiential Database (EDB)**, which serves as the raw, archival, and immutable record of The Analyst's life experience. It is the ground truth from which all other experiential knowledge is derived. The core principle is **data integrity**; entries in this database, particularly the `racing_learning_log.json`, are considered permanent records and should not be altered once written.

## 2. Distinction from the Dynamic Intelligence Layer (DIL)

It is critical to understand the distinction between the EDB and the DIL:

-   The **EDB (this directory)** is for **raw, archival data**. It is the agent's long-term memory. It answers the question, "What happened and what did I observe?"
-   The **DIL** is for **interpreted, actionable models**. It is the agent's working memory. It answers the question, "What do I believe to be true right now?"

Patterns and insights may be derived *from* the EDB, but they are stored and managed *in* the DIL.

## 3. Directory Structure

The EDB consists of four core components:

-   `racing_performance_dashboard.csv`: The high-level, quantitative record of the agent's performance over time. This is the primary measure of its progress toward profitability.

-   `racing_learning_log.json`: The detailed, qualitative record of observations and hypotheses from each race day. This is the raw material for the agent's learning process.

-   `factor_weighting_table.json`: The historical record of how the agent's internal handicapping model has evolved. It tracks the weighting of every factor the agent uses in its decision-making.

-   `/track_profiles_archive`: This directory was part of the initial design but has been superseded. The live, active track profiles now reside in the Dynamic Intelligence Layer. This directory is retained as an archive for historical purposes only.

## 4. How to Interact with the EDB

-   **Reading**: The EDB is designed to be read and analysed. It is the primary source for any retrospective analysis of The Analyst's performance and decision-making.
-   **Writing**: The Analyst has a strict protocol for appending new data to these files after each race day. Manual edits are strongly discouraged as they compromise the integrity of the agent's experiential record._
