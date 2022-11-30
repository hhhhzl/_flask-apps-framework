from utils import abspath
from utils.logger_tools import get_general_logger
from utils.manager_tools import ServiceManager
import fire

logger = get_general_logger(name='manager', path=abspath('logs'))

class ConnectFourWeb(ServiceManager):

    name = 'connect_four_web'
    file = 'connect_four_game_web.py'
    dir_path = abspath('services')

SERVICES_MAP = {
    'connect_four': ConnectFourWeb
}

def run_service(service_name, action):
    """
    action: start | stop | run | enable | disable | status
    """
    if service_name not in SERVICES_MAP:
        print(f'No such service: {service_name}')
        return

    service = SERVICES_MAP[service_name]
    service(action=action)

def main():
    fire.Fire(run_service)

if __name__ == '__main__':
    main()

