from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

from apps import connect_four_system
from utils import abspath
from utils.logger_tools import get_general_logger
from configs.connect_four_web_config import HOST, PORT

logger = get_general_logger(name='Connect_four', path=abspath('logs'))


def main():
    app = connect_four_system.create_app()
    # app.run(debug=True, port=PORT)
    http_server = WSGIServer((HOST, PORT), app)
    logger.info('Connect_four Web Started.')
    logger.info(f'Host: {HOST} Port: {PORT} URL: http://{HOST}:{PORT}')
    http_server.serve_forever()


if __name__ == '__main__':
    main()
