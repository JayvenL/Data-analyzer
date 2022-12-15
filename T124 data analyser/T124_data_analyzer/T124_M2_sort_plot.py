#Jayven Larsen
#101260364

#Nathan J. Graciano
#101267759

#Theron Rancourt 
#101273142

#Ghadi Nehme
#101270596

import T124_M1_load_data as load
import numpy as np
import matplotlib.pyplot as plt

#Student list----------------------------------------------------------------

def student_list (load_data_dic:dict)->list:
    """
    This function takes a student dictionary loaded up from the load data module
    and it converts the dictionary to a large list of students. 
    
    >>>student_list(load.student_failures_dictionary)
    [{'School': 'GP', 'Age': '18', 'StudyTime': 2, 'Health': 3, 
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_avg': 5.67, 'Failures': '0'}, 
    {'School': 'GP', 'Age': '17', 'StudyTime': 2, 'Health': 3, 
    'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_avg': 5.33, 'Failures': '0'},....]
  
    >>>student_list(load.add_average(load.load_data('student-mat.csv','School')))
    
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, '
    Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_avg': 8.33, 'Age': '15'}, 
    {'School': 'GP', 'StudyTime': 3, 'Failures': 0, 'Health': 5, 
    'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15, 'G_avg': 14.67, 'Age': '15'}.....]
         
    Predoncition: aall imported files must be in the same folder

    """
    student=[]
    if load_data_dic == load.add_average(load.load_data('student-mat.csv','School')):
        for key in load_data_dic:
            for students in load_data_dic[key]:
                students["School"] = key
                student.append(students)
    elif load_data_dic == load.add_average(load.load_data('student-mat.csv','Health')):
        for key in load_data_dic:
            for students in load_data_dic[key]:
                students["Health"] = key
                student.append(students)        
    elif load_data_dic == load.add_average(load.load_data('student-mat.csv','Age')):
        for key in load_data_dic:
            for students in load_data_dic[key]:
                students["Age"] = int(key)
                student.append(students)
    elif load_data_dic == load.add_average(load.load_data('student-mat.csv','Failures')):
        for key in load_data_dic:
            for students in load_data_dic[key]:
                students["Failures"] = key
                student.append(students)        
                        
                
                
        
    return student

#Selection sort-------------------------------------------------------

def sort_students_selection(dic:dict,attri:str)->dict:

    """
    This function will apply a selection sort algorithym to the dictionary
    inputed as an argument.

    >>>sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'Age')
    [{'Age': '15', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 
    'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_avg': 8.33, 'School': 'GP'},
     {'Age': '15', 'StudyTime': 3, 'Failures': 0, 'Health': 5, 
     'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15, 'G_avg': 14.67, 'School': 'GP'}...]

     >>>sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'School')
     [{'Age': '18', 'StudyTime': 2, 'Failures': 1, 'Health': 2, 
     'Absences': 0, 'G1': 7, 'G2': 7, 'G3': 0, 'G_avg': 4.67, 'School': 'BD'},
     {'Age': '17', 'StudyTime': 2, 'Failures': 0, 'Health': 5, 
     'Absences': 14, 'G1': 12, 'G2': 12, 'G3': 12, 'G_avg': 12.0, 'School': 'BD'}...],

     Predoncition: all attributes start with a capital letter, all imported files must be in the same folder
    """
    dictionary=student_list(dic)

    for i in range (len(dictionary)):
        min_idx = i
        for j in range (i+1, len(dictionary)):
            if dictionary[min_idx][str(attri)] > dictionary[j][str(attri)]:
                min_idx=j
                    
                    
        dictionary[i],dictionary[min_idx]=dictionary[min_idx],dictionary[i]
    
    
    return dictionary

# Buble sort:
def sort_students_bubble(load_data_dic: dict, attribute: str ) -> None:
    """Returns the list of sorted students given a dictionary of data, and sorts the students by the element given in parameter attribute.
    
    Precondition: T124_M1_load_data, student-data.csv, and T124_M2_sort_students_bubble must be in the same directory.
    
    >>>sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'Age')
    [{'School': 'GP', 'Age': '15', 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19, 'Health': '1'}, {other student}, ... 
    {'School': 'BD', 'Age': '22', 'StudyTime': 1, 'Failures': 3, 'Absences': 16, 'G1': 6, 'G2': 8, 'G3': 8, 'Health': '1'}]
    """
    student=[]
    my_list = student_list(load_data_dic)
    swap = True
    while swap:
        swap = False
        for i in range(len(my_list)-1):
            if (my_list[i].get(attribute) > my_list[i+1].get(attribute)):
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swap = True       
    
    
    return my_list


