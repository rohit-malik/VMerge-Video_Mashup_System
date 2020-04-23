from os import listdir
from os.path import isfile, join
import re
import os
import specto
from sklearn.metrics import accuracy_score
import random
from sklearn.metrics import mean_absolute_error

def getlist(mypath):
    temp_list = []
    for root, directories, filenames in os.walk(mypath):
        for filename in filenames:
            if "py" in filename:
                continue
            file_temp = os.path.join(root,filename)
            a = re.split("_|\.",filename)
            astart = a[-3]
            aend = a[-2]
            word = ""
            for i in range(0, len(a)-3):
                word = word + a[i]
            dict_temp = {"fullname": file_temp, "name": word, "start_time": int(astart), "end_time": int(aend)}
            temp_list.append(dict_temp)
    return temp_list

list_maroon5 = getlist("./Maroon5_Seoul/")
list_eminem = getlist("./Eminem_Seoul/")
list_bhangra = getlist("./Bhangra/")

def get_positive_count(passed_list):
    list_positives = []
    list_negatives = []
    count_positive = 0
    for i in range(0, len(passed_list)):
        ele = passed_list[i]
        for j in range(i+1,len(passed_list)):
            ele2 = passed_list[j]
            if ele["name"] != ele2["name"]:
                isOverlap = 0
                if (int(ele2["start_time"]) > int(ele["start_time"])) and (int(ele2["start_time"]) < int(ele["end_time"])):
                    isOverlap = 1
                elif (int(ele["start_time"]) > int(ele2["start_time"])) and (int(ele["start_time"]) < int(ele2["end_time"])):
                    isOverlap = 1
                else:
                    isOverlap = 0
                if isOverlap == 1:
                    count_positive = count_positive + 1
                    list_positives.append((ele, ele2))
                else:
                    list_negatives.append((ele,ele2))
    return list_positives, list_negatives, count_positive

list_positive1, list_negative1, count1 = get_positive_count(list_maroon5)
list_positive2, list_negative2, count2 = get_positive_count(list_eminem)
list_positive3, list_negative3, count3 = get_positive_count(list_bhangra)

#print(count1)
#print(count2)
#print(count3)
#print(count1+count2+count3)

list_positives = list_positive1 + list_positive2 + list_positive3
list_negatives = list_negative1 + list_negative2 + list_negative3

print("Total Available Positive Points: ", len(list_positives))
print("Total Available Positive Points: ", len(list_negatives))

num_positive_points = 500
num_negative_points = 500

print("Number of Positive Points Choosen: ", num_positive_points)
print("Number of Negative Points Choosen: ", num_negative_points)

random.shuffle(list_positives)
random.shuffle(list_negatives)
list_positives = list_positives[:num_positive_points]
list_negatives = list_negatives[:num_negative_points]

list_outputs = []
list_outputs_alignment = []
y_list_alignment = []
y_list = []
y_list_al = []
list_outputs_al = []
Iteration = 1
for item in list_positives:
    print("Iteration--------" + str(Iteration))
    Iteration = Iteration + 1
    print("Filename1: " + item[0]["fullname"])
    print("Filename2: " + item[1]["fullname"])
    output = specto.check_overlap(item[0]["fullname"], item[1]["fullname"])
    print("Real output: " + str(1) + " Output Predicted: " + str(output))
    """
        if output[0]==1:
            real_alignment = item[1]["start_time"] - item[0]["start_time"]
            predicted_alignment = output[1]
            if abs(real_alignment-predicted_alignment) <= 2:
                list_outputs.append(1)
            else:
                list_outputs.append(0)
        else:
            list_outputs.append(output[0])
    """
    list_outputs.append(output[0])
    y_list.append(1)
    y_list_alignment.append(item[1]["start_time"] - item[0]["start_time"])
    list_outputs_alignment.append(output[1])
    if output[0]==1:
        y_list_al.append(item[1]["start_time"] - item[0]["start_time"])
        list_outputs_al.append(output[1])
for item in list_negatives:
    print("Iteration--------" + str(Iteration))
    Iteration = Iteration + 1
    print("Filename1: " + item[0]["fullname"])
    print("Filename2: " + item[1]["fullname"])
    output = specto.check_overlap(item[0]["fullname"], item[1]["fullname"])
    print("Real output: " + str(0) + " Output Predicted: " + str(output))
    list_outputs.append(output[0])
    y_list.append(0)

accuracy = accuracy_score(y_list, list_outputs)
alignment_error = mean_absolute_error(y_list_alignment, list_outputs_alignment)
alignment_error_al = mean_absolute_error(y_list_al, list_outputs_al)
print("\n----------------------------------Results-------------------------------------------")
print("Total Number of Data Points Chosen: " + str(num_positive_points+ num_negative_points))
print("Number of Positive Data Points: " + str(num_positive_points))
print("Number of Negative Data Points: " + str(num_negative_points))
print("Accuracy Achieved in Detecting Overlap: ", accuracy)
print("Mean Absolute Error in Alignment in case of actual overlap: ", alignment_error)
print("MAE in alignment when algorithm detects overlap: ", alignment_error_al)
