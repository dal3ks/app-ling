-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title text,
    author text
);


-- The books!
INSERT INTO books (title, author) VALUES ('Misinterpretation', 'Ledia Xhoga');
INSERT INTO books (title, author) VALUES ('Drive Your Plow Over the Bones of the Dead', 'Olga Tokarczuk');
INSERT INTO books (title, author) VALUES ('Infinite Jest', 'David Foster Wallace');
INSERT INTO books (title, author) VALUES ('Blazing World', 'Margaret Cavendish');
INSERT INTO books (title, author) VALUES ('The Silmarillion', 'J R R Tolkien');