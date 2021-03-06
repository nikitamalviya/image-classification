# Image Classification Pipeline

## Requirements :
`pip3 install -r requirements.txt`

## Introduction to Modules :

```
├── projects                          <- Directory which holds all the projects
|   |                   
|   └── xyz-project                   <- An image classification project 
|         |
|         ├── dataset                 <- Dataset of classified images
|         |    |
|         |    ├── train              <- Contains train images 
|         |    ├── test               <- Contains testing images
|         |    ├── valiation          <- Contains validation images
|         |    └── may be csv/json    <- A file to extract dataset from it
|         |
|         ├── model
|         |    |
|         |    ├── saved_model        <- Contains saved models
|         |    ├── tblogs             <- Contains tensorboards
|         |    ├── weights            <- Contains saved weights
|         |    └── classes.npy        <- A file created having number of classes information
|         |
|         ├── main.py                 <- triggers training, testing and prediction
|         ├── config.py               <- configurations of project & model parameters
|         |                              ~ ** must for every project **
|         ├── prepare_dataset.py      <- reads `csv/json` files to convert it into train & test dataset
|         ├── preprocessing.py        <- preprocesses the data, triggers before training/testing/inference
|         ├── model.py                <- various models for training, returns compiled model to train.py
|         ├── train.py                <- fit the selected model
|         ├── test.py                 <- test the trained model
|         ├── predict.py              <- make predictions on explicitly provided inputs
|         ├── validations.py          <- valdiate requirements before training the model
|         └── utils.py                <- contains common utilities & functions which are in common use 
└──
```

## projects : projects/`{project_name}`/
- This is the home directory for all the image classification projects.
- This is dedicated directory for a project
- The name of the project must be from pool of alpha-numeric characters and symbols (`'_'`, `'-'`).

## dataset directory : projects/`{project name}`/dataset
- contains dataset in following sub-directories :
    - train :  contains training dataset  ----> `projects/{project name}/dataset/test`   
    - test : contains testing dataset  ----> `projects/{project name}/dataset/train`
- there must be sub-directories for each class of data containing the corresponding images. The names of the sub-directories must be the names of their respective classes
- we will be using ImageDataGenerator, available in keras to train our model on the available data, this way the process becomes much simpler in terms of code.  

#### model directory : projects/`{project name}`/model
- contains saved models, weights and tensorboard logs in following sub-directories :
    - saved models : contain saved models  ----> `projects/{project name}/model/saved models`    
    - weights : contain weight files  ----> `projects/{project name}/model/weights`
    - tblogs : contain tblogs  ----> `projects/{project name}/model/tblogs`
- these directories must be created before starting training process
- all the data, config, logs, etc should be inside this folder only for this particular project
- this whole directory should be handle with care, all learning is stored inside this folder

#### predict directory : projects/`{project name}`/predict
- contains images for prediction purpose in the following sub-directories :
    - input : contains input images  ---->  `projects/{project name}/predict/input`                
    - output : - contains output images generated by prediction phase code   ----> `projects/{project name}/predict/output`


## Project Execution Command :

#### For Training : 
- `python main.py train {project_name}`                    (Initial model training)
- `python main.py train {project_name} resume`             (Resume last training model)
- `python main.py train {project_name} example_model.h5`   (Resume training of explicitly called model) 

~ All these commands perform model training

#### For Testing : 
- `python main.py test {project_name}`
~ This command performs testing on provided testing dataset

#### For Prediction : 
- `python main.py predict {project_name}`
~ This command make predictions on the provided data inputs in `predict/input` directory

### To View Tensorboard : 
- `tensorboard --logdir projects/{project_name}/model/tblogs`
