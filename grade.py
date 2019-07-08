def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 65 <= grade <= 69:
        return "D"
    else:
        return "F"
      
    
print(grade_converter(92))

print(grade_converter(70))

print(grade_converter(61))