# Import Dependencies
import torch
import os
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, transforms

# Download datasets
train = datasets.MNIST(root="Data", download=True, train=True, transform=ToTensor())
dataset = DataLoader(train, 32) # 32 is the backprop

class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, (3,3)),
            nn.ReLU(),
            nn.Conv2d(32, 64, (3,3)),
            nn.ReLU(),
            nn.Conv2d(64, 64, (3,3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64 * (28-6) * (28-6), 10 ) ## 1 * 28 * 28, 10 classes.
        )

    def forward(self, x):
        return self.model(x)
    

# Instance of neural network, loss, optimizer
clf = ImageClassifier().to('cuda') # if no cuda or nvidia gpu display device, then use 'cpu'
opt = Adam(clf.parameters(), lr = 1e-3)
loss_fn = nn.CrossEntropyLoss()

#Training Flow
if __name__ == "__main__":
    with open('model_state.pt', 'rb') as f:
        clf.load_state_dict(load(f))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'TestImages')
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            file_path = os.path.join(folder_path, filename)
            print(f'Loaded image: {file_path}')

            img = Image.open(file_path)
            img_tensor = ToTensor()(img).unsqueeze(0).to('cuda')

            print(torch.argmax(clf(img_tensor)))