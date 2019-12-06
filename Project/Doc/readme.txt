1. Download WeatherChecker.zip folder from myCourse dropbox

2. Unzip it and place it on the desktop

3. Open terminal

4. Create a new user for postgres sql
	a. Type: sudo su postgres
	b. Type: createuser --interactive --pwprompt
	c. Enter “user1” for username
	d. Enter “password1 for password”
	e. Enter “y” when asked question Shall the new role be a superuser
	f. Type “exit”

5. If you don’t have pip install in your machine, please do:
	a. Type: sudo apt install python-pip

6. Type: pip install requests

7. Type: sudo apt-get install python-tk

8. Type: sudo apt-get install python-psycopg2
	a. Enter “y” when asked do you want to continue

9. Change Directory to Desktop 10.Change Directory to Data folder inside WeatherChecker folder
	a. Type: cd WeatherChecker/Project/Data

10. Run sql file
	a. Type: psql
	b. Type: \i user.sql;
	c. Type: \q

11. Change Directory to View folder inside WeatherChecker folder
	a. Type: cd ../View

12. Run Program
	a. Type: python WeatherChecker_UI.py