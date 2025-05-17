# def new(**n):
#     print(n)
#     print(type(n))
# new(name='komal', age=21 , quali='btech')    


def new(**kwargs):
    for k,v in kwargs.items():
        print(f'my key is {k} and value is {v}')
new(name='komal', age=21 , quali='btech') 

