from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16
import numpy as np


model = VGG16(weights='imagenet')
# load an image from file
img = load_img('tutorml/static/tutorml/img/avatar2.png', target_size=(224, 224))
# convert the image pixels to a numpy array
image = img_to_array(img)
# reshape data for the model
image = np.expand_dims(image, axis=0)
# prepare the image for the VGG model
image = preprocess_input(image)
# predict the probability across all output classes
features = model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(features)
print(label)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))