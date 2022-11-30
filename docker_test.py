import biolib
import os
import docker
my_env = os.environ.copy()
if my_env.get('DOCKER_CERT_PATH'):
    my_env.pop('REQUESTS_CA_BUNDLE', None)
docker.from_env(timeout=4000, environment=my_env)
