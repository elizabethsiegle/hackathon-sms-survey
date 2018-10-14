from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request 
app = Flask(__name__)
@app.route('/mhacks2', methods=['GET', 'POST'])
def sms():
    msg = request.values.get("Body").lower().strip() #gets incoming message
    res = MessagingResponse()
    if msg == "play":
        res.message("Q1: What did the first SMS message sent contain?")
    elif msg == "merry christmas":
        res.message("You go Glen Coco! Q2: What is the most popular password?")
    elif msg == "123456":
        res.message("Q3: Noice. How often did the most common password appear in Pwned Passwords? (no commas)")
    elif msg == "22390492":
        res.message("Good job! Q4: The co-creator and exec. producer of what show is coming to Twilio Signal?")
    elif msg == "westworld":
        res.message("Yass. Q5: What is Lizzie's Twilio Signal Conf promo code?")
    elif msg == "lsiegle10" or msg == "lsiegle20":
        res.message("right! Q6: How many active Twilio customer accounts were there at the end of June 2018? (no commas)")
    elif msg == "57350":
        res.message("smart. Q7: In 2013, how many people did Twilio reach globally? (no commas)")
    elif msg == "350000000":
        res.message("you right. Q8: In what country is Lizzie speaking at a conference in 2 weeks?")
    elif msg == "dominican republic":
        res.message("yesss. Q9: What is the most commonly-used language by developers using Twilio?")
    elif msg == "c#" or msg == "dotnet" or msg == ".net":
        res.message("correct! task 1: Dance with the Firebase people for 2 seconds and take a picture while doing so. Text back \'goog\'.")
    elif msg == 'goog':
        res.message("come to the Twilio booth, show Lizzie, and tell her your favorite ice cream flavor")
    else:
        print(msg)
        res.message("nice try, try again!")
    # count = 0
    # if msg == "play" or msg == " play" or msg == "play ":
    # 	res.message("Q1, what skateboarder is speaking at Twilio's conference this week?")
    # elif msg == "tony hawk" or msg == " tony hawk" or msg == "tony hawk ":
    #     res.message("yasss. Q2: What year was the first SMS sent?")
    # elif msg == "1992":
    # 	res.message("noice! Q3: who was the singer of the song played during the Twilio opening ceremony demo?")
    # elif msg == "rick astley":
    # 	res.message("you right! Q4: What is the ranking of Michigan's football opponent tonight?") #based on incoming message, send different message
    # elif msg == "15":
    #     res.message("Q5: Where did Twilio's CEO go to college? hint: provide it in 2 letters")
    # elif msg == "um":
    #     res.message("True! Q6 fill in blank: A ___ got its name by being the second division of an hour by 2")
    # elif msg == "second" or msg == "second " or msg == " second" or msg == " second ":
    #     res.message("You right! Now go take a selfie with a Facebook, Wayfair, or MongoDB sponsor and text \'owl\' back.")
    # elif msg == "owl":
    #     res.message("Now take a selfie with a Twilio sticker OR the Twilio booth and share it on some form of social media and @twilio. Then show both selfies to Lizzie @ twilio booth rn")
    # else:
    #     print(msg)
    #     res.message("try again!")
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)