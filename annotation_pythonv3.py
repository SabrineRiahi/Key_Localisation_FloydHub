import cv2

file = open("annotations.txt", "r")
line = file.read().splitlines()

tab = []

k = 0

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = float((box[0] + box[1]))/2.0
    y = float((box[2] + box[3]))/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

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
    

    img = cv2.imread(tab[1000-i][0],0)
    size = img.shape[:2]     
    box = [tab[1000-i][1], tab[1000-i][3], tab[1000-i][2], tab[1000-i][4]]
    x,y,w,h = convert(size,box)
    
    annotation.write(21 + " " + x + " " + y + " " + w + " " + h)
    annotation.close()
    i+=1
    
file.close()