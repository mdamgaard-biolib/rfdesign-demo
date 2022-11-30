import biolib
import os
import docker
req = os.environ.pop('REQUESTS_CA_BUNDLE', None)
docker.from_env(timeout=4000)
os.environ['REQUESTS_CA_BUNDLE'] = req
docker.info()