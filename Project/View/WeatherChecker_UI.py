import sys
import os, subprocess 
cwd = os.getcwd()
parent_dir = (os.path.abspath(os.path.join(cwd, os.pardir)))
sys.path.append(parent_dir)

from Tkinter import *
from Model.UserData import *
from Model.WeatherData import *
from Model.handleException import *
from Model.Reminder import *
login = None
user = UserData()
searchWeather = False


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def setReminder():
    global searchWeather
    global locationTextField
    option = 1
    cityName = locationTextField.get("1.0", 'end-1c')
    info = WeatherData(option, cityName)
    data = info.getWeatherInfo()
    msg = "Weather for "+cityName+"\n\n"
    msg += "Current Temperature: "+str(data[3])+" F\n"
    msg += "Lowest Temperature: "+str(data[1])+" F\n"
    msg += "Highest Temperature: "+str(data[2])+" F\n"
    msg += "Wind Speed: "+str(data[4])+" m/h\n"
    msg += "Cloud Percentage: X%\n"
    msg += "Cloud Description: "+data[5]


    if searchWeather == True:
    	email = user.getUserEmail()[0][0]
    	sendReminder(email,msg)
    else:
	print 'no'

def saveProfile():
    global firstnameTextField
    global lastnameTextField
    global birthdayTextField
    global addressTextField
    global profileLabel
    print(user.setInformation(firstnameTextField.get("1.0", 'end-1c'),
			lastnameTextField.get("1.0", 'end-1c'),
			birthdayTextField.get("1.0", 'end-1c'),
			addressTextField.get("1.0", 'end-1c')))
    if not user.setInformation(firstnameTextField.get("1.0", 'end-1c'),
			lastnameTextField.get("1.0", 'end-1c'),
			birthdayTextField.get("1.0", 'end-1c'),
			addressTextField.get("1.0", 'end-1c')):
	profileLabel.config(text='Invalid input',foreground="red")
    else:
	profileLabel.config(text='Saved',foreground="green")

def loginUI():
    global login
    global usernameTextFieldLogin
    global passwordTextFieldLogin
    global loginLabel
    
    login = Tk()
    login.title('Login')
    login.geometry("400x200+200+130")

    usernameLabel = Label(login, text="User Name", font=("Helvetica", 12))
    usernameLabel.place(x=60, y=30)

    usernameTextFieldLogin = Text(login)
    usernameTextFieldLogin.place(x=150, y=30, height=25, width=200)

    passwordLabel = Label(login, text="Password", font=("Helvetica", 12))
    passwordLabel.place(x=60, y=72)

    passwordTextFieldLogin = Text(login)
    passwordTextFieldLogin.place(x=150, y=70, height=25, width=200)

    loginLabel = Label(login, text="", font=("Helvetica", 12))
    loginLabel.place(anchor=CENTER, x=200, y=115)

    loginTo = Button(login, text="Login", command=checklogin)
    loginTo.place(anchor=CENTER, x=200, y=150, height=25, width=80)

    

    login.mainloop()


