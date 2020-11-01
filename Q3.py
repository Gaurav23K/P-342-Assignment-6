'''
Gaurav Kanu{1811067}
Assignment : 6
Q_3 :
'''
import you_can
import math


def func(x):
    f = math.exp(-x**2)
    return f


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


n = 10
M = you_can.mid_point(0, 1, func, n)

n = 15
T = you_can.trapezoidal(0, 1, func, n)

n = 25
S = you_can.simpson(0, 1, func, n)

print(color.BOLD+"Method{:<10} N{:<15} Result{:<15} Error{:<10}".format("", "", "", "")+color.END)
print("{:<15} {:<10} {:<25} {:<10}".format("Midpoint", 10, M[0], M[1]))
print("{:<15} {:<10} {:<25} {:<10}".format("Trapezoidal", 15, T[0], T[1]))
print("{:<15} {:<10} {:<25} {:<10}".format("Simpson", 25, S[0], S[1]))


'''
******************************OUTPUT*************************************

Method           N                Result                Error          
Midpoint        10         0.7471308777479975        0.0008270957992569568
Trapezoidal     15         0.7465515891604121        0.0007309001140945972
Simpson         25         0.7468241341203177        0.0009473903143468
'''
