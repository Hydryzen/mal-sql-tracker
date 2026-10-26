# MyAnimeList SQL Tracker

A Data Engineering project that parses my personal MyAnimeList XML export and loads it into a PostgreSQL database for analytical querying.

## Features
- **ETL Pipeline:** A Python script (`basedate.py`) uses `xml.etree.ElementTree` to parse a 300+ item XML file.
- **Relational Schema:** Normalized database schema with Primary Keys, Foreign Keys, and CHECK constraints.
- **Data Loading:** Utilizes `psycopg2` to insert data safely and efficiently.
- **Analytics:** Includes a file (`queries.sql`) with complex analytical queries using `JOIN`, `GROUP BY`, and aggregate functions.

## How to Run

1. **Set up PostgreSQL:**
   Create a database and run the schema:
   ```bash
   psql -U postgres -c "CREATE DATABASE anime_tracker;"
   psql -U postgres -d anime_tracker -f schema.sql