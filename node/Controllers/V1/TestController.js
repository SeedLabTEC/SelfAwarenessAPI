'use strict';

//Enviroment Selector
var envData = require('../../Enviroments/Development');
if (process.env.NODE_ENV.trim() == 'production') { // production || debug
    envData = require('../../Enviroments/Production');
}

//LogService
var logger = require('../../Services/LogService');

//Functions
exports.testFunc = async function (req, res) { //Endpoint Function, can only handle 1 session.
    //set Cors
    res.header("Access-Control-Allow-Origin", envData.Cors);
    //set Headers
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With", "Content-Type, Accept");

    //Always surround with try/Catch
    try{
        logger.ReportAction("ActionDone");
        res.send('Some data');
    }catch(err){
        logger.ReportError(err);
        res.json({
            "errorInternalCode": envData.Errors.GenericCatchException,
            "Message": err
        });
    }
};