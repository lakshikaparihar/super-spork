import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo'] * 10000

def findNemo(array):
    start = time.time()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo!')
    end = time.time()
    print("Call to find Nemo took " + str((end - start) * 1000) + " milliseconds")

findNemo(array=large) # O(n) --> Linear Time