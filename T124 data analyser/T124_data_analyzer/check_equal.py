#Jayven larsen ID:101260364

#Jayven larsen
#Student ID: 101260364

#Ghadi Nehme
#Student ID: 101270596

#Theron Rancourt 
#Student ID: 101273142

#Nathan J. Graciano
#Student ID: 101267759


import string
import time

#Ghadi Nehme
#Student ID: 101270596  
def check_equal(filename:str,dic1:dict,dic2:dict,dic3:dict,dic4:dict)->str:
    """
    This function is a large test file testing various items from the load data dictionaries
    It check for correct dictionary keys, correct sized list, correct indiviual
    student entries.
    It also tests in depth the add average function making it worked and modifed
    the dictionaries properly. It will test for the amount of the dictionaries,
    check if the "G_avg" key has been inserted into each students info, and 
    finally check to see if the average grade is correct.
    
    Preconditions: all files must be in the same folder, for calling this function,
    the dictionaries have to be in a certain order such as: dic 1: school key,
    dic 2: health key, dic 3: age key and dic 4: failures key
    
    >>> ce.check_equal('student-mat.csv',student_school_dictionary,student_health_dictionary,student_age_dictionary,student_failures_dictionary)
    
    Test key function:
    
    School Dictionary: PASSED, 5 items tested out of 5, 0 items failed.
    Health Dictionary: PASSED, 10 items tested out of 10, 0 items failed.
    Age Dictionary: PASSED, 18 items tested out of 18, 0 items failed.
    Failures Dictionary: PASSED, 22 items tested out of 22, 0 items failed.
    ---------------------------------
    Test average function:
    
    Add average tests passed for all dictionaries, 4740 items tested
    ---------------------------------
    Test value type function:
    
    Checking School...
    Checking Health...
    Checking Age...
    Checking Failures...
    
    All Dictionaries passed, 32 items tested
    
    ---------------------------------
    Test student amount function:
    
    number of students in student_age_dictionary['15'] PASSED
    ------
    number of students in student_health_dictionary['3'] PASSED
    ------
    number of students in student_age_dictionary['15'] PASSED
    ------
    number of students in student_failures_dictionary['2'] PASSED
    ------
    4 test cases passed, 0 tests cases failed
    ---------------------------------

    
    """
    dictionary_names=['School','Health','Age','Failures']
    dictionary_lst=[]
    dictionary_lst.append(dic1)
    dictionary_lst.append(dic2)
    dictionary_lst.append(dic3)
    dictionary_lst.append(dic4)
    
    
    
    print("\nTest key function:\n")
    actualkeys=[{'GP', 'MB', 'CF', 'BD', 'MS'},{'1','2','3','4','5'},
                {'15', '16', '17', '18', '19', '20', '21', '22'},{'0', '1', '2', '3'}]
    
    tests_failed = 0
    tests_passed = 0
    test_counts = 0
    count=0
    for i in range (len(dictionary_lst)):
        
        dic_keys=[]
        for keys in dictionary_lst[i].keys():
            dic_keys.append(keys)
            
        
        for keys in dic_keys:
            if keys in actualkeys[count]:
                tests_passed += 1
                test_counts+=1
                
            else:
                tests_failed += 1
                test_counts+=1
        count+=1   
        if tests_passed == test_counts:
            print(dictionary_names[i],"Dictionary: PASSED,",tests_passed,"items tested out of "+str(test_counts)+",",tests_failed,'items failed.')
        elif tests_passed !=test_counts:
            print("FAILED: Some or All" , str(dictionary_lst[i].keys())
                  + " are not in the expected set values")
    print("---------------------------------")




#---------------------------------------------------------------


#CHECK EQUAL TEST
#Jayven larsen
#Student ID: 101260364

    print("Test average function:\n")
    passed=[]
    
    for dics in range (len(dictionary_lst)):
        
        in_file = open(filename, "r")
        sample_file = in_file.readlines()[1:] 
        students=[]
        for items in sample_file:
            rows = items.split(',')
            students.append(rows)
        expected = len(students)
        student_in_dic=[]
        
        #Test 1
        for keys in dictionary_lst[dics]:
            for i in dictionary_lst[dics][keys]:    
                student_in_dic.append(i)
        amount_students = len(student_in_dic)
        if amount_students != expected:
            print("Test 1 FAILED: expected "+expected+", got "+amount_students+".")
                  
        else:
            passed.append(1)
        
        
        #Test 2  
    
        counter =0
        for keys in dictionary_lst[dics]:
            for i in dictionary_lst[dics][keys]:
                if 'G_avg' in i:
                    counter +=1
                else:
                    continue
        if counter != expected:
            print("Test  FAILED: expected "+str(expected)+", got "+str(dictionary_lst[dics])+".")
        else:
            passed.append(1)
        
        #Test 3
        G1=[]
        G2=[]
        G3=[]
        avg=[]
        student_counter=0
        for items in sample_file:
            rows = items.split(',')
            G1.append(int(rows[6]))
            G2.append(int(rows[7]))
            G3.append(int(rows[8].strip('\n')))
            g_avg = ((G1[student_counter] + G2[student_counter] + G3[student_counter]) / 3).__round__(2)
            avg.append(g_avg)
            student_counter+=1
        correct=0
        for key in dictionary_lst[dics]:
            for student in dictionary_lst[dics][key]:
                if student['G_avg'] in avg:
                    correct+=1
        if correct == len(avg):
            
            passed.append(1)
        else:
            print("Test 3:", correct, "FAILED")
        
        total_counter=correct+counter+amount_students
    if len (passed)==12:
        
        print("Add average tests passed for all dictionaries,", str(total_counter*4),'items tested')
    print("---------------------------------")
        
