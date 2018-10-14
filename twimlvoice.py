from twilio.twiml.voice_response import Client, Dial, Number, VoiceResponse

response = VoiceResponse()
dial = Dial(caller_id='+12402198265')
dial.number('650-787-8004')
dial.client('joey')
dial.client('charlie')
response.append(dial)

print(response)