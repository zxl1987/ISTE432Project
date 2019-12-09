import sys
import os, subprocess 
import threading
import time
import datetime as dt
cwd = os.getcwd()
parent_dir = (os.path.abspath(os.path.join(cwd, os.pardir)))
sys.path.append(parent_dir)

from Tkinter import *
import ttk
from Model.UserData import *
from Model.WeatherData import *
from Model.handleException import *
from Model.Reminder import *
from Model.SignUpEmail import *
main = Tk()
emailTimerController = True
emailTimerCirculationController = True
login = None
user = UserData()
searchWeather = False
global localoption
localoption=1
reminderArr = []
reminderCirculationArr = []
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def setReminderEmail(option,cityName):
		
	global reminderMsgLabel
	info = WeatherData(option, cityName)
	data = info.getWeatherInfo()
	msg = "Weather for "+cityName+"\n\n"
	msg += "Current Temperature: "+str(data[3])+" F\n"
	msg += "Lowest Temperature: "+str(data[1])+" F\n"
	msg += "Highest Temperature: "+str(data[2])+" F\n"
	msg += "Wind Speed: "+str(data[4])+" m/h\n"
	msg += "Humidity: "+str(data[6])+"%\n"
	msg += "Cloud Description: "+data[5]

	email = user.getUserEmail()[0][0]
	if sendReminder(email,msg):
		reminderMsgLabel.config(text='Reminder set completed.',foreground="green")

	
def setReminder1():
	global dateTextField
	global timeTextField
	global reminderMsgLabel
	global locationTextField
	global localoption
	try:
		time = dateTextField.get("1.0", 'end-1c') + " " + timeTextField.get("1.0", 'end-1c')
		reminderTime = dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
	except:
		reminderMsgLabel.config(text='Date/Time Incorrect in format\nyyyy-mm-dd hh:mm:ss.',foreground="red")
		return


	if searchWeather == True:
		cityName = locationTextField.get("1.0", 'end-1c')
		searchArr = []
		searchArr.append(localoption)
		searchArr.append(cityName)
		searchArr.append(reminderTime)
		reminderArr.append(searchArr)
		reminderMsgLabel.config(text='Reminder Set!',foreground="green")
	else:
		reminderMsgLabel.config(text='Please Search first.',foreground="red")
		return
	

    

def setReminder2():
    	global time2TextField
	global var 
	global locationTextField
	global localoption
	global reminderMsgLabel
	cityName = locationTextField.get("1.0", 'end-1c')
	day = var.get()
	dayNum = ''
	if day == 'Monday': dayNum = 0	
	elif day == 'Tuesday': dayNum = 1 
	elif day == 'Wednesday': dayNum = 2
	elif day == 'Thursday': dayNum = 3
	elif day == 'Friday': dayNum = 4 
	elif day == 'Saturday': dayNum = 5 
	elif day == 'Sunday': dayNum = 6 
	elif day == 'Everyday': dayNum = 7

	

	try:
		time = time2TextField.get("1.0", 'end-1c')		
		reminderTime = dt.datetime.strptime(time, '%H:%M:%S')
	except:
		reminderMsgLabel.config(text='Time Incorrect in format\nhh:mm:ss.',foreground="red")
		return
	

	if searchWeather == True:
		arr = []
		arr.append(localoption)
		arr.append(cityName)
		arr.append(dayNum)
		arr.append(time)
		reminderCirculationArr.append(arr)
		reminderMsgLabel.config(text='Reminder Set!',foreground="green")
	else:
		reminderMsgLabel.config(text='Please Search first.',foreground="red")
		return
	


def emailTimer():
	global emailTimerController
	while(emailTimerController):
		time.sleep(1)
		now = dt.datetime.now()
	
		for emailTime in reminderArr:
			if now >= emailTime[2]:
				setReminderEmail(emailTime[0],emailTime[1])
				reminderArr.remove(emailTime)

def emailCirculationTimer():
	global emailTimerCirculationController
	while(emailTimerCirculationController):		
		time.sleep(1)
		now = dt.datetime.now()
		nowTime = dt.datetime.strftime(now, '%H:%M:%S')
		for emailTime in reminderCirculationArr:
			if emailTime[2] == 7:
				if nowTime == emailTime[3]:
					setReminderEmail(emailTime[0],emailTime[1])
			else:
				if now.weekday() == emailTime[2]:
					if nowTime == emailTime[3]:
						setReminderEmail(emailTime[0],emailTime[1])
					
		
		
def on_closing():
	print "close"
	global main, emailTimerController, emailTimerCirculationController
	emailTimerController = False
	emailTimerCirculationController = False
	time.sleep(1.1)
	main.destroy()


