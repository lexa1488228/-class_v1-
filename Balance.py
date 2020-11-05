class Balance:
    def x(a):
        a.right = 0
        a.left = 0

    def add_right(a, r):
        a.right = r

    def add_left(a, u):
        a.left = u

    def result(a):
        if a.left > a.right:
            print('L')
        if a.left < a.right:
            print('R')
        else:
            print('=')
