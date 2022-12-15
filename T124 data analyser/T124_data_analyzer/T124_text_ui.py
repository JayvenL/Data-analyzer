import T124_M1_load_data as load
import T124_M2_sort_plot as sort
import T124_M3_optimization as minmax




load_data_conf=False
while True:
    print('''
The available commands are: 
    1. L)oad Data
    2. S)ort Data
        'School' 'Age' 'StudyTime' 'Failures' 'Health'
        'Absences' 'G1' 'G2' 'G3' 'G_Avg' 
    3. H)istogram
        'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    4. W)orst _____ for Grades
        'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 
    5.B)est _____forGrades
        'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 
    6. Q)uit
    
    ''')
    user_input = input("Please type your command: ")

    if user_input == "L":
        file_input = input("Please enter the name of the file: ")
        attribute_input= input("Please load the attribute to be used as a key: ")
        loaded_data=load.add_average(load.load_data(file_input,attribute_input))
        
        print("Data loaded")
        load_data_conf = True
    
    elif user_input == 'S':
        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))
            attribute_input2 = input(''' Please enter the attribute you want to use for sorting:
            'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg'
            : ''')
            
            sorted_data=sort.sort_students_selection(loaded_data,attribute_input2)
            
            print_input=input('Data sorted. Would you like to display the data? (Y/N): ')
            if print_input == 'Y':
                print(sorted_data)
                
            elif print_input == 'N':
                None
        else:
            print('Please load a file first')
    elif user_input== 'H':
        
        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))
            attribute_input = input('''Please enter the attribute you want to use for graphing:
            'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
            : ''')
            print("Data graphed.")
            print_input=input('Data graphed. Would you like to display the data? (Y/N): ')
            if print_input == 'Y':
                sort.histogram(loaded_data,attribute_input)
                
            elif print_input == 'N':
                None
        else:
            print('Please load a file first')
            
    elif user_input == "B":

        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))

            attribute_input4 = input('''Please enter the attribute you want to use for graphing:
            'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
            : ''')
            
            best=minmax.best_grade(loaded_data,attribute_input4)
            print(f"The Best value for the attribute {attribute_input4} is {best[0]}")

        else:
            print('Please load a file first')

    elif user_input == "W":

        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))

            attribute_input4 = input('''Please enter the attribute you want to use for graphing:
            'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
            : ''')
            
            best=minmax.worst_grade(loaded_data,attribute_input4)
            print(f"The Worst value for the attribute {attribute_input4} is {best[0]}")

        else:
            print('Please load a file first')
    elif user_input == 'Q':
        break
    else:
        print("invalid option")
        continue

        


    
