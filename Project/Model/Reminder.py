import smtplib

def sendReminder(email,msg):
	
	subject = "Reminder for WeatherChecker!!"
	messsage = 'Subject: {}\n\n{}'.format(subject, msg)

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("weatherchecker432@gmail.com", "weatherchecker")
	server.sendmail("weatherchecker432@gmail.com",email,messsage)
	server.quit()



