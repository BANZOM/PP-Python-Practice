if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    target = student_marks.get(query_name) # get the index of marks
     
    mean = (target[0]+ target[1]+ target[2]) / 3  # finding the mean
    
    result = format( mean , '.2f')  # format the mean according to the need
    
    print(result)
    
    
    
'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.


Sample Input 0:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
    
    
Sample Output 0:

56.00
    
