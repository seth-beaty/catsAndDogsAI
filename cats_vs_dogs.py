import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
import pickle

DIRECTORY = r'C:\Users\callm\PycharmProjects\catsAndDogsAI\archive\dogscats\dogscats\train'
CATEGORIES = ['cats', 'dogs']
IMG_SIZE = 200


def main():

    data = []

    for category in CATEGORIES:
        folder = os.path.join(DIRECTORY, category)
        label = CATEGORIES.index(category)
        for image in os.listdir(folder):
            img_path = os.path.join(folder, image)
            img_arr = cv2.imread(img_path)
            img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
            data.append([img_arr, label])

    random.shuffle(data)

    x = []
    y = []
    for features, labels in data:
        x.append(features)
        y.append(labels)

    x = np.array(x)
    y = np.array(y)

    pickle.dump(x, open('x.pkl', 'wb'))
    pickle.dump(y, open('y.pkl', 'wb'))


if __name__ == "__main__":
    main()
