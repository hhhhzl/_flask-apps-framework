from utils import abspath
from utils.logger_tools import get_general_logger
from utils.manager_tools import ServiceManager
import fire

logger = get_general_logger(name='manager', path=abspath('logs'))


class App1Web(ServiceManager):
    name = 'app1_web'
    file = 'app1_web.py'
    dir_path = abspath('services')

class App2Web(ServiceManager):
    name = 'app1_web'
    file = 'app1_web.py'
    dir_path = abspath('services')


SERVICES_MAP = {
    'app1': App1Web,
    'app2': App2Web
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
