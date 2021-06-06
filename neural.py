# python3 neural.py

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import csv

modality = []
metrics = []
audial = [0, 0, 0]
visual = [0, 0, 1]
discret = [0, 1, 0]

with open("data.csv", newline='') as data:
    data_reader = csv.reader(data, delimiter=";")

    for row in data_reader:
        if row[5] == '1':
            modality.append(audial)
        elif row[5] == '2':
            modality.append(visual)
        elif row[5] == '3':
            modality.append(discret)
        metrics.append(row[0:4])

metrics_train, metrics_test, modality_train, modality_test = train_test_split(metrics, modality, test_size=0.33)
neuralnet = MLPClassifier(solver='adam', activation='relu', hidden_layer_sizes=(10, 10))
neuralnet.fit(metrics_train, modality_train)
accuracy_test = neuralnet.score(metrics_test, modality_test)
accuracy_train = neuralnet.score(metrics_train, modality_train)

print(str(accuracy_test * 100) + "% accuracy_test")
print(str(accuracy_train * 100) + "% accuracy_train")
