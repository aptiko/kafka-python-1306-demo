# Demo for reproducing a kafka-python bug

This is a setup that reproduces
https://github.com/dpkp/kafka-python/issues/1306.

How to prepare:

1. Make sure you have Docker installed.

2. Create and activate a Python 3 virtualenv.

3. `pip install -r requirements.txt`. This will install docker-compose>=1.13 (maybe older versions will work, maybe not).

4. `docker-compose build`. This may take several minutes and may download several hundreds of MB of stuff (but only the first time you run it).

Now let's go to reproduce the bug:

1. Make sure you have activated the virtualenv.

2. `docker-compose up -d`

3. In another window, `docker-compose logs -f kafkaclient`. Wait for 5 seconds or until you see a little output that indicates that kafkaclient connected to kafka.

4. `docker-compose stop kafkaserver`

At this point, after the kafkaserver goes down, one of two things will happen; either the kafkaclient will behave normally, or it will go into an endless loop.

**If it behaves normally**, the log will show a repeated couple of warning messages about a heartbeat problem, again and again and again. If you start the server again with `docker-compose start kafkaserver`, after about 10 seconds these messages will stop repeating themselves as the client will automatically reconnect. Go back to step (4) and retry, and eventually you'll get the endless loop.

**If it goes into the endless loop**, you will get an endless stream of some warning messages and a traceback, which will not stop when you restart the server.

When you're done, `docker-compose down` will stop the docker containers.
