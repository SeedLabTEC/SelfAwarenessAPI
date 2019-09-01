'use strict'; // To run in strict mode

module.exports = function (app) {

    //Calling the Controller	
    var testController = require('../Controllers/' + process.env.VERSION_API + '/TestController');

    //Routing 
    app.route('/' + process.env.VERSION_API + '/test') 
        .get(testController.testFunc);

};