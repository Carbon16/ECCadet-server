//simple express server
const express = require('express');
const app = express();
const port = 8080;

var names = []

function checkPresence(name) {
    //check names for the presence of name
    for (var i = 0; i < names.length; i++) {
        if (names[i].title == name) {
            return true;
        }
    }
    return false;
}

app.get('/delete/:name', (req, res) => {
    //check if id is already in names
    if (checkPresence(req.params.name)) {
        //remove name from names
        for (var i = 0; i < names.length; i++) {
            if (names[i].title == req.params.name) {
                names.splice(i, 1);
            }
        }
        res.sendStatus(200);
    };
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