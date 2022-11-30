import biolib
import os
import docker
my_env = os.environ.copy()
my_env.pop('REQUESTS_CA_BUNDLE', None)
docker.from_env(timeout=4000, environment=my_env)