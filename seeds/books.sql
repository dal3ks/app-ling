-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title text,
    author text,
    rating int
);


-- The books!
INSERT INTO books (title, author, rating) VALUES ('Misinterpretation', 'Ledia Xhoga', 4);
INSERT INTO books (title, author, rating) VALUES ('Drive Your Plow Over the Bones of the Dead', 'Olga Tokarczuk', 4);
INSERT INTO books (title, author, rating) VALUES ('Infinite Jest', 'David Foster Wallace', 3);
INSERT INTO books (title, author, rating) VALUES ('Blazing World', 'Margaret Cavendish', 3);
INSERT INTO books (title, author, rating) VALUES ('The Silmarillion', 'J R R Tolkien', 5);