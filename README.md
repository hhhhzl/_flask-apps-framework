# flask-apps-framework
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

This repository contains the source framework for a multiple apps based on flask with databases setted up (postgre + redis) as default. The repo can also can serve as mircoservice for one of the applications. With sreen and fire tools, the framework is easy to deploy and start.

The framework is the example of 2 apps but feel free to add more apps, and change database whatever you want. Have fun! 

```
apps // apps register, main set up 
blueprints  // flask bp & response logic 
    |- app1 
        | - __init__.py // Views of app1
        | - model.py // Models of app1
        | - controller.py // Controller of app1
    | - app2
        | - __init__.py // Views of app2
        | - model.py // Models of app2
        | - controller.py // Controller of app2
    | ..add your app
configs // config files for evironment, database (postgre + redis)
services // main services
tests // test tools
tools // tool functions
utils // util tool, (utilize tools)
manager.py main process
```

## What included?
- MVC ( model, view, controller )
- database ( postgre, redis )
- 2 apps ( app1, app2 )
- log
- screen
- util ( database utils )

## Start
1. need a server, with database set up

2. build a new conda environment ( optional )
```
conda create --name flask-apps python==3.9
```

3. change the env path to local conda env in config.environment.py file
```
ENV_PATH = '%define yours%'
```

4. install requirements
```
pip setup.py develop
```

5. config files
```
- app1_config.py
- app2_config.py
- environment.py
- postgre_config.py
- redis_config.py
- .....add your configs
```

6. start/ stop/ restart web server
```
manager app1 start
manager app2 start

manager app1 stop
manager app2 stop

manager app1 restart
manager app2 restart
```

To see the status of the deployment
```
screen -ls
```

Links
-----

-   Documentation: https://flask.palletsprojects.com/
