//simple express server
const express = require('express');
const app = express();
const port = 8080;

var names = []
var tokens = []
var logs = []

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
    };
});

app.get('/ax/:fname', (req, res) => {
    //check if id is already in names
    // forward any json files in the directory that match the filename in req.params.fname
    res.sendFile(req.params.fname, { root: __dirname });
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
app.get('/add/:id/:usr', (req, res) => {
    //check if id is already in names
    if (checkPresence(req.params.id)) {
        res.sendStatus(409);
        return;
    } if(!(checkPresence(req.params.id))) {
        names.push({"title": req.params.id, "id": req.params.id, "reg": 0, "authorised": req.params.usr})
        res.sendStatus(201);
        //save names to json file named the date only
        var date = new Date()
        var timestamp = date.getDate()
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