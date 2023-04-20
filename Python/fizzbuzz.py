# Day 1
import time

def fizzbuzz(table, repeat):
    '''fizzbuzz function with generators'''
    n = ''
    for i in repeat:
        for k in table:
            if i % table[k] == 0:
                n += k
        if n == '':
            yield i
        else:
            yield n
            n = ''

if __name__ == '__main__':
    # start timer
    start = time.time()

    table = {'Fizz':3, 'Buzz':5}

    # usage example
    # for i in fizzbuzz(table, range(100)):
        # print(i)

    # faster print time
    print('\n'.join(map(str, fizzbuzz(table, range(100)))))

    # end timer
    end = time.time() - start
    print(end,'s')
