"""contains all queries for tables"""

users = """ CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    firstname character varying (120) NOT NULL,
    lastname character varying (120) NOT NULL,
    email character varying (120) NOT NULL,
    Phone_no int NOT NULL,
    is_admin boolean NOT NULL,
    password int NOT NULL
)"""

incident = """ CREATE TABLE IF NOT EXISTS incidents (
    incident_id serial PRIMARY KEY NOT NULL,
    type_of_incident character varying (120) NOT NULL,
    comment character varying (250) NOT NULL,
    status character varying (120) NOT NULL,
    location varchar (120) NOT NULL,
    created_at varchar (120) NOT NULL
)"""

query = [users, incident]

