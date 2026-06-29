import csv


#class C_Read_Sort():

def main():
        clog = load()
        menu = {1: 'display Options', 2: 'Sort', 3:'Filter'}
        choosing = int(input("Which would you like via number: "))
        if choosing == 1:
              whichDisplay = loadAllList()
              print(whichDisplay)
              display(clog)
        elif choosing == 2:
              sort(clog)
        elif choosing == 3:
                filter(clog, field, value)
        

def loadAllList():
        with open(file = 'All.csv', mode = 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            loaded = list(reader)
        return loaded

def load():
        with open(file = 'cars.csv', mode = 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            dic = list(reader)
        return dic

def filter(clog, field, value):
        return [car for car in clog if float(car[field]) > value]

def sort(clog):
    fields = list(clog[0].keys())  # get column names from first car
    print("Sort by:")
    for i, field in enumerate(fields):
        print(f"{i+1}: {field}")
    
    choice = int(input("Enter number: ")) - 1
    field = fields[choice]
    
    direction = input("Ascending or descending (a/d): ").lower()
    reverse = direction == 'd'
    
    try:
        return sorted(clog, key=lambda car: float(car[field]), reverse=reverse)
    except ValueError:
        return sorted(clog, key=lambda car: car[field], reverse=reverse)
    

def display(clog):
        print(' | '.join(clog[0].keys()))  # prints headers
        for car in clog:
                print(' | '.join(str(v) for v in car.values()))



if __name__ == '__main__':
       main()