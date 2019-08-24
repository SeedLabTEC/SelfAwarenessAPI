//Express
var express    = require('express');        // call express
var app        = express();                 // define our app using express
//#####

//Body Parser
var bodyParser = require('body-parser');
app.use(bodyParser({limit: '50mb'})); // extiende el limite de MB del cuerpo de la consulta
app.use(bodyParser.urlencoded({ extended: true })); // habilita el url encoded
app.use(bodyParser.json({limit: '50mb'})); // extiende el limite de transferencia de objetos JSON
//#####

//ENV Configuration
require('dotenv').config();

envData = require('./Enviroments/Development');
if(process.env.NODE_ENV.trim() == 'production'){ // production || debug
    envData = require('./Enviroments/Production');
}
console.log("Enviroment: " + process.env.NODE_ENV);
//#####

// set our port
var port =  envData.HttpPort;
if(envData.isSecure){
    port = envData.HttpsPort;
}
else{
    port = envData.HttpPort;
}
//#####

//Cors enable
var cors = require('cors');
app.use(cors({origin: envData.cors})); // habilita los Cors globalmente
//#####


//Public static folder
app.use(express.static('public')); // habilita un puerto de lectura de archivos estaticos 'public'
//######

//Home Route... API DOcumentation
app.get('/', function(req, res) {
    res.sendFile('index.html', {
        root: './Public/Views'
    });
});
//#####

//Provided Routes
var testRoute = require('./Routes/TestRoute');
testRoute(app);
//#####


// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Server started at port: ' + port);
//#####