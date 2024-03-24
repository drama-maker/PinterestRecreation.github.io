-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "email" TEXT NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

CREATE TABLE search_history (
    id SERIAL PRIMARY KEY,
    search_query TEXT NOT NULL,
    search_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE profile_visibility (
    id SERIAL PRIMARY KEY,
    is_private_profile BOOLEAN NOT NULL DEFAULT FALSE,
    is_search_privacy BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE pins (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    image_url TEXT NOT NULL,
    search_keywords TEXT[],
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE boards (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);