import csv


#class C_Read_Sort():

def main():
        print("Hello")
        clog = load()
        display(clog)
        filter(clog)


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

def display(clog):
        print(' | '.join(clog[0].keys()))  # prints headers
        for car in clog:
                print(' | '.join(str(v) for v in car.values()))
if __name__ == '__main__':
       main()