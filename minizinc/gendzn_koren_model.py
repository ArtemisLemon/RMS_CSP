import random

def string_array_number(l):
    in_string = ""
    for val in l:
        in_string += str(val)
        in_string += ","
    return "[{}]".format(in_string[:-1])

def string_array2d_bool(m,i_str,j_str):
    in_string = ""
    for line in m:
        for val in line:
            if val:
                in_string +="true,"
            else:
                in_string +="false,"
    return "array2d(1..{},1..{},[{}])".format(i_str,j_str,in_string[:-1])

def string_affectation(variable, affectation):
    out = "{} = {};\n".format(variable,affectation)
    return out


# prototype_data = {
#     "number_of_stages" : 2,
#     "stage2machineCount" : [3,3],
#     "stage2machineCountMax" : [6,6],
#     "number_of_characteristics" : 1,
#     "stage2char" : [[True],[True]],
#     "number_of_tasks" : 10,
#     "task2succtask" : [[False for i in range(10)] for j in range(10)],
#     "task2char" : [[True] for i in range(10)]
# }

def gen_prototype_data_dimentions(stages,mc,mmc,characteristics,tasks):
    out = {
        "number_of_stages" : stages,
        "stage2machineCount" : [mc for i in range(stages)],
        "stage2machineCountMax" : [mmc for i in range(stages)],
        "number_of_characteristics" : characteristics,
        "stage2char" : [[True for i in range(characteristics)] for j in range(stages)],
        "number_of_tasks" : tasks,
        "task2succtask" : [[False for i in range(tasks)] for j in range(tasks)],
        "task2char" : [[True for i in range(characteristics)] for j in range(tasks)]
    }
    return out

prototype_data = gen_prototype_data_dimentions(2,3,6,1,10)

def boolfromItoJ(bool,i,j,row):
    out = row
    for b in range(i,j):
        out[b] = bool
    return out

def data2stringdata(data):
    out = data
    out["number_of_stages"] = str(out["number_of_stages"])
    out["stage2machineCount"] = string_array_number(out["stage2machineCount"])
    out["stage2machineCountMax"] = string_array_number(out["stage2machineCountMax"])
    out["number_of_characteristics"] = str(out["number_of_characteristics"])
    out["stage2char"] = string_array2d_bool(out["stage2char"],"number_of_stages","number_of_characteristics")
    out["number_of_tasks"] = str(out["number_of_tasks"])
    out["task2succtask"] = string_array2d_bool(out["task2succtask"],"number_of_tasks","number_of_tasks")
    out["task2char"] = string_array2d_bool(out["task2char"],"number_of_tasks","number_of_characteristics")
    return out

def write_stringdata(data):
    open("koren_model.dzn","w").close()
    with open("koren_model.dzn","a") as file:
        for key, val in data.items():
            print("{} : {}".format(key,val))
            file.write(string_affectation(key,val))


# Edit Data
def triangleSUCCdata(prototype_data):
    out = prototype_data
    edit = out["task2succtask"]

    for i, row in enumerate(edit):
        row = boolfromItoJ(True,i,len(row),row)
    
    out["task2succtask"] = edit
    return out


def randomCHARdata(prototype_data):
    out = prototype_data
    edit_task = [[False for j in range(out["number_of_characteristics"])] for i in range(len(out["task2char"]))]
    edit_stage = out["stage2char"]

    for row in edit_task:
        j = random.choice([1,1,1,1,2,2,3])
        i = random.choice([i for i in range(len(row)-j)])
        
        row = boolfromItoJ(True,i,i+j,row)
    
    for row in edit_stage:
        j = random.choice([0,0,1,1,1,1])
        i = random.choice([i for i in range(len(row)-j)])
        row = boolfromItoJ(False,i,i+j,row)

    out["task2char"] = edit_task
    out["stage2char"] = edit_stage
    return out

def mydata():
    out = gen_prototype_data_dimentions(4,3,6,10,20)

    edit = out["task2succtask"]
    for i in range(6):
        edit[i] = boolfromItoJ(True, i,len(edit[i]),edit[i])
    for i in range(10,13):
        edit[i] = boolfromItoJ(True, i,13,edit[i])
    out["task2succtask"]= edit

    edit = out["stage2char"]
    edit[1]= boolfromItoJ(False,5,10,edit[1])
    out["stage2char"] = edit

    edit = [[False for j in range(out["number_of_characteristics"])] for i in range(len(out["task2char"]))]
    for row in edit:
        i = random.choice([i for i in range(len(row))])       
        row[i]=True
    out["task2char"] = edit
    return out

# Make Data
# write_stringdata(data2stringdata(prototype_data))

# write_stringdata(data2stringdata(
#     triangleSUCCdata(
#         gen_prototype_data_dimentions(4,3,6,1,20))))

# write_stringdata(data2stringdata(
#     arbitraryCHARdata(
#         gen_prototype_data_dimentions(4,3,6,5,20))))

write_stringdata(data2stringdata(
    mydata()))