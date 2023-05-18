# MA415 Project: Training on CIFAKE
## Authors:
Blake Baker, Ryan Bowering, William Chong, Derick Miller, Raymond Zhao


# Instructions
## Preprocessing data

AIR_Image is the folder with all the images, this is a necessary file to run the data

* ***Skip step 1 if you already have the following files:
  * Test_images.npz
  * Train_images.npz

1. Run Format Data.ipynb to create .npz files of the raw pixel data which is used in some notebooks.

* ***Skip step 2 if you already have the following files:
  * Fake_Test_Features.csv
  * Fake_Train_Features.csv
  * REAL_Test_Features.csv
  * Real_Train_Features.csv

2. Run VGG16FeatureCreation.ipynb to create .csv files with extracted features

3. Loader.py is a script that is made to load the data from the .npz files, it does not need to be run but 
it needs to be in the folder at the same level the notebooks. 


## Setting up Kaggle

Several of our notebooks use Kaggle's servers. This is noted in the title of the notebook. To set up kaggle do the following:
1. Create an account and verify your phone number to use accelerators
2. Create a new dataset called vgg16-cifake and upload all 4 .csv files to it
3. For SVM and GBT, ensure that the P100 GPU is enabled. If you get the error 'No module cudf' 'No module cuml', you need to enable the GPU
4. For SVM and GBT, running it once will give you an error on the cell with all the imports. Run it again and the error will go away




