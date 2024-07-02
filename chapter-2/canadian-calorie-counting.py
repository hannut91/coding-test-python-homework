# Canadian Calorie Counting - https://dmoj.ca/problem/ccc06j1
import re

pattern = re.compile(r'^[1-4]$')

bugers = {
    1: {"name": "Cheeseburger", "calories": 461},
    2: {"name": "Fish Burger", "calories": 431},
    3: {"name": "Veggie Burger", "calories": 420},
}

drinks = {
    1: {"name": "Soft Drink", "calories": 130},
    2: {"name": "Orange Juice", "calories": 160},
    3: {"name": "Milk", "calories": 118},
}

sides = {
    1: {"name": "Fries", "calories": 100},
    2: {"name": "Baked Potato", "calories": 57},
    3: {"name": "Chef Salad", "calories": 70},
}

desserts = {
    1: {"name": "Apple Pie", "calories": 167},
    2: {"name": "Sundae", "calories": 266},
    3: {"name": "Fruit Cup", "calories": 75},
}


def selectMenu(menu, number):
    return menu.get(number, {"calories": 0})["calories"]


def inputDigit():
    value = input()
    if pattern.match(value):
        return int(value)
    else:
        raise "1-4 정수만 입력 가능합니다"


buguerChoice = inputDigit()
sideChoice = inputDigit()

drinkChoice = inputDigit()
dessertChoice = inputDigit()

totalCal = (selectMenu(bugers, buguerChoice) + selectMenu(sides, sideChoice) + selectMenu(drinks, drinkChoice) +
            + selectMenu(desserts, dessertChoice))

print(f"Your total Calorie count is {totalCal}.")
