import sys
import os
cwd = os.getcwd()
parent_dir = (os.path.abspath(os.path.join(cwd, os.pardir)))
sys.path.append(parent_dir)

from Tkinter import *
from Model.UserData import *
login = None


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
        loginCheck = verify(usernameTextFieldLogin.get("1.0", 'end-1c'),passwordTextFieldLogin.get("1.0", 'end-1c'))
   	if loginCheck == False: 
		loginLabel.config(text='Wrong Username/Password',foreground="red")
   	elif loginCheck == True: 
	
		global login
		login.destroy()
		main.geometry("1000x400+100+100")

		loginButton.place(anchor=CENTER, x=830, y=20, height=25, width=80)
		signupButton.place(anchor=CENTER, x=950, y=20, height=25, width=80)
		orLabel.place(x=880, y=10)
		logoutButton = Button(main, text="Logout", bg='#cceeff')
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

		setButton = Button(main, text="Set")
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

	signUpLabel = Label(signUp, text="1", font=("Helvetica", 12))
    	signUpLabel.place(anchor=CENTER, x=200, y=150)

	signupButton = Button(signUp, text="Sign Up", command=checkSignUp)
	signupButton.place(anchor=CENTER, x=200, y=180, height=25, width=80)


	signUp.mainloop()

def checkSignUp():
    	global usernameTextFieldSignUp
	global passwordTextFieldSignUp
	global emailTextFieldSignUp
	global signUpLabel
        signUpCheck = signUp(usernameTextFieldSignUp.get("1.0", 'end-1c'),passwordTextFieldSignUp.get("1.0", 'end-1c'))
   	if signUpCheck != True: 
	     signUpLabel.config(text=signUpCheck,foreground="red")
   	elif signUpCheck == True: 
	     signUpLabel.config(text="Congratulations!",foreground="green")
		

main = Tk()
main.title('Weather Checker')
main.geometry("600x400+100+100")

appNameLabel = Label(main, text="Weather Checker", font=("Helvetica", 20))
appNameLabel.place(anchor=CENTER, x=300, y=85)

locationLabel = Label(main, text="Location", font=("Helvetica", 12))
locationLabel.place(x=120, y=152)

locationTextField = Text(main)
locationTextField.place(x=190, y=150, height=25, width=200)

searchButton = Button(main, text="Search")
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

cloudPrecentageLabel = Label(main, text="Cloud Percentage: X%", font=("Helvetica", 12))
cloudPrecentageLabel.place(x=330, y=255)

cloundDescriptionLabel = Label(main, text="Cloud Description: X", font=("Helvetica", 12))
cloundDescriptionLabel.place(x=330, y=290)

main.mainloop()








