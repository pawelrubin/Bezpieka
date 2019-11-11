const https = require('https');
const fs = require('fs');
const express = require('express');

const options = {
    key: fs.readFileSync('./ssl/server_pk.pem'),
    cert: fs.readFileSync('./ssl/serwer_cert.crt')
};

const port = 443;

const app = express();
app.use(express.static('.'));

app.get('/hack', (req, res) => {
  console.log(req.query)
  return res.end(`HACKED ${JSON.stringify(req.query)}`)
})

https.createServer(options, app).listen(port);

console.log(`server running on port ${port}`)
