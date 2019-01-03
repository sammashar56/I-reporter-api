"""contains all queries for tables"""

users = """ CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    firstname character varying (120) NOT NULL,
    lastname character varying (120) NOT NULL,
    email character varying (120) NOT NULL,
    Phone_no int NOT NULL,
    is_admin boolean NOT NULL,
    password character varying(250) NOT NULL
)"""

incidents = """ CREATE TABLE IF NOT EXISTS incidents (
    incident_id serial PRIMARY KEY NOT NULL,
    type_of_incident character varying (120) NOT NULL,
    comment character varying(250) NOT NULL,
    status character varying(120) NOT NULL,
    location character varying(120) NOT NULL,
    created_at character varying(120) NOT NULL,
    user_id int NOT NULL
    
)"""

queries = [users, incidents]
#FOREIGN KEY (user_id) REFERENCES users (user_id)
