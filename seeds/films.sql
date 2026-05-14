-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title text,
    genre text,
    release_date int
);


-- The films!
INSERT INTO films (title, genre, release_date) VALUES ('The Shawshank Redemption', 'Drama', 1994);
INSERT INTO films (title, genre, release_date) VALUES ('The Dark Knight', 'Action', 2008);
INSERT INTO films (title, genre, release_date) VALUES ('Lord of the Rings: The Fellowship of the Ring', 'Fantasy', 2001);
INSERT INTO films (title, genre, release_date) VALUES ('The Matrix', 'Sci-fi', 1999);
INSERT INTO films (title, genre, release_date) VALUES ('One Flew over the Cuckoos Nest', 'Dark Comedy', 1975);