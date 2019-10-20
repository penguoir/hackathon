var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(8080);

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/../public/client.html');
});

io.on('connection', function (socket) {
  socket.emit('question', { title: 'With a radius of <> and mass of <>, would a planet of size <> and radius <> be feasable?' });
});