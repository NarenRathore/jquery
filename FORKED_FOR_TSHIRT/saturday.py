import smtplib
con=smtplib.SMTP("smtp.gmail.com",587)
con.starttls()
con.login("guptapikky19@gmail.com","2802@pikky")
con.sendmail("guptapikky19@gmail.com","guptapikky@gmail.com","Hello prayag")
con.quit()

