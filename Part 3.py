from scipy import *


def compute_dkl():
    res = []
    for i in range(4):
        with open("benchmark/dataset{}/motif.txt".format(str(i)),"r") as file1, open ("motif_finder/dataset{}/predictedmotif.txt".format(str(i)),"r") as file2:
            next(file1)
            next(file2)
            line1 = file1.readline()
            line2 = file2.readline()
            sum = 0
            while line1 and line2:
                P = line1.split()
                Q = line2.split()
                for j in range(4):

                    if float(Q[j]) == 0.0 or float(P[j]) == 0.0:
                        temp = 0.0
                    else:
                        temp = float(P[j]) * log(float(P[j]) / float(Q[j]))
                    sum += temp

                line1 = file1.readline()
                line2 = file2.readline()
            res.append(sum)
    return res

def compute_position():
    res = []
    counts = []
    for i in range(4):
        with open("benchmark/dataset{}/motif.txt".format(str(i)), "r") as file1, open(
                "motif_finder/dataset{}/predictedsites.txt".format(str(i)), "r") as file3,open(
            "benchmark/dataset{}/sites.txt".format(str(i)), "r") as file2:
            num = int(file1.readline().split()[1])


            line1 = file2.readline()
            line2 = file3.readline()
            sum = 0
            array = []
            count = 0
            while line1 and line2:
                P = line1.split()
                Q = line2.split()

                temp = int(P[0]) + num - int(Q[0])
                if temp >= num / 2:
                    count+=1
                array.append(temp)
                line1 = file2.readline()
                line2 = file3.readline()
            res.append(array)
            counts.append(count)
    return res,counts

def main():
    res,counts = compute_position()
    print(res)
    print(counts)

    res = compute_dkl()
    print(res)
main()