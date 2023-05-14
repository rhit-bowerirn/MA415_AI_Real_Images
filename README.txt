AIR_Image is the folder with all the images, this is a necessary file to run the data

Format Data.ipynb needs to be run to create .npz files of the data which will be run in the programs.

Loader.py is a script that is made to load the data from the .npz files, it does not need to be run but 
it needs to be in the folder with the programs. 

The three files above are preliminary files necessary to run the rest of the project.



Logisitic Regressor (Images).ipynb is a simple logisitc regressor used as one of the baseline models and contains
the code that trains a basic logistic regressor, a lasso regressor, and a ridge regressor and calculates the train,
validation, and test scores. This file also includes the code that creates pixel importance figures that help show
which pixels are the most important in deciding whether an image is real or modified by AI.



