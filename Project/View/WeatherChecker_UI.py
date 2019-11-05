from Tkinter import *

login = None


def loginUI():
    global login
    global usernameTextField
    login = Tk()
    login.title('Login')
    login.geometry("400x200+200+130")

    usernameLabel = Label(login, text="User Name", font=("Helvetica", 12))
    usernameLabel.place(x=60, y=30)

    usernameTextField = Text(login)
    usernameTextField.place(x=150, y=30, height=25, width=200)

    passwordLabel = Label(login, text="Password", font=("Helvetica", 12))
    passwordLabel.place(x=60, y=72)

    passwordTextField = Text(login)
    passwordTextField.place(x=150, y=70, height=25, width=200)

    loginTo = Button(login, text="Login", command=userFunction)
    loginTo.place(anchor=CENTER, x=200, y=150, height=25, width=80)

    login.mainloop()

def checkLogin():
    check = True;
    return check;


def userFunction():
    global usernameTextField
    loginCheck = checkLogin()
    if loginCheck == False: print "no"
    elif loginCheck == True:
        print usernameTextField.get("1.0", END)
        print usernameTextField.get("1.0", END)

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
    signUp = Tk()
    signUp.title('Sign Up')
    signUp.geometry("400x230+200+130")

    usernameLabel = Label(signUp, text="User Name", font=("Helvetica", 12))
    usernameLabel.place(x=60, y=30)

    usernameTextField = Text(signUp)
    usernameTextField.place(x=150, y=30, height=25, width=200)

    passwordLabel = Label(signUp, text="Password", font=("Helvetica", 12))
    passwordLabel.place(x=60, y=72)

    passwordTextField = Text(signUp)
    passwordTextField.place(x=150, y=70, height=25, width=200)

    emailLabel = Label(signUp, text="Email", font=("Helvetica", 12))
    emailLabel.place(x=60, y=114)

    emailTextField = Text(signUp)
    emailTextField.place(x=150, y=110, height=25, width=200)

    signupButton = Button(signUp, text="Sign Up", command=signUp.destroy)
    signupButton.place(anchor=CENTER, x=200, y=180, height=25, width=80)


    signUp.mainloop()

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







