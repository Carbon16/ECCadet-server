//simple express server
const express = require('express');
const app = express();
const port = 8080;
app.get('/', (req, res) => res.send('Hello World!'));

var names = []

//listen for http get requests
app.get('/api/:id', (req, res) => {
    names.push({"title": req.params.id, "id": req.params.id, "registered": 0})
    res.send(names);
});

app.get('/', (req, res) => {
    res.sendStatus(200);
});

app.listen(port, () => console.log(`Example app listening on port ${80}!`));