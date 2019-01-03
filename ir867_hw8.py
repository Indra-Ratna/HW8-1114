#Indra Ratna
#CS-UY 1114
#Indra Ratna
#11 November 2018
#Homework 8
import math

def read_file(filename):
    myList = []
    f = open(filename,"r")
    f.readline()
    for line in f:
        list = (line.split(","))
        myList.append(list)
    f.close()
    return myList

def find_most_exclusive_womens_college(colleges):
    final_college = "-"
    adm_rate = 1.0
    for line in colleges:
        if((line[22])!="NULL" and line[24]!="NULL"):
            if(int(line[22])==1):
                if(float(line[24])<adm_rate):
                  final_college = line[3]
                  adm_rate = float(line[24])
    return final_college

def average_sat_score_in_ny(colleges):
    sum = 0
    number = 0
    for line in colleges:
        if(line[5]!="NULL" and line[25]!="NULL"):
            if(line[5]=="NY"):
                sum+= int(line[25])
                number+=1
    avg = sum/number
    return avg

def distance(first,second):
    a1 = first[0]
    a2 = first[1]
    b1 = second[0]
    b2 = second[1]
    distance = math.sqrt(math.pow(a1-b1,2)+math.pow(a2-b2,2))
    return distance

def find_college_nearest_center_of_us(colleges):
    center = (39.833333, -98.583333)
    d = 1000000000
    college = "-"
    for line in colleges:
        if(line[18]!="NULL" and line[19]!="NULL"):
            center_to = distance(center,(float(line[18]),float(line[19])))
            if center_to<d:
                d = center_to
                college = line[3]
    return college

def main():
    colleges = read_file("colleges.csv")
    print("Most exclusive womens college is " +find_most_exclusive_womens_college(colleges))
    print("Average SAT of all NY schools" +average_sat_score_in_ny(colleges))
    print("College nearest the center of the US"+find_college_nearest_center_of_us(colleges))
main()
