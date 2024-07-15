CREATE SCHEMA IF NOT EXISTS content;

SET TIME ZONE 'Europe/Moscow';

CREATE TABLE IF NOT EXISTS content.transit_records (
    id uuid PRIMARY KEY,
    place VARCHAR(100) NOT NULL,
    truck_id uuid NOT NULL,
    read_time timestamp WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS content.trucks (
    id uuid PRIMARY KEY,
    truck_num VARCHAR(100) NOT NULL UNIQUE,
    marker_id_1 VARCHAR(100) NOT NULL UNIQUE,
    marker_id_2 VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP

);

CREATE UNIQUE INDEX truck_markers_idx ON content.trucks (marker_id_1, marker_id_2);

CREATE TABLE IF NOT EXISTS content.logs (
    id uuid PRIMARY KEY,
    marker_id_1 VARCHAR(100),
    marker_id_2 VARCHAR(100),
    info VARCHAR(100) NOT NULL,
    place VARCHAR(100) NOT NULL,
    antenna SMALLINT,
    created_at timestamp WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
