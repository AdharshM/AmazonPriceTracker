import requests
import smtplib
import time 
from bs4 import BeautifulSoup

def checkprice():
	#URL of the product, here I chose Ukelele
	URL = 'https://www.amazon.in/Juarez-JRZ21UK-Hawaiian-Rosewood-Fingerboard/dp/B071JM85N8/ref=sr_1_2?dchild=1&keywords=ukelele&qid=1600889930&sr=8-2'
	#headers for browser details
	headers = {
	"User-Agent" : "specify: just check my user agent in google"
	}
	pg = requests.get(URL, headers = headers)
	webpg = BeautifulSoup(pg.content, 'html.parser')			#parse the webpage by html parser
	title = webpg.find(id = "productTitle").getText()			#Retrieves Title
	price = webpg.find(id = "priceblock_ourprice").getText()	#Retrieves Price
	pr = ""
	for i in range(2, len(price)):
		if price[i] != ',':
			pr += price[i]										#Price in float
	conv_price = float(pr)										
	if conv_price <= 2100:										#Sends mail to user if condition price is satisfied	
		send_mail()
	else:
		print("NO PRICE CHANGE")								#NO PRICE CHANGE 
		return 0


def send_mail():
	mailer = smtplib.SMPT('smtp.gmail.com', 587);		#Connecting to GMAIL SMTP server
	mailer.ehlo()										
	mailer.starttls()									#TLS
	mailer.ehlo()

	mailer.login('email_id', 'password')

	subject = "Price of the Item fell down"

	body = "Check it now on https://www.amazon.in/Juarez-JRZ21UK-Hawaiian-Rosewood-Fingerboard/dp/B071JM85N8/ref=sr_1_2?dchild=1&keywords=ukelele&qid=1600889930&sr=8-2"
	message = f"Subject : {subject}\n\n\n{body}"

	server.send_mail(
		'sender_email_address',
		'recipient_mail_address',
		message
		)
	print("MAIL SENT")


while 1 < 2:
	checkprice()
	time.sleep(86400)									#Repeats Everyday
