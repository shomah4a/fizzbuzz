'''
fizzbuzz
'''

__version__ = '0.1.0'
__author__ = '@shomah4a'
__license__ = 'LGPL'

def fizzbuzz_gen(last=None):

    count = 1
    
    while True:

        if last is not None and count > last:
            break

        if count % 3 == 0 and count % 5 == 0:
            yield 'fizzbuzz'
        elif count % 3 == 0:
            yield 'fizz'
        elif count % 5 == 0:
            yield 'buzz'
        else:
            yield str(count)

        count += 1


def fizzbuzz(last=None):

    for i in fizzbuzz_gen(last):
        print(i)



if __name__ == '__main__':

    fizzbuzz()
            
        
