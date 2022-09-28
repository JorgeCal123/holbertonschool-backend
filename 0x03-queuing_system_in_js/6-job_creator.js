var kue = require('kue'), queue = kue.createQueue();

const obj = { phoneNumber: "1234", message: "new message" }

var job = queue.create('push_notification_code', obj).save(function(err){
   if( !err ) 
   console.log( `Notification job created: ${job.id}` );
});

job.on('complete', function(result){
    console.log('Notification job completed', result);
    
  }).on('failed', function(errorMessage){
    console.log('Notification job failedd');
  
  });


  /**var kue = require('kue'), queue = kue.createQueue();

const obj = { phoneNumber: "1234", message: "new message" }

var job = queue.create('push_notification_code', obj).save();

job.on('enqueue', function() {
    console.log(`Notification job created: ${job.id}`)

  }).on('complete', function(result){
    console.log('Notification job completed', result);
    
  }).on('failed', function(errorMessage){
    console.log('Notification job failedd');
  
  }); */