import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('achuthk99@gmail.com','123698745achuth')
msg=" hi "
s.sendmail('achuthk99@gmail.com","akashitha.17cs@gmail.com',)
s.quit()




