//simple express server
const express = require('express');
const app = express();
const { Expo } = require('expo-server-sdk');
const port = 8080;
const fs = require('fs');
const { send } = require('process');

var names = []
var tokens = []
var logs = []
var merits = []

fetch('https://lgsk.tech/auth/Skingley, L/Carbon1769')

if (fs.existsSync("TOKENS.json")) {
    var data = fs.readFileSync("TOKENS.json");
    var json = JSON.parse(data.toString());
    tokens = json;
}

if (fs.existsSync("merits.json")) {
    var data = fs.readFileSync("merits.json");
    var json = JSON.parse(data.toString());
    merits = json;
}


//push some data to tokens
tokens.push({
    name: "Leo",
    token: "ExponentPushToken[FfdQW8JeDRD_z5sL5bZH3f]"
})

tokens.push(
    {
        name: "Izzy",
        token: "ExponentPushToken[ueguW8KZd8YA21_cSi4b-t]"
    }
)

var date = new Date();
var timestamp = date.getUTCDate();
var name = timestamp + '.json';

// Notifs

let expo = new Expo()

function newNotif(to, body) {
    let messages = [];
    // Check that all your push tokens appear to be valid Expo push tokens
    if (!Expo.isExpoPushToken(to)) {
        console.error(`Push token ${to} is not a valid Expo push token`);
    }
    // Construct a message (see https://docs.expo.io/push-notifications/sending-notifications/)
    messages.push({
        to: to,
        sound: 'default',
        body: body,
    })

    let chunks = expo.chunkPushNotifications(messages);

    let tickets = [];
    (async () => {
    // Send the chunks to the Expo push notification service. There are
    // different strategies you could use. A simple one is to send one chunk at a
    // time, which nicely spreads the load out over time:
    for (let chunk of chunks) {
        try {
        let ticketChunk = await expo.sendPushNotificationsAsync(chunk);
        console.log(ticketChunk);
        tickets.push(...ticketChunk);
        // NOTE: If a ticket contains an error code in ticket.details.error, you
        // must handle it appropriately. The error codes are listed in the Expo
        // documentation:
        // https://docs.expo.io/push-notifications/sending-notifications/#individual-errors
        } catch (error) {
            console.error(error);
        }
    }
    })();
}

function notifyRem(victim, auth, oAuth) {
    //if oauth in tokens.name
    for (var i = 0; i < tokens.length; i++) {
        if (tokens[i].name == oAuth) {
            newNotif(tokens[i].token, `Your cadet, ${victim}, was removed by ${auth}`)
        }
    }
}

var prev = [{"title":"PATEL, Rohan","id":"PATEL, Rohan","reg":1,"authorised":"Kousetta "},{"title":"CLARK, Sophie","id":"CLARK, Sophie","reg":1,"authorised":"Kousetta "},{"title":"LUNG, Sean","id":"LUNG, Sean","reg":1,"authorised":"Kousetta "},{"title":"MACGREGOR","id":"MACGREGOR","reg":1,"authorised":"Kousetta "},{"title":"LUTTIG, Zach","id":"LUTTIG, Zach","reg":2,"authorised":"Kousetta "},{"title":"Jack Wingate","id":"Jack Wingate","reg":1,"authorised":"Flt Sgt Crockett"},{"title":"Harry Hamlyn","id":"Harry Hamlyn","reg":1,"authorised":"Flt Sgt Crockett"},{"title":"Zoe Moir","id":"Zoe Moir","reg":2,"authorised":"Leo"},{"title":"Ronnie Hickling","id":"Ronnie Hickling","reg":2,"authorised":"Leo"},{"title":"Zain Thaver","id":"Zain Thaver","reg":1,"authorised":"Flt Sgt Crockett"},{"title":"Imogen Martin-Webb","id":"Imogen Martin-Webb","reg":1,"authorised":"Leo"},{"title":"SIRAH, Jeevan","id":"SIRAH, Jeevan","reg":2,"authorised":"Kousetta "},{"title":"BUIJS, Catharina","id":"BUIJS, Catharina","reg":1,"authorised":"Izzy"}]

// only run if file exists

if (fs.existsSync(name)) {
    var data = fs.readFileSync(name);
    var json = JSON.parse(data.toString());
    names = json;
}



if (fs.existsSync("log.json")) {
    var data = fs.readFileSync("log.json");
    var json = JSON.parse(data.toString());
    logs = json;
}

function checkPresence(name) {
    //check names for the presence of name
    for (var i = 0; i < names.length; i++) {
        if (names[i].title == name) {
            return true;
        }
    }
    return false;
}

app.get('/log', (req, res) => {
    res.send(logs)
});

