def get_demog(data_points):

    demog = {}
    
    for k,v in data_points.items():
        val = input(f"Enter the subject's {k}> ")
   
        # If v is a type, then compare input value type
        if not isinstance(v,tuple):
            while True:
                try:
                    val = v(val)
                    break
                except:
                    val = input(f"{val} is not an {v}, enter age as an integer> ")
                    
                    
        demog[v]=val
    
    return demog

demog_values = get_demog({"id":str,"age":int,"sex":('M','F'),"weight":float})
print(demog_values)