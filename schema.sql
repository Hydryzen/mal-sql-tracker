CREATE TABLE anime (
    anime_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    total_episodes INT NOT NULL
);

CREATE TABLE watch_history (
    history_id SERIAL PRIMARY KEY,
    anime_id INT NOT NULL REFERENCES anime(anime_id),
    status VARCHAR(50) NOT NULL,
    score INT CHECK (score >= 0 AND score <= 10),
    watched_episodes INT NOT NULL,
    start_date DATE,
    finish_date DATE
);