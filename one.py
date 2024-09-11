# one.py
def func():
    print("My func() in one.py")


print("TOP LEVEL IN ONE.PY")

# __name__ == '__main__' means if this file is in the main directory run it u can also add methods to the bottom to pick order it will be ran
if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported')
