import docker
client = docker.from_env()
print(client.info(timeout=4000))