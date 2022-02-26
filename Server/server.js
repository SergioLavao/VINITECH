var path = require('path')

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

function updatePerception(){

    io.sockets.emit('perceptionData', 
      { 
        Temp : Math.random() + 10, //Valor de sensores
        Peso : Math.random() + 7,  //Valor sensores
        Luz  : Math.random() + 5,  //Valor sensores
        Hum  : Math.random() + 3,  //Valor sensores        
      });

    setTimeout(updatePerception, 1000);
}

updatePerception();