import uuid
import shutil
import split_folders
import os
import math
import importlib
from cv2 import cv2
import numpy as np
import pandas as pd
import utils
import validation

def prepare_dataset(project_name):
    # call ValidationClass to get all the paths and config file
    validObj = validation.ValidateClass(project_name)
    paths = validObj.paths
    config = validObj.config
    flag = None
    # dataset type 
    dataset_type = config.dataset_type

    ## Set paths
    # final output dataset
    dataset_path = paths['dataset_path']
    # loaded images into a single folder
    images_folder_path = paths['images_path']

    train_data_path  = f'{dataset_path}/{config.train_data_path}'
    test_data_path  = f'{dataset_path}/{config.test_data_path}'

    split_input_path = images_folder_path
    split_output_path = dataset_path

    # check if dataset already converted into images
    flag = check_the_dataset_status(train_data_path, test_data_path)

    # load and prepare dataset
    if((dataset_type == 'unspilt_data') & (flag == False)):
        # split images into train and test 
        split_dataset_into_train_test(split_input_path, split_output_path, config, paths)
    
    elif((dataset_type == 'csv') & (flag == False)):
        # get images into a single folder from csv
        prepare_csv_dataset(project_name, config, dataset_path, images_folder_path)
        # split dataset into train and test
        split_dataset_into_train_test(split_input_path, split_output_path, config, paths)
    
    elif((dataset_type == 'json') & (flag == False)):
        prepare_json_dataset(project_name, config, dataset_path, images_folder_path)
    
    else:
        return

def check_the_dataset_status(train_data_path, test_data_path):
    ''' This function checks the existance of train and test dataset ''' 
    if (os.path.exists(train_data_path) and os.path.exists(test_data_path)):
        if ([len(os.listdir(train_data_path)) != 0] or [len(os.listdir(test_data_path)) != 0]):
            flag = True
    else:
        flag = False
    return flag

def split_dataset_into_train_test(split_input_path, split_output_path, config, paths):
    
    split_folders.ratio(split_input_path, split_output_path, seed=1337, ratio = config.train_test_valid_ratio)

    # remove images folder which of no use after split
    try:
        for dir in os.listdir(f"{split_output_path}/val/"):
            for image in os.listdir(f"{split_output_path}/val/{dir}/"):
                shutil.move(f"{split_output_path}/val/{dir}/{image}", f"{paths['input_path']}", copy_function = shutil.copytree)
    except:
        utils.print_head(f"Unable to move validation dataset into predict folder!", color='red')

    try:
        shutil.rmtree(split_input_path)
        shutil.rmtree(f"{split_output_path}/val")
    except:
        try:
            os.rmdir(split_input_path)
            os.rmdir(f"{split_output_path}/val")
        except:
            pass

def prepare_json_dataset(project_name, config, dataset_path, images_folder_path):
    ''' This function loads json dataset, extract images and labels '''
    utils.print_head("Preparing dataset from provided .json file... ", color='darkcyan')
    pass

def prepare_text_dataset():
    ''' This function loads text dataset, extract images and labels '''
    utils.print_head("Preparing dataset from provided .txt file... ", color='darkcyan')
    pass

def prepare_csv_dataset(project_name, config, dataset_path, images_folder_path):
    ''' This function loads csv dataset, extract images and labels '''
    utils.print_head("Preparing dataset from provided .csv file... ", color='darkcyan')
    # load csv
    try:
        dataset = pd.read_csv(f'{dataset_path}/{config.csv_name}')
    except:
        utils.print_head("CSV data file is not provided!\nCheck `csv_name` in config file & `dataset` folder...", color='red')
        exit()

    # create folder to store images if not exists
    if os.path.exists(images_folder_path) == False:
        os.mkdir(images_folder_path)

    ## Labels
    # create folders for the labels found in the dataset
    for folder_name in dataset[config.label_column_name].unique():
        if os.path.exists(f'{images_folder_path}/{str(folder_name)}') == False:
            os.mkdir(f'{images_folder_path}/{str(folder_name)}')

    labels = dataset[config.label_column_name].tolist()
    
    ## Images 
    # save all the pixels values to list 'pixels' 
    pixels_of_images = dataset[config.images_column_name].tolist()

    for image_label, image_pixels in zip(labels, pixels_of_images) :

        # face contains pixels value of single image
        image = [int(pixel) for pixel in image_pixels.split(' ')]

        # convert image into array
        try:        
            image = np.asarray(image).reshape(config.img_height, config.img_width)
        except:
            utils.print_head("The size provided for resizing is larger than the image!", color='red')
        
        # save the image as .png file
        image_name = str(uuid.uuid4())
        cv2.imwrite(f"{images_folder_path}/{str(image_label)}/{image_name}.png", image)       
