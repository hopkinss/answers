import csv
def read_data(input_file):
    """read in the data and return a dictionary"""    
    data = {}
    with open(input_file) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            key  = row.pop('NAME').upper()
            data[key]=row
    return data            

            
def get_subject_details(subject,data):
    
    try:
        return data[subject]
    except KeyError:
        raise KeyError("Subject not found")
        

if __name__=="__main__":
    data = read_data("class.csv")
    
    value = get_subject_details("ALICE",data)
    
    print(value)
    
    
    
    
