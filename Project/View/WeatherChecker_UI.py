from Tkinter import *

userlogin = False
login = None

def loginUI():
	global login
	login = Tk() 
	login.title('Login')
	login.geometry("400x200+200+130") 

	usernameLabel = Label(login,text="User Name",font=("Helvetica", 12))
	usernameLabel.place(x=60,y=30)

	usernameTextField = Text(login)
	usernameTextField.place(x=150,y=30, height=25, width=200)

	passwordLabel = Label(login,text="Password",font=("Helvetica", 12))
	passwordLabel.place(x=60,y=72)

	passwordTextField = Text(login)
	passwordTextField.place(x=150,y=70, height=25, width=200)

	loginButton = Button(login,text="Login", command=checkLogin)
	loginButton.place(anchor=CENTER, x=200,y=150, height=25, width=80)

	login.mainloop() 
	
def checkLogin():
	global login
	login.destroy()
	main.geometry("800x400+100+100") 

def signUpUI():
	signUp = Tk() 
	signUp.title('Sign Up')
	signUp.geometry("400x230+200+130") 

	usernameLabel = Label(signUp,text="User Name",font=("Helvetica", 12))
	usernameLabel.place(x=60,y=30)

	usernameTextField = Text(signUp)
	usernameTextField.place(x=150,y=30, height=25, width=200)

	passwordLabel = Label(signUp,text="Password",font=("Helvetica", 12))
	passwordLabel.place(x=60,y=72)

	passwordTextField = Text(signUp)
	passwordTextField.place(x=150,y=70, height=25, width=200)

	emailLabel = Label(signUp,text="Email",font=("Helvetica", 12))
	emailLabel.place(x=60,y=114)

	emailTextField = Text(signUp)
	emailTextField.place(x=150,y=110, height=25, width=200)

	signupButton = Button(signUp,text="Sign Up", command=signUp.destroy)
	signupButton.place(anchor=CENTER, x=200,y=180, height=25, width=80)	

	signUp.mainloop() 
	


main = Tk() 
main.title('Weather Checker')
main.geometry("600x400+100+100") 	

appNameLabel = Label(main,text="Weather Checker",font=("Helvetica", 20))
appNameLabel.place(anchor=CENTER,x=300, y=85)

locationLabel = Label(main,text="Location",font=("Helvetica", 12))
locationLabel.place(x=120,y=152)

locationTextField = Text(main)
locationTextField.place(x=190,y=150, height=25, width=200)

searchButton = Button(main,text="Search")
searchButton.place(x=410,y=150, height=25, width=80)

loginButton = Button(main,text="Login", bg='#cceeff', command=loginUI)
loginButton.place(x=380,y=10, height=25, width=80)

orLabel = Label(main,text="or",font=("Helvetica", 12))
orLabel.place(x=470, y=10)

signupButton = Button(main,text="Sign Up",bg='#cceeff', command=signUpUI)
signupButton.place(x=500,y=10, height=25, width=80)

currentTempLabel = Label(main,text="Current Temperature: X F",font=("Helvetica", 12))
currentTempLabel.place(x=70,y=220)

lowestTempLabel = Label(main,text="Lowest Temperature: X F",font=("Helvetica", 12))
lowestTempLabel.place(x=70,y=255)

highestTempLabel = Label(main,text="Highest Temperature: X F",font=("Helvetica", 12))
highestTempLabel.place(x=70,y=290)

windSpeedLabel = Label(main,text="Wind Speed: X m/h",font=("Helvetica", 12))
windSpeedLabel.place(x=330,y=220)

cloudPrecentageLabel = Label(main,text="Cloud Percentage: X%",font=("Helvetica", 12))
cloudPrecentageLabel.place(x=330,y=255)

cloundDescriptionLabel = Label(main,text="Cloud Description: X",font=("Helvetica", 12))
cloundDescriptionLabel.place(x=330,y=290)



main.mainloop() 





	

