import T124_M1_load_data as load
import T124_M2_sort_plot as sort
import T124_M3_optimization as minmax

load_data_conf=False

batch_file= open(input('Enter the name of the file where your commands are stored: '))

for lines in batch_file:
    counter=0
    commands_lst = lines.strip("\n").split(";")


    user_input = commands_lst[counter]
    counter+=1
    if user_input == "L":
        file_input = commands_lst[counter]
        counter+=1
        attribute_input= commands_lst[counter]
        loaded_data=load.add_average(load.load_data(file_input,attribute_input))
        counter+=1
        
        print("Data loaded")
        load_data_conf = True

    elif user_input == 'S':
        
        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))
            attribute_input2 = commands_lst[counter]
            counter+=1
            
            sorted_data=sort.sort_students_selection(loaded_data,attribute_input2)
            print('data sorted')
            
            print_input=commands_lst[counter]
            counter+=1
            if print_input == 'Y':
                print(sorted_data)
                
            elif print_input == 'N':
                None
    elif user_input== 'H':
        
        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))
            attribute_input3 =commands_lst[counter]
            counter+=1
            print("Data graphed.")
            print_input=commands_lst[counter]
            counter+=1
            if print_input == 'Y':
                sort.histogram(loaded_data,attribute_input3)
                
            elif print_input == 'N':
                None
            
    

    elif user_input == "B":

        if load_data_conf == True:
            loaded_data=load.add_average(load.load_data(file_input,attribute_input))
            attribute_input4 = commands_lst[counter]
            counter +=1
            
            best=minmax.best_grade(loaded_data,attribute_input4)
            print(f"The Best value for the attribute {attribute_input4} is {best[0]}")

    elif user_input == "W":
        loaded_data=load.add_average(load.load_data(file_input,attribute_input))
        if load_data_conf == True:
            attribute_input4 = commands_lst[counter]
            counter+=1
            
            best=minmax.worst_grade(loaded_data,attribute_input4)
            print(f"The Worst value for the attribute {attribute_input4} is {best[0]}")



    else:
        print("invalid option")
        






    



