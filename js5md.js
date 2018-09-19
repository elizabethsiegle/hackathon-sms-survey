var express = require('express');
var bodyParser = require('body-parser');
var dotenv = require('dotenv');
dotenv.load();
var fromNum = `+18649368416`;
// var app = express();
// app.use(bodyParser.urlencoded({extended:false}));

// app.post('/message', (req, res) => {
// 	console.log(req.body);
// 	res.send("<Response><Message>Welcome to GHC</Message></Response>");
// });

// var listener = app.listen(1337, () => {
// 	console.log("Express server listening on port 1337");
// });

const client = require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

const filter = {
	to: fromNum // switch this out with your "from" number
}

client.messages.each(filter, (message) => client.calls.create({
	url:'https://desolate-shelf-95000.herokuapp.com/redirect', // switch this for the mp3 of your choice
	to: message.from,
	from:fromNum // again, switch out for your "from" number
}).then(call => console.log(call.sid))
.done()
);
// var call = client.calls.create({
//     url:'https://desolate-shelf-95000.herokuapp.com/redirect', // switch this for the mp3 of your choice
//     to: '+16507878004',
//     from:fromNum // again, switch out for your "from" number
// }).then(call => console.log(call.sid));
