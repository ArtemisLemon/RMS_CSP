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


prototype_data = {
    "number_of_stages" : 2,
    "stage2machineCount" : [3,3],
    "stage2machineCountMax" : [6,6],
    "number_of_characteristics" : 1,
    "stage2char" : [[True],[True]],
    "number_of_tasks" : 10,
    "task2succtask" : [[False for i in range(10)] for j in range(10)],
    "task2char" : [[True] for i in range(10)]
}

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

write_stringdata(data2stringdata(prototype_data))



