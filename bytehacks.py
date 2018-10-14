
# from twilio.rest import Client
# import os

# client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

# #for num in client.messages.list(to='+12402198265'):
# call = client.calls.create(
#     body = 'take your pill at this time',
#     to = 'your-num', #num.from_,
#     from_ = '+12402198265'
# )
# print(call.sid)

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)
@app.route('/mhacks', methods=['GET', 'POST'])
def sms():
    inb_message = request.values.get('Body').lower()
    res = MessagingResponse()
    if inb_message == "hi":
        res.message("hi back")
    else:
        res.message("other msg")
    return str(res)
if __name__ == "__main__":
    app.run(debug=True)

