#!/bin/bash

docker network create book_store_network

docker run \
    --name book_store_db \
    --network book_store_network \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=book_store \
    -v book_store_data:/var/lib/postgresql/data \
    -d postgres:17

docker exec -i book_store_db psql -U postgres -d book_store < seeds/books.sql

docker build -t book_store .

docker run \
    -p 5001:5001 \
    --network book_store_network \
    book_store