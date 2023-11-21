//simple express server
const express = require('express');
const app = express();
const port = 8080;
const fs = require('fs');

var names = []
var tokens = []
var logs = []

var date = new Date();
var timestamp = date.getUTCDate();
var name = timestamp + '.json';

// only run if file exists
if (fs.existsSync(name)) {
    var data = fs.readFileSync(name);
    var json = JSON.parse(data.toString());
    names = json;
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

app.get('/delete/:name/:usr', (req, res) => {
    //check if id is already in names
    if (checkPresence(req.params.name)) {
        //remove name from names
        for (var i = 0; i < names.length; i++) {
            if (names[i].title == req.params.name) {
                names.splice(i, 1);
            }
        }
        res.sendStatus(200);
        //timestamp
        var date = new Date()
        var timestamp = date.toISOString();
        logs.push(`${timestamp}: ${req.params.usr} removed ${req.params.name}`)
        console.log(logs)
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

function convertToTick(inp) {
    var tick = "✘"
    if (inp == 1|inp == "1") {
        tick =  "✓"
    }
    return tick;
}

app.get('/view', (req, res) => {
    //send names as a webpage in detail
    B = ""
    S = ""
    T = ""
    N = ""
    R = ""
    var page = "<h1>Names</h1><br><ul>"
    for (var i = 0; i < names.length; i++) {
            let tick = convertToTick(names[i].reg)
            if (names[i].service == "B") {
                B += `<li>${names[i].title} - ${tick}</li>`
            } if (names[i].service == "S") {
                S += `<li>${names[i].title} - ${tick}</li>`
            } if (names[i].service == "T") {
                T += `<li>${names[i].title} - ${tick}</li>`
            } if (names[i].service == "N") {
                N += `<li>${names[i].title} - ${tick}</li>`
            } if (names[i].service == "R") {
                R += `<li>${names[i].title} - ${tick}</li>`
            }
            
    }
    page += `<h2>Bradford</h2><ul>${B}</ul><h2>Scott</h2><ul>${S}</ul><h2>Training</h2><ul>${T}</ul><h2>Navy</h2><ul>${N}</ul><h2>RAF</h2><ul>${R}</ul>`
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
    } if (!(checkPresence(req.params.name))) {
        res.sendStatus(404)
    }
})

app.listen(port, () => console.log(`Example app listening on port ${80}!`));