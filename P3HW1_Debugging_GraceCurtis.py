# P3HW1 
# Grace

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if score >= 90:
       print('Your grade is: A')
    elif 90 > score >= 80:
      print('Your grade is: B')
    elif 80 > score >= 70:
          print('Your grade is: C')
    elif 70 > score >= 60:
          print('Your grade is: D')
    else:
      print('Your grade is: F')
    
    # TO DO: finish this







# program start
main()
