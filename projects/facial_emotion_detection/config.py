''' DATASET PARAMETERS '''

# training and testing dataset is needed, as data for validation is spliting during traning
train_data_path = "train"
test_data_path = "test"

# select the dataset type then given options : 'csv' /'json' / 'unspilt_data', 'None' (for the saved image dataset)
dataset_type = 'csv'

# if the dataset is csv
csv_name = 'fer2013.csv'
images_column_name = 'pixels'
label_column_name = 'emotion'

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

model_name = 'Shapes-Classification'

# Select one of these : `vgg16`, `fer`, `customized_model_name` 
selected_model =  'fer'

# Image params (used in preprocessing images & model)
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