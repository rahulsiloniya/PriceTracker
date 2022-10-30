import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('psiloniya@gmail.com', 'nrtpqqmaoaupttly')
subject = 'File'
hand = open(r'C:\Users\Rahul Siloniya\Downloads\CS PROJECT.pdf', 'r')
body = (hand)
msg = f"Subject:{subject}\n\n{body}"
server.sendmail(
    'psiloniya@gmail.com',
    'rsiloniya@gmail.com',
    msg
    )
server.quit()
