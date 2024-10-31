### **Introduction**

This is a small AI project trainig on images of cats and dogs and teaching a model to identify which is which. The dataset can be found here:
https://www.kaggle.com/datasets/arpitjain007/dog-vs-cat-fastai

The model will use TensorFlow and Keras to create layers to train the AI model. The results can then be viewwed in a browser.
Github wouldn't let me include the .pkl files created for the dataset, hence why I have included the link.

### **Installation**
The dataset will need to be dowloaded from Kaggle, and put somewhere locally on your system. 
Once it is local, the ```DIRECTORY``` variable in **__cats_vs_dogs.py__** will need to be adjusted to whatever directory the photos are in.
You will want to put the images inside the project you are running the code in, e.g. I used PyCharm and 
added the data into my project folder. Once your data is inside the project folder and the ```DIRECTORY``` variable
is pointing to the right place. For me it was
```'C:\Users\callm\PycharmProjects\catsAndDogsAI\archive\dogscats\dogscats\train'```, but it depends on where you have the dataset.

Once you have downloaded the dataset at the link above and the **DIRECTORY** variable is pointing to the correct place, you can run
**__cats_vs_dogs.py__** by opening a terminal, pointing to the containting directory 
(for me it is ```C:\Users\callm\PycharmProjects\catsAndDogsAI```) and typing ```python cats_vs_dogs.py``` in the terminal and pressing enter.
Once this has executed, you will have your ```.pkl``` files. Then you will simply need to run the ```training.py``` file by typing ```python training.py```
in the terminal and pressing enter. 

This will run the model. At this point, to run another model, you will only need to run **python training.py** again. To view the results, 
in the same terminal type ```tensorboard --logdir=logs/```.

This should give you an ouput similar to the following:
```python
-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-08-20 14:44:06.315058: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical
results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.17.1 at http://localhost:6006/ (Press CTRL+C to quit)
```

At this point, you will just need to copy the ```localhost``` address above, copy it into a browser, and you should get a visualization of the 
results of however many models you ran.

I got this simple project from the following:

https://www.youtube.com/watch?v=FLf5qmSOkwU&list=PLUc_7x68VCSN_WNoeAnfydLL22sYyobgW
