const https = require('https');
const fs = require('fs');

const options = {
    key: fs.readFileSync('../z01/privkeyA.pem'),
    cert: fs.readFileSync('../z01/certA.crt')
};

const port = 443;

https.createServer(options, (req, res) => {
    res.writeHead(200);
    res.end('hello world\n');
  }).listen(port);

console.log(`server running on port ${port}`)
