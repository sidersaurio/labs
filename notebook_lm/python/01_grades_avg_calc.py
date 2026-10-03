def run():
    name = input('Welcome to the Regional Education System, identify yourself: ')
    print(f'Welcome {name}')
    grades = []
    for i in range(3):
        grade = float(input(f'Introduce your grade for Test #{i+1}: '))
        grades.append(grade)
    counter = 0
    for i in range(len(grades)):
        counter += grades[i]
    average = round(counter/len(grades), 2)
    print(f'{name} your average grade for the tests is: {average}')

if __name__ == '__main__':
    run()