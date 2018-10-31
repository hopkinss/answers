def get_demog(data_points):

    demog = {}
    
    for i in data_points:
        val = input(f"Enter the subject's {i}> ")mo

        demog[i]=val
    
    return demog

demog_values = get_demog(("id","age","sex","weight"))
print(demog_values)
            