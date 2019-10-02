# Image Classification Pipeline

## Directory Strcuture

### projects/`{project_name}`/
The name of project must be from pool of alpha-numeric characters and symbols (`'_'`, `'-'`). Folder contains config.py, dataset folder and model folder.  All data, config, logs, etc should be inside this folder only for this particular project.


### projects/{project name}/model
You must create this folder before starting training process. This folder will store all weights file, model files, tensorboard logs, class files, etc. 
This folder should be handle with care, all learning is stored inside this folder.


### projects/{project name}/dataset
The training data must be stored in a particular format in order to be fed into the network to train. We will be using ImageDataGenerator, available in keras to train our model on the available data. That way the process becomes much simpler in terms of code.
There must be a main dataset folder, inside that folder, there must be a test/train folders and inside that there must be folders for each class of data containing the corresponding images. The names of the folders must be the names of their respective classes.

### projects/{project name}/config.py
Python file which contains all model related config variables. 


## How to run
### For trianing
python main.py train `{project_name}` 

### To view tensorboar
tensorboard --logdir `projects/{project_name}/model/tblogs` 

## Dependencies
- Python3
- etc
