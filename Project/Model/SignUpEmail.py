import smtplib


def sendSignUpEmail(email):
	
	subject = "Thank You For Signing Up!"
	msg = "Sign Up Completed!"
	messsage = 'Subject: {}\n\n{}'.format(subject, msg)

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("weatherchecker432@gmail.com", "weatherchecker")
	server.sendmail("weatherchecker432@gmail.com",email,messsage)
	server.quit()
	

