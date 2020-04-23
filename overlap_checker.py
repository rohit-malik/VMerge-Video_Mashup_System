import specto
from sklearn.metrics import accuracy_score
import random

# specto.check_overlap("1.mp3", "2.mp3")
list_positives = []
list_negatives = []
with open("overlapFinder/event_animal_overlap.txt","r") as file:
    for line in file:
        line_list = line.split()
        folder = "Audio Project/event_animal/"
        if int(line_list[2])==1:
            list_positives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))
        else:
            list_negatives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))

with open("overlapFinder/event_complete_overlap.txt","r") as file:
    for line in file:
        line_list = line.split()
        folder = "Audio Project/event_complete/"
        if int(line_list[2])==1:
            list_positives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))
        else:
            list_negatives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))

with open("overlapFinder/event_daylight_overlap.txt","r") as file:
    for line in file:
        line_list = line.split()
        folder = "Audio Project/event_daylight/"
        if int(line_list[2])==1:
            list_positives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))
        else:
            list_negatives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))

with open("overlapFinder/event_lost_star_overlap.txt","r") as file:
    for line in file:
        line_list = line.split()
        folder = "Audio Project/event_lost_star/"
        if int(line_list[2])==1:
            list_positives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))
        else:
            list_negatives.append((folder + line_list[0],folder + line_list[1],int(line_list[2])))


print("Number of postive data points: ",len(list_positives))
print("Number of negative data points: ",len(list_negatives))

num_positive_points = 150
num_negative_points = 150

random.shuffle(list_positives)
random.shuffle(list_negatives)
list_positives = list_positives[:num_positive_points]
list_negatives = list_negatives[:num_negative_points]

list_outputs = []
y_list = []
Iteration = 1
for item in list_positives:
    print("Iteration--------" + str(Iteration))
    Iteration = Iteration + 1
    print("Filename1: " + item[0])
    print("Filename2: " + item[1])
    output = specto.check_overlap(item[0], item[1])
    print("Real output: " + str(item[2]) + " Output Predicted: " + str(output))
    list_outputs.append(output)
    y_list.append(item[2])
for item in list_negatives:
    print("Iteration--------" + str(Iteration))
    Iteration = Iteration + 1
    print("Filename1: " + item[0])
    print("Filename2: " + item[1])
    output = specto.check_overlap(item[0], item[1])
    print("Real output: " + str(item[2]) + " Output Predicted: " + str(output))
    list_outputs.append(output)
    y_list.append(item[2])

accuracy = accuracy_score(y_list, list_outputs)
print("\n----------------------------------Results-------------------------------------------")
print("Total Number of Data Points Chosen: " + str(num_positive_points+ num_negative_points))
print("Number of Positive Data Points: " + str(num_positive_points))
print("Number of Negative Data Points: " + str(num_negative_points))
print("Accuracy Achieved: ", accuracy)
