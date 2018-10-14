from twilio.twiml.messaging_response import MessagingResponse 
from flask import Flask, request 

app = Flask(__name__)
@app.route('/mhacks', methods=['GET', 'POST'])

def sms():
	res = MessagingResponse()
	res.message("mhacks rules! @lizziepika, lsiegle@twilio.com")
	return str(res)
if __name__ == "__main__":
	app.run(debug=True)