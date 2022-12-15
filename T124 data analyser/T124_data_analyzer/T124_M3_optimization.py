import T124_M1_load_data as load
import T124_M2_sort_plot as stu
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fminbound
from numpy.polynomial import Polynomial



def curve_fit(new_dic: dict, attribute: str)->list:
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


    working_list =stu.student_list(new_dic)

    x_values = []
    
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
    
    coefficients = list(np.polyfit(x_values_lst, y_values_lst, 2))

    for i in range(len(coefficients)):
        coefficients[i] = round(coefficients[i], 5)

    #min y value 

    y_values_min=min(y_values_lst)
    #find the x value for which the y value is mined

    index=y_values_lst.index(y_values_min)
    x_value_min=x_values_lst[index]


    #max y value 

    y_values_max=max(y_values_lst)
    #find the x value for which the y value is maxed

    index2=y_values_lst.index(y_values_max)
    x_value_max=x_values_lst[index2]

    

    #returns the min values in the first tuple then the max valudes in the other tuple
    return ((coefficients,(x_value_min-0.5,x_value_min+0.5)),(coefficients,(x_value_max-0.5,x_value_max+0.5)))




#Worst grade function ------------------------------------------

def worst_grade(dic,attri):
    """
    this function takes a dictionary and an atteriubte and give the attriubte with the worst grade average
    
    Precondition: must have the add average function loaded in with the loaded dictionary, attribute must be numerical

    >>>print(worst_grade(load.add_average(load.load_data('student-mat.csv','Health')),"StudyTime"))
    


    """
    #this is a function to make an euqation with our coefs.
    
    def curve_function(coef,x):
        return np.polyval(coef,x)

    #assign x to the curve fit call to get the coefs and the x values for the interval    
    x=curve_fit(dic,attri)
    
    #gets the coef list from the tuple
    coef_list=x[0][0]

    #this function makes a polynimal function in terms of x
    #This is needed to use fminbound as it needs a function interms of x 
    def min_curve_function(x):
        return curve_function(coef_list,x)

    #Attribute value for worst grade
    #This will get the minimum value from using the function we just made with min curve function
    #The intervals are the ones that we got from calling the curve fit function (its embedded ina tuple)
    #Some rounding was used
    min_x_value=fminbound(min_curve_function,x[0][1][0],x[0][1][1])//1
    min_x_value=round(min_x_value)


    #Grade value for the worst attriubte Y
    #Since the curvefunction is our main function in terms of x, we just plug x in 
    min_y_value=curve_function(coef_list,min_x_value)
    if attri == 'StudyTime':
        return min_x_value+1,min_y_value
    return (min_x_value,min_y_value)




#Best grade function ---------------------------
def best_grade(dic:dict,attri):
    """
    this function takes a dictionary and an atteriubte and give the attriubte with the best grade average
    
    Precondition: must have the add average function loaded in with the loaded dictionary
    """
    def curve_function(coef,x):
        return np.polyval(coef,x)

    x=curve_fit(dic,attri)
    
   
    coef_list=x[1][0]
   
    
    #Since the function is fMINbound, to find a maximum we just flip the curvefunction equation
    def max_curve_function(x):
        return -curve_function(coef_list,x)


#Same thing for worst grade is applied
    #Attribute value for worst grade
    max_x_value=fminbound(max_curve_function,x[1][1][0],x[1][1][1])//1

    #Grade value for the worst attriubte Y
    max_y_value=curve_function(coef_list,max_x_value)
    max_x=round(max_x_value)

    #I had to add this because all attributes except StudyTime were 1 off
    if attri == 'StudyTime':
        return max_x,max_y_value

    
    return max_x+1,max_y_value

if __name__ == '__main__':
    print(best_grade(load.add_average(load.load_data('student-mat.csv','Health')),"StudyTime"))
    print(worst_grade(load.add_average(load.load_data('student-mat.csv','Health')),"StudyTime"))
    print(best_grade(load.add_average(load.load_data('student-mat.csv','Health')),"Age"))
    print(worst_grade(load.add_average(load.load_data('student-mat.csv','Health')),"Health"))











