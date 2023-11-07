CREATE DATABASE pharmchan;
CREATE USER pharmchandjango WITH ENCRYPTED PASSWORD 'pharmchan2024';
ALTER ROLE pharmchandjango SET client_encoding TO 'utf8';
ALTER ROLE pharmchandjango SET default_transaction_isolation TO 'read committed';
ALTER ROLE pharmchandjango SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pharmchan TO pharmchandjango;
CREATE SCHEMA pharmchandjango;
GRANT USAGE ON SCHEMA pharmchandjango TO pharmchandjango;
GRANT CREATE ON SCHEMA pharmchandjango TO pharmchandjango;
