const fs = require('fs');
var path = require('path');

const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);

const { Server } = require("socket.io");

const io = new Server(server);

app.use(express.static(path.join(__dirname,'public')));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

server.listen(3000, () => {
  console.log('listening on *:3000');
});

function updatePerception()
{

    fs.readFile('../SensorData/data.csv', 'utf8', (e,data) => 
    {
      d = data.split(/\r?\n/);
      sensorData = d[d.length - 1].split(',');
      console.log( sensorData );
      io.sockets.emit('perceptionData', 
      {
        Temp : sensorData[0], //Valor de sensores
        Peso : sensorData[1],  //Valor sensores
        Luz  : sensorData[2],  //Valor sensores
        Hum  : sensorData[3],  //Valor sensores
      });
    });

    setTimeout(updatePerception, 1000);
}

updatePerception();