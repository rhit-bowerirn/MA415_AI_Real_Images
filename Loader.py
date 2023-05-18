# Scripts to import for getting data into dataframes

import pandas as pd
import numpy as np

def loadData(data):
    images = np.vstack(data['images'])
    labels = data['labels']
    columns = [str(i) for i in range(3072)] + ['label']
    return pd.DataFrame(np.column_stack((images, labels)), columns=columns)

def train_data():
    train = np.load('./Train_images.npz', allow_pickle=True)
    return loadData(train)


def test_data():
    test = np.load('./Test_images.npz', allow_pickle=True)
    return loadData(test)

def train_data_vgg16():
    df_real = pd.read_csv("Real_Train_Features.csv")
    df_fake = pd.read_csv("Fake_Train_Features.csv")
    return pd.concat([df_real,df_fake],axis=0).drop('Unnamed: 0', axis=1)

def test_data_vgg16():
    df_real = pd.read_csv("Real_Test_Features.csv")
    df_fake = pd.read_csv("Fake_Test_Features.csv")
    return pd.concat([df_real,df_fake],axis=0).drop('Unnamed: 0', axis=1)
