

for i in range(1,100):
    if not (i % 3 + i % 5):
        print (i," fizbuzz")
    elif not (i % 3):
        print(i, " fizz")
    elif not (i % 5):
        print(i , ' buzz')
    else:
        print(i)
    