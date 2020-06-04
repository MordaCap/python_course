ALTER TABLE employee
    DROP COLUMN employee_city;

ALTER TABLE employee
    ADD employee_city VARCHAR(255) NOT NULL;

DROP TABLE city;

INSERT INTO db_scheme_version(db_version, upgraded_on) VALUES ('1.4', now());
