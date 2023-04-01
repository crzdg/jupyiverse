pip-compile-jupyterlab:
	 pip-compile -o jupyterlab/requirements/jupyterlab.txt --annotation-style=line --resolver=backtracking jupyterlab/requirements/jupyterlab.in

pip-compile-jupyterhub:
	 pip-compile -o jupyterhub/requirements/jupyterhub.txt --annotation-style=line --resolver=backtracking jupyterhub/requirements/jupyterhub.in

pip-compile-dev:
	pip-compile -o requirements/dev.txt --annotation-style=line --resolver=backtracking requirements/dev.in

build-%:
	docker build . -t jupyter-$* -f jupyterlab/docker/cuda/Dockerfile.$*

build-hub:
	docker compose build
