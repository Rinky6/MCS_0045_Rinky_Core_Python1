import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('rink29182@gmail.com','Rinky@2222')
server.sendmail( 'rink29182@gmail.com','rinkykum4444@gmail.com','Mail sent from python' )
print(" mail send ")


