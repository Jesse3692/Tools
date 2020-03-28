import sys

saved_stdout = sys.stdout

with open('./log/hello1.txt', 'wt') as file:
    sys.stdout = file
    print('This message is for file !')
    for i in range(19):
        print("chr{0}\t{1}\t{2}".format(1, i*500, (i+1)*500))

sys.stdout = saved_stdout
print('This message is for screen') 