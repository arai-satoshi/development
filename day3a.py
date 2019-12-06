import csv
import matplotlib.pyplot as plt

def draw_path(filename):
    pathX1 = [0]
    pathY1 = [0]
    pathX2 = [0]
    pathY2 = [0]
    
    with open(filename) as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    for i in range(len(l[0])):
        if 'R' in l[0][i]:
            pathX1.append(pathX1[i]+int(l[0][i][1:]))
            pathY1.append(pathY1[i])
        if 'L' in l[0][i]:
            pathX1.append(pathX1[i]-int(l[0][i][1:]))
            pathY1.append(pathY1[i])
        if 'U' in l[0][i]:
            pathX1.append(pathX1[i])
            pathY1.append(pathY1[i]+int(l[0][i][1:]))
        if 'D' in l[0][i]:
            pathX1.append(pathX1[i])
            pathY1.append(pathY1[i]-int(l[0][i][1:]))

    for j in range(len(l[1])):
        if 'R' in l[1][j]:
            pathX2.append(pathX2[j]+int(l[1][j][1:]))
            pathY2.append(pathY2[j])
        if 'L' in l[1][j]:
            pathX2.append(pathX2[j]-int(l[1][j][1:]))
            pathY2.append(pathY2[j])
        if 'U' in l[1][j]:
            pathX2.append(pathX2[j])
            pathY2.append(pathY2[j]+int(l[1][j][1:]))
        if 'D' in l[1][j]:
            pathX2.append(pathX2[j])
            pathY2.append(pathY2[j]-int(l[1][j][1:]))

    plt.plot(pathX1,pathY1)
    plt.plot(pathX2,pathY2)
    plt.plot(0,0,marker="o")
    plt.show()

                

if __name__ == '__main__':
    draw_path('input.csv')
