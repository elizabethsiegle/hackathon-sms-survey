from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, session
# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])

def sms():
    msg = request.values.get("Body").lower().strip() #gets incoming message
    res = MessagingResponse()
    question_on = session.get('question_on', 0)

    print(msg)
    if msg == "clear" or msg == "reset":
        question_on = 0
        session['question_on'] = question_on
    if msg == "play" and question_on == 0:
        res.message("Q1: What did the first SMS message sent say?")
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
    elif msg == "merry christmas" and question_on == 1:
        res.message("You go Glen Coco! Q2: What is the most popular password?")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif msg == "123456" and question_on == 2:
        res.message(
            "Noice. Q3: How often did the most common password appear in Pwned Passwords? (no commas)")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif msg == "22390492" and question_on == 3:
        res.message("correct! task 1: Dance with the Firebase people for 2 seconds and take a picture while doing so. Text back \'goog\'.")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif msg == 'goog':
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
        res.message("come to the Twilio booth, show Lizzie, and tell her your favorite ice cream flavor")
    else:
        res.message("Nice try, try again!")
        print(question_on)
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)
