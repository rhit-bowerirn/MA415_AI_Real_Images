# MA415 Project: Training on CIFAKE
## Authors:
Blake Baker, Ryan Bowering, William Chong, Derick Miller, Raymond Zhao

<br>

## See how well you can identify AI-Generated images with our human baseline test!
https://forms.gle/f69VbVkigJE9ax8N9

<br>

## Overview
* Used Logistic Regression with L1 and L2 Regularization on the raw pixel data
* Investigated pixel importance in final predictions
* Used a Noise Filter on the images and used a Logistic Regressor on the filtered images
* Extracted features using TensorFlow's VGG16 model
* Trained a Logistic Regressor, Random Forest, Gradient Boosted Trees and Support Vector Machines on extracted features

<br> 
 
## Results:
* Achieved testing accuracy of 0.67 with Logistic Regression on raw pixel data
* Achieved testing accuracy of 0.85 with Logistic Regression on VGG16 extracted features
* Achieved testing accuracy of 0.87 with Random Forests on on VGG16 extracted features
* Achieved testing accuracy of 0.90 with Gradient Boosted Trees on VGG16 extracted features
* Achieved testing accuracy of 0.91 with Support Vector Machines on VGG16 extracted features
* Achieved testing accuracy of 0.57 with Logistic Regression on the SRM filtered images

* Final Report is contained in the repository

<br>

# Usage Instructions
## Preprocessing data

AIR_Image is the folder with all the images, this is a necessary file to run the data

  * ***Skip step 1 if you already have the following files:**
     * Test_images.npz
     * Train_images.npz

1. Run Format Data.ipynb to create .npz files of the raw pixel data which is used in some notebooks.

  * ***Skip step 2 if you already have the following files:**
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




