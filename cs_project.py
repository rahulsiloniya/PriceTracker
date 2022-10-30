import requests
from bs4 import BeautifulSoup
import smtplib
import time

def conv(price):
    np = price.replace(',', '')
    nprv = float(np)
    return nprv
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('psiloniya@gmail.com', 'nrtpqqmaoaupttly')
    subject = 'Your share pricing is rising!'
    body = ('Your stocks ', title[k], 'has become profitable.',
            'You can sell them to earn a prfit of', prc[k]-bprc[k], 'on each stock.')
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'psiloniya@gmail.com',
        'rsiloniya@gmail.com',
        msg
        )
    server.quit()

title = ['Bajaj Finance (BAF)', 'HDFC (HDF)         ', 'Hero MotoCorp (HHM)', 'Asian Paints (API) ',
         'Axis Bank (UTI)    ']
URL = r'https://www.moneycontrol.com/markets/indian-indices/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

ids = ['ltp_BAF', 'ltp_HDF', 'ltp_HHM', 'ltp_API', 'ltp_UTI10']

prc = []
bprc = [4136.2, 2446.85, 2349.1, 1773.0, 743.25]

print('BUYING PRICE LIST', end = '\n')

for k in range(5):
    price = soup.find(id = ids[k]).get_text()
    nprc = conv(price)
    prc.append(nprc)
    print(title[k], end = '\t')
    print(bprc[k])
print('CURRENT MARKET PRICE OF OWNED SHARE IN THE PORTFOLIO')
def chk_price():
    for k in range(5):
        price = soup.find(id=ids[k]).get_text()
        nprc = conv(price)
        prc.append(nprc)
    for i in range(5):
        print(title[i], end = '\t')
        print(prc[i])
        if prc[i] > bprc[i]:
            send_mail()

while True:
    chk_price()
    time.sleep(60*60)
    
