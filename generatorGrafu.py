import random

n = 150

dag_matrix = [[0 for i in range(n)] for t in range(n)]
odd_vertex = []

edges = int(n * (n - 1) * 0.6)

los = 0

while (edges != 0):
    for i in range(n):
        if (edges != 0 and i + 1 < n):
            dag_matrix[i][i+1] = 1
            #dag_matrix[i+1][i] = 1
            edges -= 1
    for i in range(n):
        for t in range(i+1, n):
            if (edges != 0):
                los = random.randint(0, 1)

                if (los == 1 and dag_matrix[i][t] == 0):
                    dag_matrix[i][t] = los
                    #dag_matrix[t][i] = los
                    edges -= 1




dane = open('file.txt', 'w')
dane.write(str(n))
dane.write("\n")

for i in range(n):
    for t in range(n):
        if(dag_matrix[i][t] == 1):
            dane.write(str(i + 1))
            dane.write(" ")
            dane.write(str(t + 1))
            dane.write("\n")

dane.close()




