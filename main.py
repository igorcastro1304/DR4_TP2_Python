import csv
import pandas as pd

#TP 2.1
data = [
    ["Nome", "Idade", "Cidade"],
    ["Aurelio", 27, "Rio de Janeiro"],
    ["Jonas", 30, "São Paulo"],
    ["Luciana", 25, "Belo Horizonte"],
]

def write_csv_archive():    
    with open("dados.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
    
#TP 2.2
def read_csv_archive():
    with open("dados.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
            
#TP 2.3
def cast_csv_to_dict():
    dict_list = {}
    
    with open("dados.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        dict_list = {name: {"Idade": int(age), "Cidade": city} for name, age, city in reader}

    return dict_list

#TP 2.4
def get_sao_paulo_person_age():
    data_dict = cast_csv_to_dict()
    
    for _, values in data_dict.items():
        if values["Cidade"] == "São Paulo":
            return values["Idade"]
        
#TP 2.5
def calc_total_sales():
    total_sales = 0
    
    with open("vendas.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        for row in reader:
            total_sales += int(row[1])
            
    return total_sales

#TP 2.6
def create_and_read_orders():
    orders_data = [
        ["id", "produto", "quantidade"],
        [1, "celular", 20],
        [2, "notebook", 30],
        [3, "caderno", 50],
        [4, "bloco de notas", 10],
        [5, "café", 50],
    ]
    
    with open("pedidos.csv", "w+", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(orders_data)
        
        csv_file.seek(0)

        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
    

#TP 2.7
def count_orders_rows():
    with open("pedidos.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        print(len(rows)) 


#TP 2.8
def create_dataframe_from_csv():
    df = pd.read_csv("empregados.csv")

    df.to_csv("empregados_copia.csv", index=False)

    print("Arquivo empregados_copia.csv salvo com sucesso!")
    print(df)
    
#TP 2.9
def get_biggest_salary():
    df = pd.read_csv("empregados.csv")
    
    biggest_salary = df.loc[df["Salario"].idxmax()]

    print("Funcionário com o maior salário:")
    print(biggest_salary)


#TP 2.10
def get_on_going_projects():
    with open("projetos.csv", "r", newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        header = next(reader)

        print("Projetos 'Em elaboração':")
        for row in reader:
            if row[2] == "Em elaboração":
                print(row) 


#TP 2.11
def create_and_read_csv():
    data = [
        ["id", "quantidade", "preço"],
        [1, 10, 15.50],
        [2, 5, 8.75],
        [3, 20, 22.30],
    ]

    with open("produtos.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter="|")
        writer.writerows(data)

    with open("produtos.csv", "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="|")
        for row in reader:
            print(" | ".join(row))


#TP 2.12
def save_dataframe_to_csv():
    data = {
        "id": [1, 2, 3],
        "produto": ["Celular", "Notebook", "Fone"],
        "preço": [1500.99, 3200.50, 199.99]
    }
    df = pd.DataFrame(data)

    df.to_csv("produtos_pandas.csv", sep=";", index=False, encoding="utf-8")


write_csv_archive()
read_csv_archive()
dict_cast = cast_csv_to_dict()
print(dict_cast)
person_age_from_sp = get_sao_paulo_person_age()
print(person_age_from_sp)
print(calc_total_sales())
create_and_read_orders()
count_orders_rows()
create_dataframe_from_csv()
get_biggest_salary()
get_on_going_projects()
create_and_read_csv()
save_dataframe_to_csv()