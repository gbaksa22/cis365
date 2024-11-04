import torch
from enhanced_cifar10 import Net, load_cifar10

def predict(batch_size=10):
    # CIFAR-10 classes
    classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    _, testloader = load_cifar10(batch_size)
    
    net = Net()
    net.load_state_dict(torch.load('./cifar10_net.pth', weights_only=True))  # Setting weights_only=True
    net.eval()  # Set the model to evaluation mode

    correct = 0
    total = 0
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # Collect predictions for each class
            for label, prediction in zip(labels, predicted):
                label_name = classes[label.item()]
                pred_name = classes[prediction.item()]
                
                if label_name == pred_name:
                    correct_pred[label_name] += 1
                total_pred[label_name] += 1

    print(f'Accuracy of the network on the {total} test images: {100 * correct / total:.2f} %')

    # Print accuracy for each class
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname] if total_pred[classname] > 0 else 0
        print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')

if __name__ == '__main__':
    predict()
