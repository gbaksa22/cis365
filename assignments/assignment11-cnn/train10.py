import torch
import torch.optim as optim
from enhanced_cifar10 import Net, load_cifar10
import torch.nn as nn

def train(batch_size=10, epochs=2):
    trainloader, _ = load_cifar10(batch_size)
    
    net = Net()
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

    PATH = './cifar10_net.pth'
    torch.save(net.state_dict(), PATH)

if __name__ == '__main__':
    train()
