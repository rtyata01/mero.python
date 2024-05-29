# Import Dependencies
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

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
    for epoch in range(10): # train for 10 epochs
        for batch in dataset:
            x,y = batch
            x,y = x.to('cuda'), y.to('cuda')
            yhat = clf(x)
            loss = loss_fn(yhat, y)

            # Apply backprop
            opt.zero_grad()
            loss.backward()
            opt.step()

        print(f"Epoch:{epoch} loss is: {loss.item()}")

    with open('model_state.pt', 'wb') as f:
        save(clf.state_dict(), f)