def calc_centr(n):
    centr= n//2
    return centr
def print_Matrix (n):
    centr = calc_centr(n)
    for j in range(n):
        for i in range(n):
            if (i == centr) & (j == centr):
                print(' ', end = '')
            else:
                print("*", end ='')
        print()

n= int(input())
if(n%2==0) | (n<3):
    print('Введите нечетное число и больше трех')
else :
    print_Matrix(n)