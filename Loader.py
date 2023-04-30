import pandas as pd
import numpy as np


def loadData(data):
    flat_arrays = np.array([i.flatten()
                            for i in data['images']], dtype=np.uint8)
    num_pixels = flat_arrays.shape[1]
    col_names = [str(i) for i in range(num_pixels)]
    combined = np.hstack([flat_arrays, data['labels'].reshape(-1, 1)])
    return pd.DataFrame(combined, columns=col_names + ['label'])


def train_data():
    train = np.load('./Train_images.npz', allow_pickle=True)
    return loadData(train)


def test_data():
    test = np.load('./Test_images.npz', allow_pickle=True)
    return loadData(test)