#-----------------------------------------------------
#Nathan Graciano
#101267759


    print("Test value type function:")
    #which_dic.lower()
   
    school = (dic1)#('student-mat.csv'))
    health = (dic2)#('student-mat.csv'))
    age = (dic3)#('student-mat.csv'))
    fail = (dic4)#('student-mat.csv'))
   
    header_lst_schoo = ['Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3']
    header_lst_health = ['School', 'Age', 'StudyTime', 'Failures', 'Absences', 'G1', 'G2', 'G3']
    header_lst_age = ['School', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3']
    header_lst_fail = ['School', 'Age', 'StudyTime', 'Health', 'Absences', 'G1', 'G2', 'G3']
    #
    expected_type_school = ["'str'", "'int'", "'int'", "'int'", "'int'", "'int'", "'int'", "'int'"]
    expected_type_health = ["'str'", "'str'", "'int'", "'int'", "'int'", "'int'", "'int'", "'int'"]
    expected_type_age = ["'str'", "'int'", "'int'", "'int'", "'int'", "'int'", "'int'", "'int'"]
    expected_type_fail = ["'str'", "'str'", "'int'", "'int'", "'int'", "'int'", "'int'", "'int'"]
   
    count_pass = 0
   
    #School--------------------------------------------------
    
    print('\nChecking School...')
      
    checklist = []
    for item in header_lst_schoo:
        x = type(dic1["GP"][0][item])
        string_x = str(x)
        y = string_x.strip("<class> ")
        checklist.append(y)
         
    ctr = 0
    for i in checklist:
        if i == expected_type_school[ctr]:
            count_pass += 1
        else:
            print('Fail')
        ctr += 1
        
   
    #Health---------------------------------------------------
    
    print('Checking Health...')
    checklist = []
    for item in header_lst_health:
        x = type(health["1"][0][item])
        string_x = str(x)
        y = string_x.strip("<class> ")
        checklist.append(y)
       
         
    ctr = 0
    for i in checklist:
        if i == expected_type_health[ctr]:
                
            count_pass += 1
        else:
            print('Fail')
        ctr += 1
       
    #Age------------------------------------------------------
    
    print('Checking Age...')
      
    checklist = []
    for item in header_lst_age:
        x = type(age["15"][0][item])
        string_x = str(x)
        y = string_x.strip("<class> ")
        checklist.append(y)
      
    ctr = 0
    for i in checklist:
        if i == expected_type_age[ctr]:

            count_pass += 1
        else:
            print('Fail')
        ctr += 1
        
    #Failures------------------------------------------------
    
    print('Checking Failures...')
      
    checklist = []
    for item in header_lst_fail:
        x = type(fail["3"][0][item])
        string_x = str(x)
        y = string_x.strip("<class> ")
        checklist.append(y)
      
    ctr = 0
    for i in checklist:
        if i == expected_type_fail[ctr]:

            count_pass += 1
        else:
            print('Fail')
        ctr += 1
    if count_pass==32:
        print("\nAll Dictionaries passed,", str(count_pass), "items tested\n")
    print("---------------------------------")
    
    
    
#-------------------------------
#Theron Rancourt
#101273142


    def check_equal(description: str, actual, expected) -> None:

        actual_type = type(actual)
        expected_type = type(expected)
        
        if actual_type != expected_type:
            
            print("{0} FAILED: expected ({1}) has type {2}, " \
                  "but actual ({3}) has type {4}".
                  format(description, expected, str(expected_type).strip('<class> '), 
                          actual, str(actual_type).strip('<class> ')))
        elif actual != expected:
            print("{0} FAILED: expected {1}, got {2}".
                  format(description, expected, actual))
        else:
            print("{0} PASSED".format(description))
        print("------")





    
    print('Test student amount function:\n')
    
    failed = 0
    passed = 0

    #test cases for all dictionary functions
    check_equal('number of students in student_age_dictionary[\'CF\']', len(dic1['CF']), 80)
    if len(dic1['CF']) == 80:
        passed +=1
    else:
        failed +=1
    check_equal('number of students in student_health_dictionary[\'3\']', len(dic2['3']), 91)
    if len(dic2['3']) == 91:
        passed +=1
    else:
        failed +=1    
    check_equal('number of students in student_age_dictionary[\'15\']', len(dic3['15']), 82) 
    if len(dic3['15']) == 82:
        passed +=1
    else:
        failed +=1    
    check_equal('number of students in student_failures_dictionary[\'2\']', len(dic4['2']), 17)
    if len(dic4['2']) == 17:
        passed +=1
    else:
        failed +=1  
    
    #Number of tests run, and the number of cases that passed/failed    
    
  
    print( str(passed) + ' test cases passed, ' + str(failed) + ' tests cases failed')
    
    print("---------------------------------")
   
           
