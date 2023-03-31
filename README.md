# flask-apps-framework
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

This repository contains the source framework for a multiple apps based on flask with databases setted up (postgre + redis) as default. The repo can also can serve as mircoserver for one of the applications. With sreen and fire tools, the framework is easy to deploy and start.

The framework is the example of 2 apps but feel free to add more apps, and change database whatever you want. Have fun! 

```
blueprints - flask bp & response logic
configs - config files
services - main services
tests - test tools
tools - tool functions
utils - util tool, (utilize tools)
manager.py main process
```

MVC - model, view, controller

## Start
1. need a server, with database setted up

2. build a new conda eniroment(optional)
```
conda create --name flask-apps python==3.9
```

3. change the env path to local conda env in config.environment.py file
```
ENV_PATH = ''
```

4. install requirements
```
pip setup.py develop
```

5. config files
```
config
```

6. start/ stop/ restart web server
```
manager app1 start
manager app1 stop
manager app1 restart
```

view：
```
screen -ls
```

Links
-----

-   Documentation: https://flask.palletsprojects.com/
