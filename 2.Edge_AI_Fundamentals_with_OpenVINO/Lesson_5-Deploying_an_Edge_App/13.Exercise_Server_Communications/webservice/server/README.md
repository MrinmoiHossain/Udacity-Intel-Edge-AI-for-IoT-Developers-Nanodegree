# vehicle-edge-app

## Launching the server
Tested on Node versions 4.2.6 and 8.5.

Get node.js and NPM up and running then...

Install the Node.js dependencies (restify uuid4 mosca):
~~~~
npm install
~~~~

Start the server:
~~~~
cd node-server
node ./server.js
~~~~

## MQTT
Mosca MQTT broker is automatically started on port 1883.  This can be changed in the configuration file.
For testing or debugging the MQTT broker, if necessary, you can use:
 * [mosquitto-clients](https://mosquitto.org/download/)
 * [mqtt-spy](http://kamilfb.github.io/mqtt-spy/)

