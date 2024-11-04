import torch
import torchvision
from cifar10 import Net
from train5 import load_cifar5

def predict(batch_size=4):
    classes = ['plane', 'car', 'bird', 'cat', 'dog']
    _, testloader = load_cifar5(batch_size)

    net = Net()
    net.fc3 = torch.nn.Linear(84, 5)  # Match the last layer with 5 output classes
    net.load_state_dict(torch.load('./cifar5_net.pth', weights_only=True))
    net.eval()

    correct = 0
    total = 0
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            for label, prediction in zip(labels, predicted):
                label_name = classes[label.item()]
                pred_name = classes[prediction.item()]
                if label_name == pred_name:
                    correct_pred[label_name] += 1
                total_pred[label_name] += 1

    print(f'Accuracy on test images: {100 * correct / total:.2f} %')
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname] if total_pred[classname] > 0 else 0
        print(f'Accuracy for class {classname:5s}: {accuracy:.1f} %')

if __name__ == '__main__':
    predict()
