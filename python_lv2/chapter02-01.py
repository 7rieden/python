
# Normal Coding

# Car 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]

# Car 2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

# Car 3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

# List Structure >> 관리 불편
# 인텍스 접근 시 실수 가능성, 삭제 불편

car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'Black', 'horsepower' : 270, 'price' : 5000},
    {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# Dictionary Structure
# Repeating Code, 중첩 문제(Key)

car_dicts = [
    {'car_company' : 'Ferrari', 'car_detail' : {'color' : 'White', 'horsepower' : 400, 'price' : 8000}},
    {'car_company' : 'BMW', 'car_detail' : {'color' : 'Black', 'horsepower' : 270, 'price' : 5000}},
    {'car_company' : 'Audi', 'car_detail' : {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}}
]

print(car_dicts)
print()

del car_dicts[1]
print(car_dicts)

# Class Structure

class car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
        

car1 = car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = car('BMW', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
car3 = car('Audi', {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1))

print()
print()

# Declare Lists
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(repr(x))
    