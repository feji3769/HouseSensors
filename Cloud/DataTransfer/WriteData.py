

def write_data(data_dict, filename):
    """
    This function writes the data recieved at timestamp stored in data_dict to the filename. 

    Inputs:
    timestamp (str) containing time data was recieved
    data_dict (dict) dictionary containing the data to be written
    filename (str) location to store data
    """
    with open(filename, "a") as f:
        i = 0
        for key in data_dict:
            print(data_dict[key])
            if i == 0:
                f.writelines("New Data Recieved at: " + data_dict[key] + "\n")
                i = i + 1
            else:
                new_line = key + ": " + str(data_dict[key]) + "\n"
                f.writelines(new_line)