def saveProfile():
    global firstnameTextField
    global lastnameTextField
    global birthdayTextField
    global addressTextField
    global profileLabel
    global emailTextField
    print(user.setInformation(firstnameTextField.get("1.0", 'end-1c'),
			lastnameTextField.get("1.0", 'end-1c'),
			birthdayTextField.get("1.0", 'end-1c'),
			addressTextField.get("1.0", 'end-1c')))
    if not user.setInformation(firstnameTextField.get("1.0", 'end-1c'),
			lastnameTextField.get("1.0", 'end-1c'),
			birthdayTextField.get("1.0", 'end-1c'),
			addressTextField.get("1.0", 'end-1c')): 
	profileLabel.config(text='Invalid input',foreground="red")
    elif user.changeUserEmail(emailTextField.get("1.0", 'end-1c')) != True:
	profileLabel.config(text='Invalid email',foreground="red")
    else:
	profileLabel.config(text='Saved',foreground="green")

def savePassword():
	global currentPasswordTextField
	global newPasswordTextField
	global confirmPasswordTextField
	global passwordLabel
	
	if confirmPasswordTextField.get("1.0", 'end-1c')!=newPasswordTextField.get("1.0", 'end-1c'):
		passwordLabel.config(text='Password not match',foreground="red")
	elif user.changeUserPassword(newPasswordTextField.get("1.0", 'end-1c'),currentPasswordTextField.get("1.0", 'end-1c')) != True:
		passwordLabel.config(text='Incorrect Password',foreground="red")
	
        else:
		passwordLabel.config(text='Password Changed',foreground="green")

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
	global dateTextField
	global timeTextField
	global time2TextField
	global var
	global reminderMsgLabel
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

		set1Button = Button(main, text="Set", command = setReminder1)
		set1Button.place(x=920, y=100, height=25, width=60)
		
		set2Button = Button(main, text="Set", command = setReminder2)
		set2Button.place(x=920, y=150, height=25, width=60)

		reminderMsgLabel = Label(main, text="1", font=("Times", 12))
		reminderMsgLabel.place(anchor=CENTER, x=800, y=200)

		historyLabel = Label(main, text="Search History", font=("Times", 12))
		historyLabel.place(x=550, y=220)

		updateHistoryList()
		historyClear = Button(main, text="Clear", command=clear)
		historyClear.place(anchor=CENTER, x=950, y=262, height=25, width=60)
		
		if not user.viewUserInformation():
			userWelcomeMsg = "Welcome"
		else:
			userWelcomeMsg = "Welcome " + str(user.viewUserInformation()[0][1])
		
		userWelcomeLabel = Label(main, text=userWelcomeMsg, font=("Helvetica", 12))
		userWelcomeLabel.place(x=10, y=2)
		
		editButton = Button(main, text="Edit Profile", bg='#cceeff', command=editProfileUI)
		editButton.place(x=10, y=25, height=20, width=100)
	
		changePasswordButton = Button(main, text="Change Password", bg='#cceeff', command=changePasswordUI)
		changePasswordButton.place(x=10, y=45, height=20, width=130)


def clear():
	user.deleteHisiotry()
	updateHistoryList()

def updateHistoryList():
	variable = StringVar(main)
	variable.set("one")  # default value
	global historyChosen
	global number2
	historyChosen = ttk.Combobox(main, textvariable="variable", values=user.viewUserHistory())
	historyChosen.bind("<<ComboboxSelected>>", callback)
	historyChosen.pack()
	historyChosen.place(x=620, y=250, height=25, width=280)


def callback(eventObject):
	locationTextField.delete("1.0", 'end-1c')
	locationTextField.insert('end-1c', historyChosen.get())
	global localoption
	localoption=user.getOption(historyChosen.get())

	search()

