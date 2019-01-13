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
        res.message("correct! Q4: What was the first word said on the first phone call (no abbreviations?") #task 1: take a picture with a Twilio sticker or Twilio shirt and upload it to social media (Twitter, Instagram) with @twilio, @sb_hacks, and #twilio #makingwaves. Text back \'twlo\'.")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif msg == 'mister' and question_on == 4:
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
        res.message("you right. Q5: the creators of what tv show spoke at twilio's conference last october?")
    elif msg == "westworld" and question_on == 5:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("noice. Q6: what ucsb sport has a tortilla toss tradition?") 
    elif msg == "soccer" and question_on == 6:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("yep. Q7: what type of dog was on stage with a speaker at the last Twilio conference?")
    elif msg == "corgi" and question_on == 7:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("yupp. Q8: what MLH hackathon ran a SMS-scavenger hunt boba contest in October 2018? Hint: it's a big hackathon and it's cold.")
    elif msg == "mhacks" and question_on == 8:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("correct. take a selfie with either Diane, Erin, Chandler, Esther, or Jennifer of the organizing team. text back \'makewaves\'")
    elif msg == "makewaves" and question_on == 9:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("take a picture with a Twilio shirt or sticker and post it to social media with @twilio and #twilio, #makingwaves text back \'twlo\'")
    elif msg == "twlo" and question_on == 10:
        res.message(
            "come to the bench outside, show Lizzie the pictures, and receive your boba (limited quantity)")
    else:
        res.message("Nice try, try again!")
        print(question_on)
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)
