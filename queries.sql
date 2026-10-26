-- 1. Total anime watched
SELECT COUNT(*) FROM anime;

-- 2. Top 5 highest-rated anime
SELECT a.title, w.score 
FROM watch_history w 
JOIN anime a ON w.anime_id = a.anime_id 
WHERE w.score > 0 
ORDER BY w.score DESC 
LIMIT 5;

-- 3. How many hours spent watching TV shows vs Movies (assuming ~24 mins per episode)
SELECT a.type, SUM(w.watched_episodes * 24) / 60 AS hours_watched
FROM watch_history w
JOIN anime a ON w.anime_id = a.anime_id
WHERE w.watched_episodes > 0
GROUP BY a.type;

-- 4. Show all anime I dropped and how far I got
SELECT a.title, w.watched_episodes, a.total_episodes
FROM watch_history w
JOIN anime a ON w.anime_id = a.anime_id
WHERE w.status = 'Dropped'
ORDER BY w.watched_episodes DESC;