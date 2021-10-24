import requests
from bs4 import BeautifulSoup
import smtplib
import time
url='https://www.tunisianet.com.tn/pc-portable-tunisie/49161-pc-portable-apple-macbook-pro-16-touch-bar-gris-sideral.html'


def get_product():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())

    n =soup.find(attrs={"property":"og:title"})

    #name = n["content"]
    #print(name)

    p =soup.find(attrs={"property":"product:price:amount"})
    price = float (p["content"])
    print(price)


    if (price < 7500):
        send_mail()

def send_mail():
    #connection to gmail    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('devpython801@gmail.com','devpython112')
    #mail-form
    subject= 'IMPORTANT:Price fell down '
    body = 'Check  https://www.tunisianet.com.tn/pc-portable-tunisie/49161-pc-portable-apple-macbook-pro-16-touch-bar-gris-sideral.html '
    msg = f"subject: {subject}\n\n{body}"
    #sending-mail
    server.sendmail('devpython801@gmail.com','contact.mehdicharfi@gmail.com',msg)
    print("sendsendsendse,nd")
    server.quit()


#while(True):

#    get_product()
#    time.sleep(3600)




