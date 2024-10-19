#import csv
import matplotlib.pyplot as plt

# Function to read CSV data
def read_student_data(filename):
    students = []
    with open("/content/drive/MyDrive/DS_foundation/assignment_1/student.csv", "r") as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')    #Read the header line
        for line in lines[1:]:  #skip the header line
            students.append(line.strip().split(','))
        ##reader = csv.reader(file)
        #next(reader)  # Skip the header row
        #for row in reader:
            #students.append(row)
    return students

#Function to generate a pie cahrt for the gender ratio
def gender_pie_chart(data):
    gender_counts = {'Male': 0, 'Female': 0}

    for entry in data:
        gender = entry[1]   #entry index in the csv file 2 element
        if gender in gender_counts:
            gender_counts[gender] += 1
        else:
            print(f"Unexpected gender value: {gender}")

    labels = gender_counts.keys()
    sizes = gender_counts.values()

    plt.figure(figsize=(7,7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['blue', 'pink'])
    plt.title('Gender Ratio')
    plt.axis('equal')   #Equal aspect ratio ensures that pie is drawn as a circle.

def marks_pie_chart(data):
    pass_count = 0
    fail_count = 0

    for entry in data:
        math = int(entry[2])    #3rd element
        english = int(entry[3])    #4th element
        average = (math + english) / 2

        if average >= 40:
            pass_count += 1
        else:
            fail_count += 1

    labels = ['Pass', 'Fail']
    sizes = [pass_count, fail_count]

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['grey', 'lightblue'])
    plt.title('Pass/Fail Ratio')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def main():
    filename = 'students.csv'
    student_data = read_student_data(filename)
    gender_pie_chart(student_data)
    marks_pie_chart(student_data)

if __name__ == "__main__":
    main()