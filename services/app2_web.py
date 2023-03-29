from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

from apps import apps_system
from utils import abspath
from utils.logger_tools import get_general_logger
from configs.app2_config import HOST, PORT
from configs.environment import DEBUG

logger = get_general_logger(name='app2', path=abspath('logs'))


def main():
    app = apps_system.create_app()
    if DEBUG:
        app.run(debug=True, port=PORT)
    http_server = WSGIServer((HOST, PORT), app)
    logger.info('Connect_four Web Started.')
    logger.info(f'Host: {HOST} Port: {PORT} URL: http://{HOST}:{PORT}')
    http_server.serve_forever()


if __name__ == '__main__':
    main()
