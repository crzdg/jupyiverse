# 🪐🌚 jupyiverse

This repository contains my personally used configuration to handle my JupyterLab instances.
It uses JupyterHub with a [dockerspawner](https://www.google.com/search?client=firefox-b-d&q=dockerspawner) to handle the JupyterLab instances via Docker.

For JupyterLab a set of configurations for extensions can be found.
Additionally, some Dockerfile including JupyterLab and a preset of dependencies. 

## 🚀 Get started

- Check out and understand [jupyerhub_config.py](jupyterhub/jupyterhub_config.py)
    - Adjust the volume mappings.
    - Adjust the device mappings.
    - Adjust the allowed images.
- Create a directory for the users' work and home directory (`user-data` per default)
    - Handling of host and docker userids is not setup. JupyterLab containers do start with userid `1000`.
    - **You have to handle / setup permissions for folders by yourself.**
- Build the repos docker images.
    - `make build-"fileextension"`, i.e. `make build-cuda118-2204`
- Start the JupyterHub instance
    - `docker compose up`, daemon `docker compose up -d`

## 🪐🏗️ JupyterHub

- Handling work and home directory for users
- Simple dummyauthenticator (only use in personal networks!)
- Using dockerspawner and images to spawn instance

## 🪐🧪 JupyerLab

### ➕ Extensions

- [jupytext](https://github.com/mwouts/jupytext)
- [jupyterlab-lsp](https://github.com/jupyter-lsp/jupyterlab-lsp)
- [jupyterlab-code-formatter](https://github.com/ryantam626/jupyterlab_code_formatter)
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets)

### 🎨 Themes
- [jupyterlab-gruvbox-dark](https://github.com/IBArbitrary/jupyterlab_gruvbox_dark)
- [jupyterlab-theme-solarized-dark](https://github.com/AllanChain/jupyterlab-theme-solarized-dark)
- [theme-darcula](https://github.com/telamonian/theme-darcula)

#### ⚔️ Limitations

- jupyterlab-lsp does currently not support formatting.
- jupyterlab-lsp does currently not support the configuration of python-lsp-ruff
- jupyterlab-code-formatter does currently not support the loading of config files
- jupyterlab has problems with default viewers, there should be a more stable version with 4.0
- jupyter-code-formatter does not support on save formatting in Jupytext Notebook, might be mitigated with 4.0

### 💬 Language Servers

- [python-lsp-server](https://github.com/python-lsp/python-lsp-server)
- [pylsp-rope](https://github.com/python-rope/pylsp-rope)

## 🐍 Python Environment

#### 📦 Packages

- tensorflow
- pytorch
- matplotlib
- scikit-learn
- opencv via python3-opencv

#### 🚧 Development tools

- black
- isort
- pylint


## 💻 Development

Dependencies for development can be found in (requirements)[requirements/]

Add packages to JupyterHub and JupyterLab to there corresponding `*.in` file.

```bash
make pip-compile-jupyterhub
make pip-compile-jupyterlab
```
Rebuild the images.
