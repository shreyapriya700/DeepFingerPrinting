import os
import pickle
os.chdir("C:\Users\hp\Desktop\FCN Project\Deep Fingerprinting\closed-world-protected")

file_list = os.listdir(".")
file_list = [f for f in file_list if '.' not in f ]

def modify_line(line):
    key, value = line.strip().split('\t')
    return replace_values(value)

def replace_values(input_string):
    int_input = int(input_string.strip())
    if int_input < 0 :
        return int(-1)
    return int(1)

def modfify_file(file_name, write_file):
    with open(file_name) as read_file:
        response = [ modify_line(line) for line in read_file]
        result = list(range(2000))
        for i in range(2000):
            if i < len(response):
                result[i] = response[i]
            else:
                result[i] = 0
        return result

with open('./good1.pickle', 'wb') as write_file:
    response = []
    for file_name in file_list:
        response.append(modfify_file(file_name, write_file))
    pickle.dump(response, write_file)

with open('./good2.pickle', 'wb') as write_file:
    #pickle.dump(file_list, write_file)
    #print(file_list)
    response = []
    for file_name in file_list:
        response.append(file_name.split("-")[0])
    print(len(response))
    pickle.dump(response, write_file)
