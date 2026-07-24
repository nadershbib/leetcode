
def first_second(my_list):
    
    max,secondMax = 0,0
    for num in my_list:
        if num > max:
            max,secondMax = num,max
        elif num > secondMax: 
            secondMax = num
    return f"{max} {secondMax}"