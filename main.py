import xmltodict
import os

def get_info(file_name):
    print("Pegou o arquivo: " + file_name)
    with open('nfs/' + file_name, "r") as file_xml:
        file_dic = xmltodict.parse(file_xml.read())
        print(file_dic)
        
file_list = os.listdir('nfs')

for file in file_list:
    get_info(file)