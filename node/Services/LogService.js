'use strict';

//file manager
var fs = require('fs');

//Enviroment Selector
var Env_Data = require('../Enviroments/Development');
if(process.env.NODE_ENV.trim() == 'production'){ // production || debug
    Env_Data = require('../Enviroments/Production');
}

//Functions
exports.ReportAction = async function (msg) {
    if (Env_Data.Logs.Actions) {
        try {
            fs.appendFile("./Traceability/LogActions.txt", 'Log Reported - ' + new Date().toISOString() + '- Message:' + msg + '\n', function (err) {
                if (err) throw err;
                console.log('Log Reported to LogActions')
            });
        } catch (exc) {
            console.log('Log could not be reported, message found: ' + exc);
        }
    }
}

exports.ReportError = async function (msg) {
    if (Env_Data.Logs.Errors) {
        try {
            fs.appendFile("./Traceability/LogErrors.txt", 'Log Reported - ' + new Date().toISOString() + '- Message:' + msg + '\n', function (err) {
                if (err) throw err;
                console.log('Log Reported to LogErrors')
            });
        } catch (exc) {
            console.log('Log could not be reported, message found: ' + exc);
        }
    }
}
