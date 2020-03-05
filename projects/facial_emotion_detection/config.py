''' DATASET PARAMETERS '''

# training and testing dataset is needed, as data for validation is spliting during training
# ** do not change this **
train_data_path = "train"
test_data_path = "test"

''' DATASET TO PROCESS '''
## select the dataset type from given options :
# None : when dataset is perfectly in required and train/test format
# 'unspilt_data' : when dataset is in image format but exists in a single folder
# 'csv_urls' : when dataset is in .csv file in url form with labels
# 'csv_pixels : when dataset is in .csv file in the pixel values form with labels 
# 'json' : when dataset is in .json file in url form with labels 
dataset_type = 'json'

## .CSV 
csv_filename = 'data.csv'   #'fer2013.csv'

### csv containing URLs and LABEL 
image_url_column_name = "image_url" 
image_name_column_index = 0
image_url_column_index = 1
image_label_column_index = 4
## OR
### csv containing PIXEL values and LABEL 
images_column_name = 'pixels'
label_column_name = 'emotion'

## .JSON 
json_filename = 'json_example.json'
image_url_key_name = 'idfronturl'
image_name_key_name = '_id'
image_label_key_name = 'status'

''' DATA SPLIT '''
# split ratio to split dataset into train and test, the last argument is to separate images for prediction phase
train_test_valid_ratio = (0.8, 0.1, 0.1)
# validation split from training dataset
validation_split = 0.01


''' DATA AUGMENTATION '''
# randomly rotate images in the range (degrees 0 to 180)
rotation_range = 0

# randomly shift images horizontally/vertically (fraction of total width/height)
width_shift_range = 0
height_shift_range = 0

# randomly flip images
horizontal_flip = False
vertical_flip = False

# Random zoom
zoom_range = 0


''' MODEL PARAMETERS '''

# give model a name
model_name = 'Shapes-Classification'

# Select one of these or can add and define more inside model.py : `vgg16`, `fer`, `customized_model_name` 
selected_model =  'fer'

# Image dimensions (used in preprocessing images & model) 
img_height = 48
img_width = 48
channel = 3

# Class selection
class_mode = 'categorical'
nb_classes = 7

# Training params
epochs = 2
lr_rate = 0.01
batch_size = 128
loss = "categorical_crossentropy"

# Optimizers
optimizer = 'adam'

# [ADAM Config]
options = {
    'name' : 'adam',
    'lr': 0.01,
}

## [Adadelta Config]
# options = {
#   'name' : 'adadelta',
#   'lr': 0.01,
#   'rho': 0.95,
#   'epsilon': None, 
#   'decay': 0.0
# }

## [RMSProp Config]
# options = {
#   'name' = 'rmsprop',
#    'lr': 0,
#    'rho': 0.9,
#    'epsilon': None, 
#    'decay':0.0
# }

## [SGD Config]
# options = {
#   'name' : 'sgd',
#   'lr' : 0,
#   'momentum' : None,
#   'decay' : None,
#   'nesterov' : None
# }