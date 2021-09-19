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
    if msg != "play" and question_on == 0:
        res.message("Text \'play\' to play⚽🎾⛹️‍♀️🎱")
    if msg == "play" and question_on == 0:
        res.message("Q1: What did the first SMS message sent say?📱")
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
    elif msg == "merry christmas" and question_on == 1:
        res.message("🎄You go Glen Coco🎅! Q2: What is the most popular password?👩‍💻👨‍💻")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif msg == "123456" and question_on == 2:
        res.message(
            "Noice. Q3: The Twilio founders wrote out the plan for Twilio on the back of what in 2007?✏🖊✐")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif msg == "pizza box" and question_on == 3:
        res.message("🍕correct🍕! Q4: What was the first word said on the first phone call?☎📱📞")
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
    elif (msg == 'mister' and question_on == 4) or (msg == 'mr' and question_on == 4) or (msg == 'mr.' and question_on == 4):
        question_on +=1
        session['question_on'] = question_on
        print(question_on)
        res.message("you right.👨🕺 Q5: how many nations have ruled over texas?🌐🌎🌍")
    elif msg == "6" and question_on == 5 or msg == "six" and question_on == 5 or msg == 6 and question_on == 5:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("noice. Q6: What is the average number of tornadoes in texas per year?🌪🌀") 
    elif (msg == "132" and question_on == 6) or (msg == 132 and question_on == 6):
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("yep. Q7: how much did the first item sold on eBay sell for?💻")
    elif ("14.83" in msg and question_on == 7):
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("yupp. Q8: what year was the first email sent?📧📫")
    elif (msg == "1971" and question_on == 8) or (msg == 1971 and question_on == 8) :
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("correct. How many countries does Twilio have offices in?")
    elif msg == "17" and question_on == 9:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("yusss. Who wrote the 1st book📖 ever ordered by a customer on Amazon? It was a programming book📖! Send 1st + last name pls")
    elif msg == "douglas hofstadter" and question_on == 10:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("yeet. task 1: take a pic🤳 w/ a Twilio sticker or Twilio shirt 👕 and POST it to social media (Twitter, IG, or LinkedIn)📲 w/ @twilio, @pinnacleusorg, @twiliodevs, and #twilio. Text back \'twlo\'.")
    elif msg == "twlo" and question_on == 11:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message("make or find a developer meme and tweet-reply📲 it at @twiliodevs here: twitter.com/TwilioDevs/status/1438893015439921157. Text back \'meme\'")
    elif msg == "meme" and question_on == 12:
        question_on += 1
        session['question_on'] = question_on
        print(question_on)
        res.message(
            "come to the twilio booth, show Lizzie the picture and meme, and receive your boba (limited quantity)")
    elif question_on != 0:
        res.message("Nice try, try again!")
        print(question_on)
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)