app.get('/merit/:name/:usr/:service', (req, res) => {
    merits.push({"name": req.params.name, "authorised": req.params.usr, "service": req.params.service})
    var name = 'merits.json';
    var fs = require('fs');
    fs.writeFile(name, JSON.stringify(merits), function (err) {
        if (err) throw err;
        console.log('Saved!');
    });
    res.sendStatus(201);
});

app.get('/merits', (req, res) => {
    res.send(merits)
});


app.get('/delete/:name/:usr', (req, res) => {
    //check if id is already in names
    if (checkPresence(req.params.name)) {
        //remove name from names
        for (var i = 0; i < names.length; i++) {
            if (names[i].title == req.params.name) {
                let oAuth = names[i].authorised
                let victi = names[i].title
                names.splice(i, 1);
                notifyRem(victi, req.params.usr, oAuth)
            }
        }
        res.sendStatus(200);
        //timestamp
        var date = new Date()
        var timestamp = date.toISOString();
        logs.push(`${timestamp}: ${req.params.usr} removed ${req.params.name}`)
        console.log(logs)
        fs.writeFile("log.json", JSON.stringify(logs), function (err) {
            if (err) throw err;
            console.log('Saved!');
        });
        var date = new Date();
        var timestamp = date.getUTCDate();
        var name = timestamp + '.json';
        var fs = require('fs');
        fs.writeFile(name, JSON.stringify(names), function (err) {
            if (err) throw err;
            console.log('Saved!');
        });
    };
});

app.get('/ax/:fname', (req, res) => {
    //check if id is already in names
    // forward any json files in the directory that match the filename in req.params.fname
    res.sendFile(req.params.fname, { root: __dirname });
});

app.get('/purge/:fname/Leo', (req, res) => {
    fs.unlink(req.params.fname, (err) => {
        if (err) throw err;
        console.log(req.params.fname + ' was deleted');
    });
    res.sendStatus(200);
});

app.get('/summon', (req, res) => {
    //send a notification to every unique token in tokens
    for (var i = 0; i < tokens.length; i++) {
        newNotif(tokens[i].token, "Please dispatch all sanctions parade cadets ASAP")
    }
    res.sendStatus(200);
});

app.get('/victim/:name', (req, res) => {
//display detailed information about the name in a html format
function convertToTick(inp) {
    var tick = "✘"
    if (inp == 1|inp == "1") {
        tick =  "✓"
    }
    return tick;
}
var page = `
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #333;
        }
        div {
            margin-top: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            margin-right: 10px;
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>${req.params.name}</h1>
    <div>
`;

var mode = "https://eccadet.azurewebsites.net";
for (var i = 0; i < names.length; i++) {
    if (names[i].title == req.params.name) {
        page += `<li>Registered: ${names[i].reg}</li>`;
        page += `<li>Authorized by: ${names[i].authorised}</li>`;
        page += `<br>`;
        page += `<a href="${mode}/delete/${names[i].title}/Web-Console">Delete</a>`;
        page += `<a href="${mode}/register/${names[i].title}/1">Register</a>`;
        page += `<a href="${mode}/register/${names[i].title}/Web-Console">De-register</a>`;
        // display pervious dates that this name is included in by checking the date.json files, eg 21.json
        page += `<br>`;
        page += `<h2>Sanctions this month</h2>`;
        for (var j = 1; j < 31; j++) {
            if (fs.existsSync(j+'.json')) {
                var data = fs.readFileSync(j+'.json');
                var json = JSON.parse(data.toString());
                for (var k = 0; k < json.length; k++) {
                    if (json[k].title == names[i].title) {
                        page += `<li>${j}: ${convertToTick(json[k].reg)}</li>`;
                    }
                }
            }
        }
    }
}

page += `
    </div>
</body>
</html>
`;

res.send(page);
});


