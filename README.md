# YouTube Trending Data Engineering Pipeline

## Overview
This project is an end-to-end data engineering pipeline built using Python and PostgreSQL (Supabase).
It ingests the Kaggle YouTube Trending Videos dataset, cleans and transforms the data, and loads it into a structured data warehouse for analytics.

The goal of this project is to demonstrate core data engineering concepts including ETL pipelines, data modeling, and warehouse loading.

---

## Architecture
Kaggle CSV / JSON
↓
Python (pandas)
↓
ETL Pipeline (Extract → Transform → Load)
↓
PostgreSQL Data Warehouse (Supabase)


---

## Data Model

### Dimension Table
**categories**
- category_id (PK)
- category_name

### Fact Table
**youtube_vids**
- video_id
- trending_date
- title
- channel_title
- category_id (FK)
- views, likes, dislikes, comment_count
- flags (comments_disabled, ratings_disabled, video_error_or_removed)

This design follows a dimensional modeling approach commonly used in analytics systems.

---

## Technologies Used
- Python
- pandas
- PostgreSQL (Supabase)
- SQLAlchemy
- Kaggle Dataset

---

## Pipeline Steps

1. **Extract**
   - Load CSV and JSON data from Kaggle using pandas and json

2. **Transform**
   - Parse and standardize date and timestamp fields
   - Handle missing values
   - Enforce correct data types
   - Separate dimension and fact data

3. **Load**
   - Load cleaned data into PostgreSQL using batch inserts
   - Maintain referential integrity between tables
