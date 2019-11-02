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

while i <= len(line) :
    
    if i < 10 :
        annotation = open("gen_000"+str(i)+".txt", "w")
    
    elif i < 100 :
        annotation = open("gen_00"+str(i)+".txt", "w")
    
    elif i < 1000 :
        annotation = open("gen_0"+str(i)+".txt", "w")
    
    elif i == 1000 :
        annotation = open("gen_"+str(i)+".txt", "w")
    
    annotation.write(tab[i][5] + " " + tab[i][1] + " " + tab[i][2] + " " + tab[i][3] + " " + tab[i][4])
    annotation.close()
    i+=1
    
file.close()
