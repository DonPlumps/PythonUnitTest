#various functions to test

#calculate BMI
def calc_bmi(weight, height):
    #division by zero error
    if height == 0:
        raise ZeroDivisionError("height must not be zero")

    #negative height/weight error
    if height < 0 or weight < 0:
        raise ValueError("height AND weight must be positive")

    #type error
    if isinstance(weight, float) or isinstance(weight, int):
        if isinstance(height, float) or isinstance(height, int):
            return round(weight / height**2 , 2)
    else:
        raise TypeError("weight and height must be a number")
