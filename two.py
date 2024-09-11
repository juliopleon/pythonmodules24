# two.py
import one

print("TOP LEVEL IN TWO.PY")

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported')
