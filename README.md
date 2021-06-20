# GardenHackathon
## Bloom - Hanging Basket Flowers Identification App
A flower image classification program based on python and keras.

This project has two parts, (i) training part and (ii) GUI part.

Before running the python files, make sure pip installed the following packages: `tensorflow`, `keras`, `PyQt5`.

### Part (i) Training:

For training the model, we use Keras built in Xception network trainer to train the model for classifying flowers. For the purpose of example, please extract the `FafaSet.zip` file to the current location.
You can adding more classes of flower by adding folder containing pictures in the FafaSet file. To increase the iteration of model training, you can change `epochs` in the `TrainModel.py` file.

### Part (ii) Gui:

Open the python file `GuiPy.py` and run it, the gui will show up and simply drag the image into the drop box. (I use IDLE(Python 3.9) to run the file)
