#Jayven larsen
#Student ID: 101260364

#Ghadi Nehme
#Student ID: 101270596

#Theron Rancourt 
#Student ID: 101273142

#Nathan J. Graciano
#Student ID: 101267759




def student_school_dictionary(data: str) -> dict:
    """
    This functions takes a .csv file and reads through it. It will sort through
    its contents and assign students according to their school. Each student 
    will have their own dictionary with specific information assigned to them.
    
    >>> {'GP': [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3',
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, ... other students..}]}
    >>> 'BD': [{'Age': '18', 'StudyTime': '2', 'Failures': '1', 'Health': '2', 
    'Absences': '0', 'G1': '7', 'G2': '7', 'G3': '0'}, ... other students..}]}
    
    preconditions: file has to be to of .csv type, .csv file must be in the same location as program
    
    """
    in_file = open(data, "r")
    stud_file = in_file.readlines()[1:]
    
    
    #next(stud_file)
        # This skips the first line because its the headers

    student_info_list = []
        # This list holds all info of each student

    key_list = []
        # this holds the school key for each student

    school_key_set = set()
        # This will delete all the duplicate keys for the empty dictionary

    counter = 0
        # this counter is used for itteration counting

    main_dic = {}
        # this is the main dictionary

    for line in stud_file:
        row = line.split(',')

        school_key_set.add(row[0])
            # this is what adds the keys to the set (the keys are stored in row 0

        for keys in school_key_set:
            main_dic[keys] = []
            # creates an empty dictionary with the keys and empty list as values

        student_info = {
            'Age': row[1],
            'StudyTime': int(row[2]),
            'Failures': int(row[3]),
            'Health': int(row[4]),
            'Absences': int(row[5]),
            'G1': int(row[6]),
            'G2': int(row[7]),
            'G3': int(row[8].strip('\n')),
            }
            # This is the information being collected, each row is a piece of info in the doc

        key_list.append(row[0])
            # This is the function that adds all the keys to key_list

        student_info_list.append(student_info)
        # This is the line that adds the collected student info in the student_info_list

    for stu_key in key_list:
        if stu_key in main_dic.keys():  # Checks if the key is in the dictionary
            main_dic[stu_key] += [student_info_list[counter]]
                # This adds the student information to the correct key
                # The counter is used here as an index because this is all interated in a for loop
                # Meaning the first student will be student_info_list[0], and then the next line
                # adds one. In the next iteration it will add the second student in the list Student_info_list[1],
                # The for loop loops though all the keys in the key_list
                # Because the keys appended for each student, it will be on the same itteration as the counter
            counter += 1
        else:
            print('error')

    return main_dic
#student_school_dictionary('student-mat.csv')

def student_health_dictionary(data: str) -> dict:
    """
    This functions takes a .csv file and reads through it. It will sort through
    its contents and assign students according to their school. Each student 
    will have their own dictionary with specific information assigned to them.
    
    preconditions: file has to be to of .csv type, .csv file must be in the same location as program
    
    Test Cases:
    ('1', [{'School': 'GP', 'Age': '17', 'StudyTime': '2', 'Failures': '0', 'Absences': '6', 'G1': '6', 'G2': '5', 'G3': '6'},...)
    
   ('2', [{'School': 'GP', 'Age': '15', 'StudyTime': '2', 'Failures': '0', 'Absences': '10', 'G1': '10', 'G2': '8', 'G3': '9'},...)
    
    
    """
    in_file = open(data, "r")
    
    #header = in_file.readlines()[0:]
    
    stud_file = in_file.readlines()[1:]


    student_info_list = []

    key_list = []

    school_key_set = set()

    counter = 0

    main_dic = {}

    for line in stud_file:
        row = line.split(',')

        school_key_set.add(row[4])

        for keys in school_key_set:
            main_dic[keys] = []

        student_info = {
            'School': row[0],
            'Age': row[1],
            'StudyTime': int(row[2]),
            'Failures': int(row[3]),
            'Absences': int(row[5]),
            'G1': int(row[6]),
            'G2': int(row[7]),
            'G3': int(row[8].strip('\n')),
        }

        key_list.append(row[4])

        student_info_list.append(student_info)

    for stu_key in key_list:
        if stu_key in main_dic.keys():  # Checks if the key is in the dictionary
            main_dic[stu_key] += [student_info_list[counter]]
            counter += 1
        else:
            print('error')

    #dic = student_health_dictionary('student-mat.csv')
    sorted_dic = dict(sorted(main_dic.items()))

    return sorted_dic

#student_health_dictionary('student-mat.csv')


