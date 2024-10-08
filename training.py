import pickle
import time
from keras.api.models import Sequential
from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.python.keras.engine.input_layer import Input
from keras.api.callbacks import TensorBoard

NAME = f'cat-vs-dog-prediction-{int(time.time())}'


def main():

    tensorboard = TensorBoard(log_dir=f'logs\\{NAME}\\')

    x = pickle.load(open('x.pkl', 'rb'))
    y = pickle.load(open('y.pkl', 'rb'))
    x = x/255

    # Create Model
    model = Sequential()

    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(MaxPooling2D((2,2)))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())

    model.add(Dense(128, input_shape=Input(x.shape[1:]), activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x,y, epochs=5, validation_split=0.1, batch_size=32, callbacks=[tensorboard])


if __name__ == "__main__":
    main()