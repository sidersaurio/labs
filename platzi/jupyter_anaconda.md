## Toolbox 🧰
---
Let's refresh here some basic but helpful commands for the upcoming exercises and projects

### Anaconda 🐍
```sh
# Basic
conda info
conda env list
conda create --name env_name lib_name lib_name=version
conda activate env_name
conda deactivate
conda list
conda list lib_name
conda update lib_name
conda install lib_name=version
conda create --name new_env --copy --clone old_env
conda remove lib_name
conda env remove --name env_name

# Advanced
conda config --add channels conda-forge
conda install --channel conda-forge lib_name
conda list --revision
conda install --revision number
conda env export --from-history --file environment.yml
conda env create --file environment.yml

# Mamba
conda install --channel conda-forge mamba
mamba --help
mamba env create --file environment.yml
```
### Project Basic Structure 📑
```sh
project_x
    - data
    - models
    - notebooks
    - envs
        - external.yml
        - model.yml
        - comunication.yml
```
### Cookiecutter 🍪
```sh
cookiecutter https://github.com/sidersaurio/cookiecutter_template 
cookiecutter https://github.com/sidersaurio/cookiecutter_template --checkout folder_name
cookiecutter .
```
### OS, Pathlib, PyFilesystem2 📖
#### OS
```py
import os
CURRENT_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_DIR, os.pardir, "data", "raw")
os.path.exists(DATA_DIR)
os.path.isdir(DATA_DIR)
[os.path.join(DATA_DIR, item) for item in os.listdir(DATA_DIR)]
os.mkdir(os.path.join(DATA_DIR, "os"))
```
#### Pathlib
```py
import pathlib
CURRENT_DIR = pathlib.Path().resolve()
DATA_DIR = CURRENT_DIR.parent.joinpath("data", "raw")
DATA_DIR.is_dir()
DATA_DIR.exists()
list(DATA_DIR.glob("*"))
list(DATA_DIR.glob(".git*"))
DATA_DIR.joinpath("pathlib").mkdir()
```

#### PyFilesystem2
```py
import fs
CURRENT_DIR = fs.open_fs(".")
CURRENT_DIR.exists(".")
CURRENT_DIR.exists("..") # Error! cannot look outside, head = actual route!
DATA_DIR = fs.open_fs("../data/raw/")
DATA_DIR.listdir(".")
for path in DATA_DIR.walk.files():
    print(path)
    with DATA_DIR.open(path) as data_file:
        print(data_file.readlines())
DATA_DIRmakedir("external_fs", recreate = True)
```

#### Relative paths
```sh
# Pyprojroot: start point and routes
import pyprojroot # Works with Pathlib!
pyprojroot.here("data").joinpath("raw")

# Pyhere: start point and routes
import pyhere # Works with Pathlib!
pyhere.here()
pyhere.here().resolve()
pyhere.here().resolve() / "data" / "raw"

# Creating shortcuts
def make_dir_function(dir_name):
    def dir_function(*args):
        return pyprojroot.here().joinpath(dir_name, *args)
    return dir_function
data_dir = make_dir_function("data")
notebooks_dir = make_dir_function("notebooks")
data_dir("raw", "pathlib", ".gitkeep").exists()
```