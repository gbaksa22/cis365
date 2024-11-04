import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from cifar10 import Net

# Define which classes to keep in the subset
selected_classes = [0, 1]  # Classes for 'plane' and 'car'

def load_cifar2(batch_size=4):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    # Load the entire CIFAR-10 dataset
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
    
    # Filter dataset for the selected classes
    trainset.data = trainset.data[[i for i, label in enumerate(trainset.targets) if label in selected_classes]]
    trainset.targets = [selected_classes.index(label) for label in trainset.targets if label in selected_classes]
    testset.data = testset.data[[i for i, label in enumerate(testset.targets) if label in selected_classes]]
    testset.targets = [selected_classes.index(label) for label in testset.targets if label in selected_classes]

    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)
    
    return trainloader, testloader

def train(batch_size=4, epochs=2):
    trainloader, _ = load_cifar2(batch_size)
    net = Net()
    net.fc3 = nn.Linear(84, 2)  # Update the last layer for 2 classes

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(epochs):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            if i % 2000 == 1999:
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

    PATH = './cifar2_net.pth'
    torch.save(net.state_dict(), PATH)
    print('Finished Training')

if __name__ == '__main__':
    train()