def editProfileUI():
	global firstnameTextField
	global lastnameTextField
	global birthdayTextField
	global addressTextField
        global profileLabel
	global emailTextField
	profile = Tk()
	profile.title('Profile')
	profile.geometry("400x300+200+130")

	firstnameLabel = Label(profile, text="First Name", font=("Helvetica", 12))
	firstnameLabel.place(x=60, y=30)
		
	firstnameTextField = Text(profile)
	firstnameTextField.place(x=150, y=30, height=25, width=200)
	if user.viewUserInformation(): firstnameTextField.insert(END,str(user.viewUserInformation()[0][1]))

	lastnameLabel = Label(profile, text="Last Name", font=("Helvetica", 12))
	lastnameLabel.place(x=60, y=72)
	
	lastnameTextField = Text(profile)
	lastnameTextField.place(x=150, y=72, height=25, width=200)
	if user.viewUserInformation(): lastnameTextField.insert(END, str(user.viewUserInformation()[0][2]))

	birthdayLabel = Label(profile, text="Birthday", font=("Helvetica", 12))
	birthdayLabel.place(x=60, y=114)
	
	birthdayTextField = Text(profile)
	birthdayTextField.place(x=150, y=114, height=25, width=200)
	if user.viewUserInformation(): birthdayTextField.insert(END,str(user.viewUserInformation()[0][3]))

	addressLabel = Label(profile, text="Address", font=("Helvetica", 12))
	addressLabel.place(x=60, y=156)
	
	addressTextField = Text(profile)
	addressTextField.place(x=150, y=156, height=25, width=200)
	if user.viewUserInformation(): addressTextField.insert(END,str(user.viewUserInformation()[0][4]))

	emailLabel = Label(profile, text="Email", font=("Helvetica", 12))
	emailLabel.place(x=60, y=198)
	
	emailTextField = Text(profile)
	emailTextField.place(x=150, y=198, height=25, width=200)
	emailTextField.insert(END,str(user.getUserEmail()[0][0]))
	

	saveButton = Button(profile, text="Save",command=saveProfile)
	saveButton.place(anchor=CENTER, x=200, y=270, height=25, width=80)

	profileLabel = Label(profile, text="", font=("Helvetica", 12))
    	profileLabel.place(anchor=CENTER, x=200, y=240)

	profile.mainloop()

def changePasswordUI():
	global currentPasswordTextField
	global newPasswordTextField
	global confirmPasswordTextField
	global passwordLabel
	
	changePassword = Tk()
	changePassword.title('Change Password')
	changePassword.geometry("400x230+200+130")

	currentPasswordLabel = Label(changePassword, text="Current Password", font=("Helvetica", 12))
	currentPasswordLabel.place(x=30, y=30)

	currentPasswordTextField = Text(changePassword)
	currentPasswordTextField.place(x=170, y=30, height=25, width=200)

	newPasswordLabel = Label(changePassword, text="New Password", font=("Helvetica", 12))
	newPasswordLabel.place(x=30, y=72)

	newPasswordTextField = Text(changePassword)
	newPasswordTextField.place(x=170, y=72, height=25, width=200)

	confirmPasswordLabel = Label(changePassword, text="Confirm Password", font=("Helvetica", 12))
	confirmPasswordLabel.place(x=30, y=114)

	confirmPasswordTextField = Text(changePassword)
	confirmPasswordTextField.place(x=170, y=114, height=25, width=200)

	passwordLabel = Label(changePassword, text="")
	passwordLabel.place(anchor=CENTER, x=200, y=155)

	SavePasswordButton = Button(changePassword, text="Save", command=savePassword)
	SavePasswordButton.place(anchor=CENTER, x=200, y=180, height=25, width=80)

	changePassword.mainloop()

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
	     sendSignUpEmail(emailTextFieldSignUp.get("1.0", 'end-1c'))
		

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
	global localoption
	cityName = locationTextField.get("1.0", 'end-1c')
	handleError = handleException(localoption, cityName)
	info = WeatherData(localoption, cityName)
	data = info.getWeatherInfo()
	if handleError.inputError() and type(data) ==list:
		currentTempLabel.config(text="Current Temperature: "+str(data[3])+" F")
		lowestTempLabel.config(text="Lowest Temperature: "+str(data[1])+" F")
		highestTempLabel.config(text="Highest Temperature: "+str(data[2])+" F")
		windSpeedLabel.config(text="Wind Speed: "+str(data[4])+" m/h")
		cloudPrecentageLabel.config(text="Humidity: "+str(data[6])+"%")
		cloundDescriptionLabel.config(text="Cloud Description: "+data[5])
		searchLabel.config(text="")
		user.saveHistory(localoption, cityName)
		updateHistoryList()
		searchWeather = True
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

address = [
    ("City Name      ", 1),
    ("Zip Code       ", 2),
    ("Geo Coordinates", 3),
]

def ShowChoice(text, v):
	global localoption
	localoption=v.get()

varaddress = IntVar()
varaddress.set(address[0][1])

locationcode=156
for txt, val in address:
	Radio = Radiobutton(main, text=txt, variable=varaddress, value=val,
						command=lambda t=txt, v=varaddress: ShowChoice(t, v)).place(anchor=CENTER, x=locationcode, y=195)
	locationcode+=150


t = threading.Thread(target=emailTimer)
t.start()

t2 = threading.Thread(target=emailCirculationTimer)
t2.start()

main.protocol("WM_DELETE_WINDOW",on_closing)




main.mainloop()










