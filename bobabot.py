from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request 
app = Flask(__name__)
@app.route('/mhacks2', methods=['GET', 'POST'])
def sms():
    msg = request.values.get("Body").lower().strip() #gets incoming message
    res = MessagingResponse()
    count = 0
    if msg == "play" and count == 0:
        res.message("Q1: What did the first SMS message sent contain?")
        count += 1
    if count == 1: 
        if msg == "merry christmas":
            count +=1
            res.message("You go Glen Coco! Q2: What is the most popular password?")
        else:
            res.message("Q1: What did the first SMS message sent contain?")
    elif count == 2:
        if msg == "123456":
            count +=1
            res.message("Q3: Noice. How often did the most common password appear in Pwned Passwords? (no commas)")
        else:
            res.message("Q2: What is the most popular password?")
    elif count == 3:
        if msg == "22390492":
            count +=1
            res.message("Good job! Q4: The co-creator and exec. producer of what show is coming to Twilio Signal?")
        else:
            res.message("Q3: How often did the most common password appear in Pwned Passwords? (no commas)")
    elif count == 4:
        if msg == "westworld":
            count +=1
            res.message("Yass. Q5: What is Lizzie's Twilio Signal Conf promo code?")
        else:
            res.message("Q4: The co-creator and exec. producer of what show is coming to Twilio Signal?")
    elif count == 5:
        if msg == "lsiegle10" or msg == "lsiegle20":
            count +=1
            res.message("right! Q6: How many active Twilio customer accounts were there at the end of June 2018? (no commas)")
        else:
            res.message("Q5: What is Lizzie's Twilio Signal Conf promo code?")
    elif count == 6:
        if msg == "57350":
            count +=1
            res.message("smart. Q7: In 2013, how many people did Twilio reach globally? (no commas)")
        else:
            res.message("Q6: How many active Twilio customer accounts were there at the end of June 2018? (no commas)")
    elif count == 7:
        if msg == "350000000":
            count +=1
            res.message("you right. Q8: In what country is Lizzie speaking at a conference in 2 weeks?")
        else:
            res.message("Q7: In 2013, how many people did Twilio reach globally? (no commas)")
    elif count == 8:
        if msg == "dominican republic":
            count +=1
            res.message("yess. task 1: Dance with the Firebase people for 2 seconds and take a picture while doing so. Text back \'goog\'.")
        else:
            res.message("Q8: In what country is Lizzie speaking at a conference in 2 weeks?")
    elif count == 9:
        if msg == 'goog':
            res.message("Come to the Twilio booth, show Lizzie, and tell her your favorite ice cream flavor")
        else:
            res.message("task 1: Dance with the Firebase people for 2 seconds and take a picture while doing so. Text back \'goog\'.")
    else:
        print(msg)
        res.message("nice try, try again!")

@app.route('/mhacks', methods=['GET', 'POST'])
    count = 0
    if msg == "play" and count == 0:
    	res.message("Q1: what skateboarder is speaking at Twilio's conference this week?")
        count += 1
    if count == 1:
        if msg == "tony hawk":
            count +=1
            res.message("yasss. Q2: What year was the first SMS sent?")
        else:
            res.message("Q1: what skateboarder is speaking at Twilio's conference this week?")
    if count == 2:
        if msg == "1992":
    	   res.message("noice! Q3: who was the singer of the song played during the Twilio opening ceremony demo?")
           count +=1
        else:
            res.message("Q2: What year was the first SMS sent?")
    elif count == 3:
        if msg == "rick astley":
            count+=1
            res.message("you right! Q4: What is the ranking of Michigan's football opponent tonight?") #based on incoming message, send different message
        else:
            res.message("Q3: who was the singer of the song played during the Twilio opening ceremony demo?")
    elif count == 4:
        if msg == "15":
            count +=1
            res.message("Q5: Where did Twilio's CEO go to college? hint: provide it in 2 letters")
        else:
            res.message("Q4: What is the ranking of Michigan's football opponent tonight?")
    elif count == 5:
        if msg == "um":
            count +=1
            res.message("True! Q6 fill in blank: A ___ got its name by being the second division of an hour by 2")
        else:
            res.message("Q5: Where did Twilio's CEO go to college? hint: provide it in 2 letters")
    elif count == 6:
        if msg == "second":
            count +=1
            res.message("You right! Now go take a selfie with a Facebook, Wayfair, or MongoDB sponsor and text \'owl\' back.")
        else:
            res.message("Q6 fill in blank: A ___ got its name by being the second division of an hour by 2")
    elif count == 7:
        if msg == "owl":
            res.message("Now take a selfie with a Twilio sticker OR the Twilio booth and share it on some form of social media and @twilio. Then show both selfies to Lizzie @ twilio booth rn")
        else:
            res.message("Now go take a selfie with a Facebook, Wayfair, or MongoDB sponsor and text \'owl\' back.")
    else:
        print(msg)
        res.message("try again!")
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)