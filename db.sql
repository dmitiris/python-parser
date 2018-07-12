CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name text,
    url text NOT NULL UNIQUE,
    "like" integer,
    dislike integer
);
