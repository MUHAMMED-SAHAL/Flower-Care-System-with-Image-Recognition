from tensorflow import keras
import numpy as np
from keras.preprocessing import image


def predict(dir1):
    # Load the trained model
    model = keras.models.load_model('flower_classification_model.h5')

    # Load and preprocess the new image(s)
    img_path = dir1
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0  # Rescale the pixel values to [0, 1]

    # Make predictions
    predictions = model.predict(img)

    # Get the predicted class label
    class_index = np.argmax(predictions)

    # Define a mapping of class indices to class labels
    class_labels = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

    # Get the predicted class label
    predicted_label = class_labels[class_index]

    # Print the predicted class label and confidence
    print(f"Predicted Class: {predicted_label}")
    print(f"Confidence: {predictions[0][class_index]:.2f}")

    return predicted_label, predictions[0][class_index]
