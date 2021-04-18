from time import sleep

for c in range(10,-1, -1):
    print(c)
    sleep(1)

print('\033[32m BUM!\033[m \033[35m  BUM!\033[m \033[31m POOOW!\033[m')