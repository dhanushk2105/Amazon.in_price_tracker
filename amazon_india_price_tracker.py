import requests as r
from bs4 import BeautifulSoup as bs
import smtplib

#any product in amazon.in URL

URL = 'https://www.amazon.in/Generic-Home-Gym-Combo-20Kg/dp/B016OJ4ATW?ref_=Oct_BSellerC_3404719031_0&pf_rd_p=f0c02333-256b-5349-807c-bbbef21b0422&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=3404719031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=0FKRTSR62RHYAG33XT2T&pf_rd_r=0FKRTSR62RHYAG33XT2T&pf_rd_p=f0c02333-256b-5349-807c-bbbef21b0422'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = r.get(URL, headers = headers)
    soup = bs(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[2:])

    print(title.strip())
    print(converted_price)

    if(converted_price < 1000):
        print("Sending email ....... ")
        send_mail()

    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() #for encryption.
    server.ehlo()

    server.login('youremail@gmail.com','google app password gen') #put your email id and do 2 step varification, and genrate password for gmail, enter the password.

    subject = 'Price fell down!'
    body = 'Check the amazon link --> ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'youremail@gmail.com', #your emil id
        'target_email', #target's email id
        msg
        )
    print('Hey the mail has been sent')

    server.quit()

check_price()