def student_age_dictionary(data: str) -> dict:
    """
    This functions takes a .csv file and reads through it. It will sort through
    its contents and assign students according to their school. Each student 
    will have their own dictionary with specific information assigned to them.
    
    Preconditions: file has to be of .csv format.
                   'student-mat.csv' must be in the same directory as the function
                   
      >>> 
      { 15 : [ {'School':student_age_dictionary('student-mat.csv') 'GP', 
      'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6,
      'G1': 7, 'G2': 8, 'G3': 10}, {another element}, … ], 
      16 : [ {'School': 'MS', 'StudyTime': 1,'Failures': 1.2, 'Health': 4,
      'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7}, {another element}, … ],
      … }
    """
    in_file = open(data, "r")
    stud_file = in_file.readlines()[1:]
    
        

    student_info_list = []
       

    key_list = []
        

    age_key_set = set()
        

    counter = 0
        

    main_dic = {}
        

    for line in stud_file:
        row = line.split(',')
        age_key_set.add(row[1])
            

        for keys in age_key_set:
            main_dic[keys] = []
            
        student_info = {
            'School': row[0],
            'StudyTime': int(row[2]),
            'Failures': int(row[3]),
            'Health': int(row[4]),
            'Absences': int(row[5]),
            'G1': int(row[6]),
            'G2': int(row[7]),
            'G3': int(row[8].strip('\n')),
            }
            

        key_list.append(row[1])
            

        student_info_list.append(student_info)
        
    for stu_key in key_list:
        if stu_key in main_dic.keys():  
            main_dic[stu_key] += [student_info_list[counter]]
            counter += 1
        else:
            print('error')
            
    #sort the dictionary's age keys in acending order
    sorted_dic = dict(sorted(main_dic.items()))
    return sorted_dic

#student_age_dictionary('student-mat.csv')

def student_failures_dictionary(data: str) -> dict:
    """
    This function takes a .csv file and reads through it. When its done reading
    , it will assign studens according to the amount of times they were absent. After executing,
    the code will assign all the information corresponding to the absences and list
    them in a dictionary.
    
    
    
    Preconditions: file must be .csv, .csv file must be in the same location as the program, 
    >>> student_failures_dictionary('student-mat.csv')
    {'0': [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another student}...}
    """
    in_file = open(data, "r")
    stud_file = in_file.readlines()[1:]

    student_info_list = []
        

    key_list = []
        
    school_key_set = set()
        
    counter = 0
       
    main_dic = {}
       

    for line in stud_file:
        row = line.split(',')

        school_key_set.add(row[3])
           

        for keys in school_key_set:
            main_dic[keys] = []
           
        student_info = {
            "School":row[0],
            'Age': int(row[1]),
            'StudyTime': int(row[2]),
            'Health': int(row[4]),
            'Absences': int(row[5]),
            'G1': int(row[6]),
            'G2': int(row[7]),
            'G3': int(row[8].strip('\n')),
            }
           
        key_list.append(row[3])
           

        student_info_list.append(student_info)
        
    for stu_key in key_list:
        if stu_key in main_dic.keys():  
            main_dic[stu_key] += [student_info_list[counter]]
            counter += 1
        else:
            print('error')
            
    #dic = student_failures_dictionary('student-mat.csv')
    sorted_dic = dict(sorted(main_dic.items()))
    return sorted_dic

#student_failures_dictionary('student-mat.csv')



def load_data(file_name: str, type_dictionary: str) -> dict:
    """ 
    This function takes user input to decide which function will be used to load data 
    

    Preconditions: file must be .csv, .csv file must be in the same location as the program, 
"""
    if type_dictionary == 'School':
        return student_school_dictionary(file_name)
    elif type_dictionary == 'Health':
        return student_health_dictionary(file_name)
    elif type_dictionary == 'Age':
        return student_age_dictionary(file_name)
    elif type_dictionary == 'Failures':
        return student_failures_dictionary(file_name)
    
    
def add_average(dictoinary) -> dict:
    """
    This function will take G1, G2 and G3 and create an average grade from the 3 values. 
    This new value will then be added to that student's dictionary.
    
    >>>add_average(load_data('student-mat.csv','Failures'))
    {'0': [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6', 'G_avg': 5.67}, {another student}...,
    
    """    
    G1 = []
    G2 = []
    G3 = []
    student_counter = 0
    for keys in dictoinary:
        for i in dictoinary[keys]:
            G1.append(i['G1'])
            G2.append(i['G2'])
            G3.append(i['G3'])
            avg = ((G1[student_counter] + G2[student_counter] + G3[student_counter]) / 3)
            i['G_avg'] = avg.__round__(2)
            student_counter += 1
    return dictoinary

    


if __name__ == '__main__':
    student_school_dictionary = load_data("student-mat.csv","School")

    student_school_dictionary = add_average(student_school_dictionary)

    student_health_dictionary = load_data("student-mat.csv","Health")
    student_health_dictionary = add_average(student_health_dictionary)

    student_age_dictionary = load_data("student-mat.csv","Age")
    student_age_dictionary = add_average(student_age_dictionary)

    student_failures_dictionary = load_data("student-mat.csv","Failures")
    student_failures_dictionary = add_average(student_failures_dictionary)




