from time import perf_counter


def percent(marks):
    return (((marks[0] + marks[1] + marks[2] + marks[3]))/400) * 100

numberOfStudents1 = [45, 78, 86, 77]
percentageOne = percent(numberOfStudents1)

numberOfStudents2 = [75, 98, 88, 78]
percentageTwo = percent(numberOfStudents2)

print(percentageOne,", ",percentageTwo)