# Import Dependencies
import os
from PIL import Image
import torch
from torchvision.transforms import ToTensor, transforms

# Define the transform pipeline
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Convert to grayscale
    transforms.Resize((28, 28))  # Resize to (28, 28)
])

#Training Flow
if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'TestImages')
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            file_path = os.path.join(folder_path, filename)
            print(f'Loaded image: {file_path}')

            # Load the image
            image = Image.open(file_path)

            # transform image
            transformed_image = transform(image)

            # Save the grayscale image
            transformed_image.save(file_path)
            print(f'Saved transformed_image: {file_path}')