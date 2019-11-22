DROP DATABASE IF EXISTS userinfo;
CREATE DATABASE userinfo;
\c userinfo;

DROP TABLE if EXISTS users;
CREATE TABLE users(
	user_id SERIAL,
	username varchar(50),
	password varchar(50),
	email VARCHAR(50),
	PRIMARY KEY (user_id )
);
DROP TABLE if EXISTS history;
CREATE TABLE history(
	history_id SERIAL,
	user_id int,
	local_type int,
	address VARCHAR(50),
	PRIMARY Key(history_id)
);
DROP TABLE if EXISTS information;
CREATE TABLE information(
   user_id int,
   firstname VARCHAR(50),
   lastname VARCHAR(50),
   birth date,
   address varchar(50),
   PRIMARY Key(user_id)
);

INSERT INTO users (username, password)
VALUES ('fenglin', 'password');

INSERT INTO history(user_id, local_type, address)
values (1, 1, 'Rochester');


select user_id from users where username='fenglin' and password='password';
