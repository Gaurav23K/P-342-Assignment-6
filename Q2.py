'''
Gaurav Kanu{1811067}
Assignment : 6
Q_2 :
'''
import you_can


def func(x):
    f = (x/(1+x))
    return f


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


n = 5
M1 = you_can.mid_point(1, 3, func, n)
T1 = you_can.trapezoidal(1, 3, func, n)
S1 = you_can.simpson(1, 3, func, n)

n = 10
M2 = you_can.mid_point(1, 3, func, n)
T2 = you_can.trapezoidal(1, 3, func, n)
S2 = you_can.simpson(1, 3, func, n)

n = 25
M3 = you_can.mid_point(1, 3, func, n)
T3 = you_can.trapezoidal(1, 3, func, n)
S3 = you_can.simpson(1, 3, func, n)

a = 1.30685281944                                           # Analytical result

print(color.BOLD+"N{:<5} Mid_point{:<20} Trapezoidal{:<15} Simpson{:<13} Analytical{:<5}".format("","","","","")+color.END)
print("{:<5} {:<25} {:<25} {:<25} {:<5}".format(5, M1[0], T1[0], S1[0], a))
print("{:<5} {:<25} {:<25} {:<25} {:<5}".format(10, M2[0], T2[0], S2[0], a))
print("{:<5} {:<25} {:<25} {:<25} {:<5}".format(25, M3[0], T3[0], S3[0], a))

'''
******************************************OUTPUT************************************************

N      Mid_point                     Trapezoidal                Simpson              Analytical     
5     1.308092114284065         1.3043650793650796        1.3068497693110694        1.30685281944
10    1.3071646395900398        1.3062285968245722        1.306852625334884         1.30685281944
25    1.3069028019555275        1.3067528394240817        1.306852814445046         1.30685281944
'''