app.get('/view', (req, res) => {

    function convertToTick(inp) {
        var tick = "✘"
        if (inp == 1|inp == "1") {
            tick =  "✓"
        }
        return tick;
    }
    
    function preCheck(nom) {
        //if the name is included in by checking the date.json files, eg 21.json, return a ⚠️ and the number of times
        var count = 0;
        for (var j = 1; j < 31; j++) {
            if (fs.existsSync(j+'.json')) {
                var data = fs.readFileSync(j+'.json');
                var json = JSON.parse(data.toString());
                for (var k = 0; k < json.length; k++) {
                    if (json[k].title == nom) {
                        count++;
                    }
                }
            }
        }
        if (count-1 > 0) {
            return `⚠️ Strike ${count}`
        } else {
            return ""
        }        

    }
    //send names as a webpage in detail
    B = ""
    S = ""
    T = ""
    N = ""
    R = ""
    L = ""
    var page = `<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #333;
        }
        div {
            margin-top: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            margin-right: 10px;
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            color: #0056b3;
        }
    </style>
</head><h1>Names</h1><br><ul>`
    var mode = "https://eccadet.azurewebsites.net"
    for (var i = 0; i < names.length; i++) {
            let pre = preCheck(names[i].title)
            let tick = convertToTick(names[i].reg)
            if (names[i].service == "B") {
                B += `<li><a href="${mode}/victim/${names[i].title}">${names[i].title} - ${tick} ${pre}</a></li>`
            } if (names[i].service == "S") {
                S += `<li><a href="${mode}/victim/${names[i].title}">${names[i].title} - ${tick} ${pre}</a></li>`
            } if (names[i].service == "T") {
                T += `<li><a href="${mode}/victim/${names[i].title}">${names[i].title} - ${tick} ${pre}</a></li>`
            } if (names[i].service == "N") {
                N += `<li><a href="${mode}/victim/${names[i].title}">${names[i].title} - ${tick} ${pre}</a></li>`
            } if (names[i].service == "R") {
                R += `<li><a href="${mode}/victim/${names[i].title}">${names[i].title} - ${tick} ${pre}</a></li>`
            } if (names[i].service == "L") {
                L += `<li><a href="${mode}/victim/${names[i].title}">${names[i].title} - ${tick} ${pre}</a></li>`
            }
            
    }
    page += `<h2>Bradford</h2><ul>${B}</ul><h2>Scott</h2><ul>${S}</ul><h2>Training</h2><ul>${T}</ul><h2>Navy</h2><ul>${N}</ul><h2>RAF</h2><ul>${R}</ul><h2>Leadership</h2><ul>${L}</ul>`
    res.send(page)
});

app.get('/filez', (req, res) => {
    //return all json file names inside directory
    var filez = []
    const fs = require('fs');
    fs.readdirSync(__dirname).forEach(file => {
        if (file.endsWith('.json')) {
            filez.push(file)
        }
    });
    res.send(filez)
});

app.get('/tk', (req, res) => {
    //return all tokens
    res.send(tokens)
});

app.get('/tokes/:token/:name', (req, res) => {
    //check if id is already in tokens
    for (var i = 0; i < tokens.length; i++) {
        if (tokens[i].token == req.params.token) {
            res.sendStatus(409);
            return;
        } if(!(tokens[i].token == req.params.token)) {
            tokens.push({"token": req.params.token, "name": req.params.name})
            var name = 'TOKENS.json';
            var fs = require('fs');
            fs.writeFile(name, JSON.stringify(tokens), function (err) {
                if (err) throw err;
                console.log('Saved!');
            });
            res.sendStatus(201)
            if (req.params.name == undefined) {
                // ref is the last four letters of the token
                var ref = req.params.token.slice(-4)
                sendNotif(req.params.token, "Your username is unknow, please contact LGS with the reference " + ref)
            }
        }
}});

//listen for http get requests
app.get('/add/:id/:usr/:serv', (req, res) => {
    //check if id is already in names
    if (checkPresence(req.params.id)) {
        res.sendStatus(409);
        return;
    } if(!(checkPresence(req.params.id))) {
        if (req.params.serv == undefined) {
            req.params.serv = "Client needs update!"
        }
        names.push({"title": req.params.id, "id": req.params.id, "reg": 0, "authorised": req.params.usr, "service": req.params.serv})
        res.sendStatus(201);
        //save names to json file named the date only
        var date = new Date();
        var timestamp = date.getUTCDate();
        var name = timestamp + '.json';
        var fs = require('fs');
        fs.writeFile(name, JSON.stringify(names), function (err) {
            if (err) throw err;
            console.log('Saved!');
        });
        //timestamp
        var date = new Date()
        var timestamp = date.toISOString();
        logs.push(`${timestamp}: ${req.params.usr} added ${req.params.id}`)
        console.log(logs)
    };
});

app.get('/', (req, res) => {
    res.sendStatus(200);
});

app.get('/dump', (req, res) => {
    res.send(names);
});

app.get('/register/:name/:set', (req, res) => {
    if (checkPresence(req.params.name)) {
        for (var i = 0; i < names.length; i++) {
            if (names[i].id == req.params.name) {
                names[i].reg = parseInt(req.params.set);
            }
        }
        res.sendStatus(200);
        var date = new Date();
        var timestamp = date.getUTCDate();
        var name = timestamp + '.json';
        var fs = require('fs');
        fs.writeFile(name, JSON.stringify(names), function (err) {
            if (err) throw err;
            console.log('Saved!');
        });
    } if (!(checkPresence(req.params.name))) {
        res.sendStatus(404)
    }
})

app.get('/version', (req, res) => {
    res.send("3.2.2")
    console.log("ver")
});

app.listen(port, () => console.log(`Example app listening on port ${80}!`));