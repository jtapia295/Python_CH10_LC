


from re import I


def reverse_characters(string1):
    #string1 = string1[::-1]
    string1 = list(string1)
    string1.reverse()
    string1 = ''.join(string1)
    return string1
    
def reverse_digits(num1):
    if type(num1) == int or type(num1) == float:
        num1 = str(num1)
        num1 = list(num1)
        num1.reverse()
        num1 = ''.join(num1)
        num1 = float(num1) if '.' in num1 else int(num1)
        return num1
    else:
        return "Invalid argument passed, Expecting: type float or Int"


def reverse_list_all(given_list):
    if type(given_list) == list:
        for index in range(len(given_list)):
            if type(given_list[index]) == str:
                given_list[index] = reverse_characters(given_list[index])
            elif type(given_list[index]) == int or type(given_list[index]) == float:
                given_list[index] = reverse_digits(given_list[index])
    #list(given_list).reverse()
    return given_list
    


my_list = ['hell0', 'world', 12.3, 'orange', 987]
second_list = [123, 8897, 4.2, 1138, 8675309]
third_list = ['sdroW dezilatipaC', 'otatop', 'elppa']

print(reverse_list_all(my_list))
print(reverse_list_all(second_list))
print(reverse_list_all(third_list))



#Bonus Mission 

def change_the_phrase(string2):
    modified_string = None
    if len(string2) <= 3:
        modified_string = string2[-1:]
    elif len(string2) > 3:
        modified_string = string2[:3]
    return "We put the {} in {}".format(modified_string,string2)    
    
print(change_the_phrase('Hello'))



def calculate_rectangle_area(length,width = None):
    if type(length) == int and type(width) == int:
        area = length*width
    elif width == None:
        area = length**2
    return area

rectangle_width = 25
rectangle_length = 50
rectangle_area = calculate_rectangle_area(rectangle_length,rectangle_width)


square = 15
square_area = calculate_rectangle_area(square)
print(f"The area of your rectangle is: {rectangle_area}")
print(f"The area is {square_area}cm^2")