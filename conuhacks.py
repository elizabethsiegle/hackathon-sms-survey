from twilio.twiml.messaging_response import MessagingResponse 
from flask import Flask, request 

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def sms():
	msg = request.form['Body'].lower() #gets incoming message
	if msg == "hi": #based on incoming message, send different message
		resp = MessagingResponse().message("hi")
	else:
		resp = MessagingResponse().message("lol")
	#return message: if you just want to send any message, return this
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
