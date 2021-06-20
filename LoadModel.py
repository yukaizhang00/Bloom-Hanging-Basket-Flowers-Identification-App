import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

fafanames = ("African_lily", "Anthurium","Astilbe", "Begonia _rieger", "Bellflower","Bougainvillea","Bougainvillea_tree","Bridal_veil","Bromeliad","Citrosa_geranium", "Firetail","Kalanchoe", "Natal_lily", "Pot_mum")
fafanames = os.listdir('FafaSet')
model = keras.models.load_model('Model_30.h5')
image_size = (180, 180)
img = keras.preprocessing.image.load_img("Try1.jpg", target_size=image_size)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)
predictions = model.predict(img_array)
predictions = list(predictions[0])
(fi,se) = sorted(range(len(predictions)), key=lambda k: predictions[k])[:-3:-1]
if predictions[fi]+predictions[se] < 0.6:
    print("Unforturnatly this might not be a garden flower, find something else to play.")
else:
    print("Well, I can tell you that it is", int(predictions[fi]*100) ,"% chance to be",fafanames[fi] ,", and",int(predictions[se]*100), "% chance to be",fafanames[se], ". Now get lost.")
