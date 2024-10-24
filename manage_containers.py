import docker
import time

client = docker.from_env()

def list_containers():
    containers = client.containers.list()
    for container in containers:
        print(f'Container {container.name} is {container.status}')

def restart_flask_if_unhealthy():
    flask_container = client.containers.get('flask_app')
    health_status = flask_container.attrs['State']['Health']['Status']
    if health_status != 'healthy':
        print('Flask app is unhealthy, restarting...')
        flask_container.restart()

if __name__ == "__main__":
    while True:
        list_containers()
        restart_flask_if_unhealthy()
        time.sleep(30)  # Check every 30 seconds
