pip-compile-jupyterlab:
	@hatch run pip-compile-jupyterlab:update

pip-compile-jupyterhub:
	@hatch run pip-compile-jupyterhub:update

pip-compile-dev:
	@hatch run pip-compile-dev:update

pip-compile-mains:
	@hatch run pip-compile-main:update

update: pip-compile-dev pip-compile-jupyterhub pip-compile-jupyterlab pip-compile-mains

build-%:
	docker build . -t jupyter-$* -f jupyterlab/docker/Dockerfile.$*

build-hub:
	docker compose build
