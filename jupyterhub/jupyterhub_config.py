import os

import docker

c = get_config()

# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = "dummy"

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = "0.0.0.0"

# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = "jupyterhub"

c.JupyterHub.allow_named_servers = True
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.name_template = "{prefix}-{username}-{servername}"
c.DockerSpawner.allowed_images = [
    "jupyter-cuda118-2204-py311:latest",
    "jupyter-cuda118-2204:latest",
    "jupyter-cuda118-2004-py310:latest",
    "jupyter-cuda112-2004-py310:latest",
    "jupyter-2204:latest",
    "jupyter-2004:latest",
]

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = "jupyterhub"
# c.DockerSpawner.pull_policy = "always"

homedir_inside_container = "/home/jovyan"
repository_directory_on_host = "/home/rb/git/jupyiverse"
user_data_directory_on_host = f"{repository_directory_on_host}/user-data"

c.DockerSpawner.notebook_dir = f"{homedir_inside_container}/work"
c.DockerSpawner.volumes = {
    f"{repository_directory_on_host}/jupyterlab/jupyter_lab_config.py": f"{homedir_inside_container}/.jupyter/jupyter_lab_config.py",
    f"{user_data_directory_on_host}/jupyiverse-user-{{username}}/home": f"{homedir_inside_container}",
    f"{user_data_directory_on_host}/jupyiverse-user-{{username}}/work": f"{homedir_inside_container}/work",
    "/home/rb/git": f"{homedir_inside_container}/git",
}
c.DockerSpawner.read_only_volumes = {"/mnt/st8tb": "/mnt/st8tb"}

# delete containers when the stop
c.DockerSpawner.remove = True
c.DockerSpawner.debug = False
c.DockerSpawner.extra_host_config = {
    "device_requests": [
        docker.types.DeviceRequest(
            count=-1,
            capabilities=[["gpu"]],
        ),
    ],
}
c.DockerSpawner.cmd = ["jupyterhub-singleuser"]
