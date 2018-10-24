demog = {}

data_points = ["id","age","sex"]

for i in data_points:
    val = input(f"Enter the subject's {i}> ")
    # validate age is an integer
    if i == 'age':
        while True:
            try:
                val = int(val)
                break
            except:
                val = input(f"{val} is not an integer, enter age as an integer> ")

    demog[i]=val

print(f"Subject={demog['id']}\nAge={demog.get('age')}\nSex={demog['sex']}")
            