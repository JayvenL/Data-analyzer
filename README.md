# Data-analyzer

### T124_data_analyser version 1.0

---

Date: 2022-12-07

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

## Project Description

---

This application takes data from a spreadsheet and manipulates it through sorting, plotting, and optimization.

## Installation

---

Install the package manager [pip](https://pip.pypa.io/en/stable/) (version 22.3.1):

```
pip python -m pip install -U pip
```

Use pip to install the following libraries:

Matplotlib (version 3.6.2)
```
pip install matplotlib
```

Numpy (version 1.23.5)
```
pip install numpy
```

Scipy (version 1.9.3)
```bash
pip install scipy
```

## Usage

---

Open a python IDE of your choice (PyCharm or Wing 101).

NOTE: The data file and T124_data_analyser MUST be in the same directory.

There are two possible ways of running this application:
1. Through text UI
2. Through batch UI

##### Text UI method 
Open and run T124_text_UI. The shell displays a list of commands and prompts the user to enter one:

```
The available commands are:
    1. L)oad Data
    2. S)ort Data
    'School' 'Age' 'StudyTime' 'Failures' 'Health'
     'Absences' 'G1' 'G2' 'G3' 'G_Avg'
    3. H)istogram
     'School' 'Age' 'StudyTime' 'Failures' 'Health'
     'Absences'
    4. W)orst _____ for Grades
     'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    5. B)est _____ for Grades
     'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    6. Q)uit
    
Please type your command:<one space>
```

The filename of the data is entered.
```
Please enter the name of the file: <the user enters response>
```

The attribute to perform analysis on is entered.
```
Please enter the attribute you want to use as key:
'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
'G1' 'G2' 'G3' 'G_Avg'
: <the user enters response>
```

The data is loaded and displayed. The user is prompted to enter more commands or quit.
```
Data loaded
<The data is displayed>
<The UI in figure 1 is displayed>
```

##### Batch UI method 

A text file is created with all desired commands, separated by a semicolons:

ex.
L;student-mat.csv
S;Health;N
B;Age
W;Health
H;StudyTime

Open and run T124_batch_UI. The user is prompted to enter the file name in which their commands are stored.

```
Enter the name of the file where your commands are stored:
test.txt

# returns:
Data loaded
Data sorted. <<<You selected not to display>>>
The best value for the attribute Age is 15 years old
The worse value for the attribute Health is 1
<<<Histograms with Study time will be shown>>>
```

## Credits

---

##### Lab 3
#
| Function | Author(s) |
| ----------- | ----------- |
| student_school_dictionary | Jayven Larsen |
| student_health_dictionary | Nathan Graciano |
| student_age_dictionary | Theron Rancourt |
| student_failures_dictionary | Ghadi Nehme |
| load_data | Jayven Larsen |
| add_average | Jayven Larsen |

##### Lab 4
#
| Function | Author(s) |
| ----------- | ----------- |
| check_equal | Theron Rancourt, Jayven Larsen  |

##### Lab 5
#
| Function | Author(s) |
| ----------- | ----------- |
| student_list | Jayven Larsen, Nathan Graciano |
| sort_students_selection| Jayven Larsen |
| sort_students_bubble | Theron Rancourt |
| curve_fit | Nathan Graciano, Jayven Larsen | 
| histogram |  Ghadi Nehme, Jayven Larsen | 

##### Lab 6
#
| Function/module | Author(s) |
| ----------- | ----------- |
| minimum | Theron Rancourt, Jayven Larsen | 
| maximum | Nathan Graciano,Jayven Larsen | 
| text user interface | Jayven Larsen |
| batch user interface | Jayven Larsen |

## Contact

---

T124_data_analyser can be reached at: jayvenlarsen04@gmail.com // +1 6137154481
Jayven Larsen

## License

---

[MIT License](https://choosealicense.com/licenses/mit/)