def checklogin():
    	global usernameTextFieldLogin
    	global passwordTextFieldLogin
        global loginLabel
	global user
        loginCheck = user.verify(usernameTextFieldLogin.get("1.0", 'end-1c'),passwordTextFieldLogin.get("1.0", 'end-1c'))
   	if loginCheck == False: 
		loginLabel.config(text='Wrong Username/Password',foreground="red")
   	elif loginCheck == True: 
	
		global login
		login.destroy()
		main.geometry("1000x400+100+100")

		loginButton.place(anchor=CENTER, x=830, y=20, height=25, width=80)
		signupButton.place(anchor=CENTER, x=950, y=20, height=25, width=80)
		orLabel.place(x=880, y=10)
		logoutButton = Button(main, text="Logout", bg='#cceeff',command = restart_program)
		logoutButton.place(anchor=CENTER, x=830, y=20, height=25, width=80)

		reminderLabel = Label(main, text="Set Reminder", font=("Times", 12))
		reminderLabel.place(x=550, y=70)

		dateLabel = Label(main, text="Date", font=("Times", 12))
		dateLabel.place(x=600, y=100)

		dateTextField = Text(main)
		dateTextField.place(x=650, y=100, height=25, width=110)

		timeLabel = Label(main, text="Time", font=("Times", 12))
		timeLabel.place(x=780, y=100)

		timeTextField = Text(main)
		timeTextField.place(x=830, y=100, height=25, width=80)

		options = ('Everyday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
		var = StringVar();
		var.set(options[0])
		dayOptionMenu = OptionMenu(main, var, *options)
		dayOptionMenu.place(x=635, y=150, height=30, width=130)

		time2Label = Label(main, text="Time", font=("Times", 12))
		time2Label.place(x=780, y=150)

		time2TextField = Text(main)
		time2TextField.place(x=830, y=150, height=25, width=80)

		orReminderLabel = Label(main, text="or", font=("Times", 12))
		orReminderLabel.place(x=760, y=125)

		setButton = Button(main, text="Set", command = setReminder)
		setButton.place(anchor=CENTER, x=950, y=138, height=25, width=60)

		historyLabel = Label(main, text="Search History", font=("Times", 12))
		historyLabel.place(x=550, y=200)

		historyTextField = Text(main)
		historyTextField.place(x=600, y=230, height=100, width=300)

		scrollbar = Scrollbar(historyTextField)
		scrollbar.pack(side=RIGHT, fill=Y)

		historyTextField.config(yscrollcommand=scrollbar.set)
		scrollbar.config(command=historyTextField.yview)

		historyClear = Button(main, text="Clear")
		historyClear.place(anchor=CENTER, x=950, y=270, height=25, width=60)
		
		if not user.viewUserInformation():
			userWelcomeMsg = "Welcome"
		else:
			userWelcomeMsg = "Welcome " + str(user.viewUserInformation()[0][1])
		userWelcomeLabel = Label(main, text=userWelcomeMsg, font=("Helvetica", 12))
		userWelcomeLabel.place(x=10, y=2)
		
		editButton = Button(main, text="Edit Profile", bg='#cceeff', command=editProfile)
		editButton.place(x=10, y=25, height=20, width=100)


def editProfile():
	global firstnameTextField;
	global lastnameTextField;
	global birthdayTextField;
	global addressTextField;
        global profileLabel;
	profile = Tk()
	profile.title('Profile')
	profile.geometry("400x270+200+130")

	firstnameLabel = Label(profile, text="First Name", font=("Helvetica", 12))
	firstnameLabel.place(x=60, y=30)
		
	firstnameTextField = Text(profile)
	firstnameTextField.place(x=150, y=30, height=25, width=200)
	firstnameTextField.insert(END,str(user.viewUserInformation()[0][1]))

	lastnameLabel = Label(profile, text="Last Name", font=("Helvetica", 12))
	lastnameLabel.place(x=60, y=72)
	
	lastnameTextField = Text(profile)
	lastnameTextField.place(x=150, y=72, height=25, width=200)
        lastnameTextField.insert(END,str(user.viewUserInformation()[0][2]))

	birthdayLabel = Label(profile, text="Birthday", font=("Helvetica", 12))
	birthdayLabel.place(x=60, y=114)
	
	birthdayTextField = Text(profile)
	birthdayTextField.place(x=150, y=114, height=25, width=200)
	birthdayTextField.insert(END,str(user.viewUserInformation()[0][3]))

	addressLabel = Label(profile, text="Address", font=("Helvetica", 12))
	addressLabel.place(x=60, y=156)
	
	addressTextField = Text(profile)
	addressTextField.place(x=150, y=156, height=25, width=200)
	addressTextField.insert(END,str(user.viewUserInformation()[0][4]))

	saveButton = Button(profile, text="Save",command=saveProfile)
	saveButton.place(anchor=CENTER, x=200, y=228, height=25, width=80)

	profileLabel = Label(profile, text="", font=("Helvetica", 12))
    	profileLabel.place(anchor=CENTER, x=200, y=195)

	profile.mainloop()

def signUpUI():
	global usernameTextFieldSignUp
	global passwordTextFieldSignUp
	global emailTextFieldSignUp
	global signUpLabel

	signUp = Tk()
	signUp.title('Sign Up')
	signUp.geometry("400x230+200+130")

	usernameLabel = Label(signUp, text="User Name", font=("Helvetica", 12))
	usernameLabel.place(x=60, y=30)

	usernameTextFieldSignUp = Text(signUp)
	usernameTextFieldSignUp.place(x=150, y=30, height=25, width=200)

	passwordLabel = Label(signUp, text="Password", font=("Helvetica", 12))
	passwordLabel.place(x=60, y=72)

	passwordTextFieldSignUp = Text(signUp)
	passwordTextFieldSignUp.place(x=150, y=70, height=25, width=200)

	emailLabel = Label(signUp, text="Email", font=("Helvetica", 12))
	emailLabel.place(x=60, y=114)

	emailTextFieldSignUp = Text(signUp)
	emailTextFieldSignUp.place(x=150, y=110, height=25, width=200)

	signUpLabel = Label(signUp, text="", font=("Helvetica", 12))
    	signUpLabel.place(anchor=CENTER, x=200, y=150)

	signupButton = Button(signUp, text="Sign Up", command=checkSignUp)
	signupButton.place(anchor=CENTER, x=200, y=180, height=25, width=80)

	signUp.mainloop()


def checkSignUp():
	global user
    	global usernameTextFieldSignUp
	global passwordTextFieldSignUp
	global emailTextFieldSignUp
	global signUpLabel
        signUpCheck = user.signUp(usernameTextFieldSignUp.get("1.0", 'end-1c'),passwordTextFieldSignUp.get("1.0", 'end-1c'),emailTextFieldSignUp.get("1.0", 'end-1c'))
   	if signUpCheck != True: 
	     signUpLabel.config(text=signUpCheck,foreground="red")
   	elif signUpCheck == True: 
	     signUpLabel.config(text="Congratulations!",foreground="green")

def search():
	global locationTextField
	global currentTempLabel
	global lowestTempLabel
	global highestTempLabel
	global windSpeedLabel
	global cloudPrecentageLabel
	global cloundDescriptionLabel
	global searchLabel
	global searchWeather
	cityName = locationTextField.get("1.0", 'end-1c')
	option = 1
	handleError = handleException(option, cityName)
	if handleError.inputError():
		info = WeatherData(option, cityName)
		data = info.getWeatherInfo()
		currentTempLabel.config(text="Current Temperature: "+str(data[3])+" F")
		lowestTempLabel.config(text="Lowest Temperature: "+str(data[1])+" F")
		highestTempLabel.config(text="Highest Temperature: "+str(data[2])+" F")
		windSpeedLabel.config(text="Wind Speed: "+str(data[4])+" m/h")
		cloudPrecentageLabel.config(text="Humidity: "+str(data[6])+"%")
		cloundDescriptionLabel.config(text="Cloud Description: "+data[5])
		searchLabel.config(text="")	
		searchWeather = True
		##print(user.viewUserHistory())
	else:
		searchLabel.config(text="Invalidate input!",foreground="red")
		currentTempLabel.config(text="Current Temperature: X F")
		lowestTempLabel.config(text="Lowest Temperature: X F")
		highestTempLabel.config(text="Highest Temperature: X F")
		windSpeedLabel.config(text="Wind Speed: X m/h")
		cloudPrecentageLabel.config(text="Humidity: X%")
		cloundDescriptionLabel.config(text="Cloud Description: X")	
		searchWeather = False

		

global locationTextField
global currentTempLabel
global lowestTempLabel
global highestTempLabel
global windSpeedLabel
global cloudPrecentageLabel
global cloundDescriptionLabel
global searchLabel
main = Tk()
main.title('Weather Checker')
main.geometry("600x400+100+100")

appNameLabel = Label(main, text="Weather Checker", font=("Helvetica", 20))
appNameLabel.place(anchor=CENTER, x=300, y=85)

locationLabel = Label(main, text="Location", font=("Helvetica", 12))
locationLabel.place(x=120, y=152)

locationTextField = Text(main)
locationTextField.place(x=190, y=150, height=25, width=200)

searchButton = Button(main, text="Search", command=search)
searchButton.place(x=410, y=150, height=25, width=80)

loginButton = Button(main, text="Login", bg='#cceeff', command=loginUI)
loginButton.place(x=380, y=10, height=25, width=80)

orLabel = Label(main, text="or", font=("Helvetica", 12))
orLabel.place(x=470, y=10)

signupButton = Button(main, text="Sign Up", bg='#cceeff', command=signUpUI)
signupButton.place(x=500, y=10, height=25, width=80)

currentTempLabel = Label(main, text="Current Temperature: X F", font=("Helvetica", 12))
currentTempLabel.place(x=70, y=220)

lowestTempLabel = Label(main, text="Lowest Temperature: X F", font=("Helvetica", 12))
lowestTempLabel.place(x=70, y=255)

highestTempLabel = Label(main, text="Highest Temperature: X F", font=("Helvetica", 12))
highestTempLabel.place(x=70, y=290)

windSpeedLabel = Label(main, text="Wind Speed: X m/h", font=("Helvetica", 12))
windSpeedLabel.place(x=330, y=220)

cloudPrecentageLabel = Label(main, text="Humidity: X%", font=("Helvetica", 12))
cloudPrecentageLabel.place(x=330, y=255)

cloundDescriptionLabel = Label(main, text="Cloud Description: X", font=("Helvetica", 12))
cloundDescriptionLabel.place(x=330, y=290)

searchLabel = Label(main, text="", font=("Helvetica", 12))
searchLabel.place(anchor=CENTER, x=300, y=340)

cityRadio = Radiobutton(main, text="City Name", value=1)
cityRadio.place(anchor=CENTER, x=156, y=195)

zipRadio = Radiobutton(main, text="Zip Code", value=2)
zipRadio.place(anchor=CENTER, x=253, y=195)

gcRadio = Radiobutton(main, text="Geographic Coordinates", value=3)
gcRadio.place(anchor=CENTER, x=396, y=195)


main.mainloop()










