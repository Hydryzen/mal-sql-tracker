import xml.etree.ElementTree as ET
import psycopg2
import os

# 1. Database credentials
DB_NAME = "anime_tracker"
DB_USER = "postgres"
DB_PASS = os.environ.get("DB_PASS", "your_password_here")
DB_HOST = "localhost"
DB_PORT = "5432"

def main():
    # 2. Connect to the database
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()
        print("Connected to database.")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return

    # 3. Parse the XML file
    # Make sure this filename matches your actual file!
    xml_file = "animelist_1792979602_-_15008784.xml" 
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 4. Loop through every anime in the XML
    for anime in root.findall('anime'):
        anime_id = int(anime.find('series_animedb_id').text)
        title = anime.find('series_title').text or "Unknown"
        anime_type = anime.find('series_type').text or "Unknown"
        total_eps = int(anime.find('series_episodes').text or 0)
        
        status = anime.find('my_status').text
        score = int(anime.find('my_score').text or 0)
        watched = int(anime.find('my_watched_episodes').text or 0)
        
        # Handle dates (MAL uses '0000-00-00' which Postgres rejects)
        start_date = anime.find('my_start_date').text
        finish_date = anime.find('my_finish_date').text
        
        start_date = None if start_date == '0000-00-00' else start_date
        finish_date = None if finish_date == '0000-00-00' else finish_date

        # 5. Insert into 'anime' table (ON CONFLICT prevents duplicates)
        cur.execute("""
            INSERT INTO anime (anime_id, title, type, total_episodes)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (anime_id) DO NOTHING;
        """, (anime_id, title, anime_type, total_eps))

        # 6. Insert into 'watch_history' table
        cur.execute("""
            INSERT INTO watch_history (anime_id, status, score, watched_episodes, start_date, finish_date)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (anime_id, status, score, watched, start_date, finish_date))

    # 7. Save changes and close
    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded successfully!")

if __name__ == "__main__":
    main()