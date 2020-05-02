```python
import paho.mqtt.client as mqtt
```

```python
HOSTNAME = socket.gethostname()
IPADDRESS = socket.gethostbyname(HOSTNAME)
MQTT_HOST = IPADDRESS
MQTT_PORT = 3001
MQTT_KEEPALIVE_INTERVAL = 60
```

```python
client = mqtt.Client()
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
```

```python
client.publish("class", json.dumps({"class_names": class_names}))
client.publish("speedometer", json.dumps({"speed": speed}))
```

```python
client.disconnect()
```

```python
import sys
```

```python
sys.stdout.buffer.write(frame)  
sys.stdout.flush()
```

## Running the App
```bash
python app.py | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 1280x720 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
```