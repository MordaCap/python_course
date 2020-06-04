CREATE TABLE IF NOT EXISTS city (
    city_id SERIAL NOT NULL PRIMARY KEY,
    city_name VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO db_scheme_version(db_version, upgraded_on) VALUES ('1.1', now());
