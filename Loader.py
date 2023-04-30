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
