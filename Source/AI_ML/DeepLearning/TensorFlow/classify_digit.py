import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import os

# Load your trained model (or build and train first, then save with model.save('mnist_cnn.h5'))
script_dir = os.path.dirname(os.path.abspath(__file__))
mnist_cnn_file = os.path.join(script_dir, 'mnist_cnn.h5')
model = load_model(mnist_cnn_file)

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'image_6.jpg')
img = Image.open(img_path).convert('L')  # convert to grayscale

# Invert colors if needed (MNIST has white digits on black background)
img = ImageOps.invert(img)

# Resize to 28x28 (MNIST standard)
img = img.resize((28, 28))

# Convert to numpy array and normalize to [0,1]
img_array = np.array(img) / 255.0

# Reshape to (1, 28, 28, 1) for the model input
img_array = img_array.reshape(1, 28, 28, 1)

# Predict
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions)

print(f"Predicted digit: {predicted_class}")
