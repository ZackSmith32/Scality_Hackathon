const Transform = require('stream').Transform;
const ProducerStream = require('../kafka-node/lib/producerStream');
const ConsumerGroupStream = require('../kafka-node/lib/consumerGroupStream');
const resultProducer = new ProducerStream();

const consumerOptions = {
  kafkaHost: '127.0.0.1:9092',
  groupId: 'ExampleTestGroup',
  sessionTimeout: 15000,
  protocol: ['roundrobin'],
  asyncPush: false,
  id: 'consumer1',
  fromOffset: 'latest'
};
console.log('right before function')
const consumerGroup = new ConsumerGroupStream(consumerOptions, 'test3');

var count = 0;
const messageTransform = new Transform({
  objectMode: true,
  decodeStrings: true,
  transform (message, encoding, callback) {
    count += 1;
    // console.log(`Received message ${count} : ${message.value}`);
    console.log(message.value)
    callback(null, {
      topic: 'RebalanceTopic',
      messages: `You have been (${message.value}) made an example of`
    });
  }
});

$(function () {
	console.log('doc ready function')
	consumerGroup.pipe(messageTransform).pipe(resultProducer);
})


var drawFunc = function(data) {

	// window.onload = function () {
		// initial values of dataPoints
		var dps = []
		for(var inx in data){
			dps.push({label: inx, y: data[inx]})
		}
		
		 var questionTitle = "Question???  -- answers: 42";
		
		
		//this should be turned into a init graph function
		var chart = new CanvasJS.Chart("chartContainer",{
			theme: "theme3",
			title:{ 
				// text: "Question currently being asked."
			},
			axisY: {				
				title: "Poll results"
			},					
			legend:{
				verticalAlign: "top",
				horizontalAlign: "centre",
				fontSize: 16

			},
			data : [{
				type: "column",
				//showInLegend: true,
				//legendMarkerType: "none",
				//legendText: questionTitle,
				//indexLabel: "{y}",
				dataPoints: dps
			}]
		});

		// renders initial chart
		chart.render();
		
		var updateInterval = 10;
		//this will be called eachtime rapid responds
		var updateChart = function () {
			//take in json object, and parse into label array
			//then  render
			chart.render();
		};
		//update chart after we've heard back from rapid.
		// setInterval( function(){ updateChart() }, updateInterval );
	// }

}
