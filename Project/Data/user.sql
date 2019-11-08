DROP DATABASE IF EXISTS userInfor;
CREATE DATABASE userInfor;
use userInfor;

DROP TABLE if EXISTS users;
CREATE TABLE users(
	user_id INT NOT NULL AUTO_INCREMENT,
	username varchar(50),
	password varchar(50),
	PRIMARY KEY (user_id )
);

CREATE TABLE history(
	history_id INT NOT NULL AUTO_INCREMENT,
	user_id int,
	local_type ENUM('1','2','3'),
	address VARCHAR(50),
	PRIMARY Key(history_id)
);
CREATE TABLE information(
   user_id int,
   firstname VARCHAR(50),
   lastname VARCHAR(50),
   email VARCHAR(50),
   birth date,
   address varchar(50),
   PRIMARY Key(user_id)
);

INSERT INTO users (username, password)
VALUES ('fenglin', 'password');

INSERT INTO history(user_id, local_type, address)
values (1, 1, 'Rochester');

INSERT INTO information(user_id, firstname, lastname, email, birth, address)
Values (1, 'Feng', 'Lin', 'pytrade@gmail.com', '1996-08-06', 'FuckMyLife Street');

select user_id from users where username='fenglin' and password='password';
