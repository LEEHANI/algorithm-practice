def gradingStudents(grades):

    answer=[]
    for origin in grades:
        final_grade = ((origin//5)+1)*5
        
        if final_grade >= 40 and (final_grade-origin < 3):
            answer.append(final_grade)
        else:
            answer.append(origin) 
    return answer   

print(gradingStudents([73,67,38,33]))