import csv
import json

#class C_Read_Sort():

def main():
        clog = load()
        menu = {1: 'display Options', 2: 'Sort', 3:'Filter', 4:'Exit'}
        running = True
        while running == True:
                for key, value in menu.items():
                      print(f"{key}: {value}")
                choosing = int(input("Which would you like via number: "))
                if choosing == 1:
                        try:
                                choose_saved_file()
                        except FileNotFoundError:
                                with open('saved_files.json', 'w') as f:
                                        json.dump(['cars.csv'], f)
                                choose_saved_file()
                elif choosing == 2:
                        sort(clog)
                elif choosing == 3:
                        filter(clog, )
                elif choosing == 4:
                        break                        
        

def add_to_registry(filename):
    try:
        with open('saved_files.json', 'r') as f:
            files = json.load(f)
    except FileNotFoundError:
        files = []
    
    files.append(filename)
    
    with open('saved_files.json', 'w') as f:
        json.dump(files, f)

def load():
        with open(file = 'cars.csv', mode = 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            dic = list(reader)
        return dic

def filter(clog, ):
        fields = list(clog[0].keys())
        print("Sort by:")
        for i, field in enumerate(fields):
                print(f"{i+1}: {field}")
        choice = int(input("Enter number: ")) - 1
        field = fields[choice]
        value = int(input('From what number minimum would you like: '))
        results = [car for car in clog if float(car[field]) > value]

        display(results)
        save = input("Save y/n: ").lower()
        if save == 'y':
                name = input("Name: ").strip() + '.csv'
                with open(name, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.DictWriter(f, fieldnames=results[0].keys())
                        writer.writeheader()
                        writer.writerows(results)
                        add_to_registry(name)
        return results

def sort(clog):
    fields = list(clog[0].keys())
    print("Sort by:")
    for i, field in enumerate(fields):
        print(f"{i+1}: {field}")
    choice = int(input("Enter number: ")) - 1
    field = fields[choice]
    direction = input("Ascending or descending (a/d): ").lower()
    reverse = direction == 'd'
    
    try:
        result = sorted(clog, key=lambda car: float(car[field]), reverse=reverse)
    except ValueError:
        result = sorted(clog, key=lambda car: car[field], reverse=reverse)
    
    display(result)
    
    save = input("Save y/n: ").lower()
    if save == 'y':
        name = input("Name: ").strip() + '.csv'
        with open(name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=result[0].keys())
            writer.writeheader()
            writer.writerows(result)
        add_to_registry(name)
    return result

def display(clog):
        print(' | '.join(clog[0].keys()))  # prints headers
        for car in clog:
                print(' | '.join(str(v) for v in car.values()))

def choose_saved_file():
    with open('saved_files.json', 'r') as f:
        files = json.load(f)
    
    print("Saved files:")
    for i, f in enumerate(files):
        print(f"{i+1}: {f}")
    
    choice = int(input("Which file: ")) - 1
    filename = files[choice]
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    display(data)

if __name__ == '__main__':
       main()