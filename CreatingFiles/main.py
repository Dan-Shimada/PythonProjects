# o segundo argumento determina o tipo de operacao a ser realizada no arquivo
# Se for "r+" então o arquivo será lido
# Se for "w+" então o arquivo será escrito
newfile = open("newfile.txt", "w+")
string = "Creating new file and writing in it"
newfile.write(string)

####################################################
import simplejson as json
import os # consegue obter informações sobre o arquivo, como se esse esta vazio ou nao

# verifica se existe um determinado arquivo, se o valor for igual a zero então o arquivo estara vazio
# agora, se não existir o arquivo, criara um arquivo no old_file
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is ", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Nick", "age": 27}
    print("No file found, setting default age to ", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))





