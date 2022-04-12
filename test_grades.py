import csv
import statistics

outfile = open("output.csv",'w')
outfile_header = "First Name, Surname, Average, Grade\n"
outfile.write(outfile_header)
with open('input.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for line in csv_reader:
        student_first_name = line[0]
        student_last_name = line[1]
        marks = line[2:6]
        marks_list = [int(i) for i in marks]
        avg_mark = round(statistics.mean(marks_list),1)
        if avg_mark >=80:
            grade = "A+"
        elif avg_mark >=70:
            grade = "B-"
        elif avg_mark >=60:
            grade = "C"
        elif avg_mark >=50:
            grade = "D"
        elif avg_mark >=40:
            grade = "E"
        elif avg_mark >=0:
            grade = "F-"         
        line = "{},{},{},{}\n".format(student_first_name,student_last_name,avg_mark,grade)
        outfile.write(line)
outfile.close()        