#Curve fit function-----------------------------------------------------------
def curve_fit(new_dic: dict, attribute: str, order: int)->list:
    """
    This function will take a dictionary from the load data module, an attribute from the student 
    informaiton and and order (degree) of a polynomial. It will take the Grade average from the student for each attribute level
    and will create a function based off the degree given by the user

    >>>curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Failures",3)
    [-0.0, 0.355, -2.735, 11.36]
    >>>curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Failures",1)
    [-1.67, 11.005]
    >>>curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"StudyTime",3)
    [-0.35833, 2.66, -5.28167, 13.23]
    
    Predoncition: all attributes start with a capital letter, all imported files must be in the same folder

    
    """

    dic=new_dic
    working_list =student_list(new_dic)

    x_values = []
    y_values = set()
    y_values_lst=[]

    for i in range(len(working_list)):
        x_values.append(working_list[i][attribute])

    x_values = set(x_values)
    
    x_values_lst=[]
    for j in x_values:
        x_values_lst.append(int(j))
        

    for i in x_values:
        grade_sum = 0
        count = 0

        for j in range(len(working_list)):
            if working_list[j][attribute] == i:
                grade_sum += working_list[j]['G_avg']
                count += 1

        new_avg = grade_sum / count
        y_values_lst.append(round(new_avg, 2))
    
    if order > len(x_values_lst) - 1:
        order = len(x_values_lst) - 1
        coefficients = list(np.polyfit(x_values_lst, y_values_lst, order))
    else:
        coefficients = list(np.polyfit(x_values_lst, y_values_lst, order))

    for i in range(len(coefficients)):
        coefficients[i] = round(coefficients[i], 5)

    return coefficients


#Histogram
def histogram(dic:dict,attri:str):
    """
    This function will create a histogram based off any load data dictiony and any attribute from the dictionnary
    It plots the amount of students for each attribute level
    This funcion will print a bar diagram

    >>>istogram(load.add_average(load.load_data('student-mat.csv','School')),"School")
    None
    >>>istogram(load.add_average(load.load_data('student-mat.csv','School')),"School")
    None

    Predoncition: all attributes start with a capital letter, all imported files must be in the same folder

    """

    student_lst=student_list(dic)

    attri_list=[]
    for students in student_lst:
        attri_list.append(students[attri])

    fig= plt.figure()
    x=plt.xlabel(attri)
    y=plt.ylabel("Number of students")
    
    x_v_lst=[]
    x_v_set=set()
    for x in attri_list:
        x_v_set.add(x)
    for i in x_v_set:
        x_v_lst.append(i)
        
    
    count_lst=[]
    
    for i in range(len(x_v_lst)):
        x=attri_list.count(x_v_lst[i])
        count_lst.append(x)
        
    
       
    bar=plt.bar(x_v_lst,count_lst)
    
    plt.show()


#Function calls------------------------------------------------------------
if __name__ == "__main__":
    #1) Student list:
    
    student_list(load.add_average(load.load_data('student-mat.csv','School')))
    student_list(load.add_average(load.load_data('student-mat.csv','Age')))
    student_list(load.add_average(load.load_data('student-mat.csv','Failures')))
    student_list(load.add_average(load.load_data('student-mat.csv','Health')))

    #2) Selection sort

    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'School')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'Age')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'Health')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'StudyTime')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'Absences')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'G1')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'G2')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'G3')
    sort_students_selection(load.add_average(load.load_data('student-mat.csv','School')),'G_avg')


    #3) Buble sort
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'School')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'Age')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'Health')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'StudyTime')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'Absences')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'G1')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'G2')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'G3')
    sort_students_bubble(load.add_average(load.load_data('student-mat.csv','School')), 'G_avg')




    #4) Curve fit 

    print(curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Failures",3))
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Failures",1)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Age",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"StudyTime",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Health",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"Absences",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"G1",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"G2",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"G3",3)
    curve_fit(load.add_average(load.load_data('student-mat.csv','School')),"G_avg",3)




    #5) Histogram

    histogram(load.add_average(load.load_data('student-mat.csv','School')),"School")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"Age")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"Health")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"Failures")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"StudyTime")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"Absences")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"G1")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"G2")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"G3")
    histogram(load.add_average(load.load_data('student-mat.csv','School')),"G_avg")




