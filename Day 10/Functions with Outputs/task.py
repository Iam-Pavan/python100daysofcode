def format_name(f_name,l_name):
    # print(f_name.title())
    formated_f_name = f_name.title()
    # print(l_name.title())
    formated_l_name = l_name.title()

    return f'{formated_f_name} {formated_l_name}'

formated_string = format_name('pavan','ANGELA')
print(formated_string)

def func1(text):
    return text + text
def func2(text):
    return text.title()
output = func2(func1('pavan'))
print(output)

def pra(x,y):
    c=x+y
    return c
# sa = pra(2,7)

# def df(x,y):
#     z = x + y
#     print(z)
# df(sa,10)



