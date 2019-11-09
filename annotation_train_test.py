file = open("annotations.txt", "r")
line = file.read().splitlines()

tab = []

k = 0

while k <= len(line) :
    for i in line :
        newline = i.replace (",", " ")
        element = newline.split()
        tab.append(element)
    k += 1

i = 1

# Train proportion a
a = 0.8*len(line)

while i <= len(line) :
    
    if i == 1 : 
        annotation = open("annotation_train.txt", "w")
    
    elif 1 < i and i < a :
        annotation = open("annotation_train.txt", "a")
    
    elif i == a : 
        annotation = open("annotation_test.txt", "w")
    
    elif i > a :
        annotation = open("annotation_test.txt", "a")
    
    annotation.write(tab[i][0] + "\n")
    annotation.close()
    i+=1
    
file.close()