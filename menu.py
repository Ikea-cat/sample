sudado_de_pollo = [1, 'potato', 'rice', 'tomato', 'drumsticks']
alfredo_pasta = [2, 'heavy cream', 'butter', 'chicken breast', 'parmesan']
burrito = [3, 'ground beef', 'onion', 'lettuce', 'sour cream', 'hot sauce', 'guac', 'tortilla', 'cheese']
menu = [sudado_de_pollo, alfredo_pasta, burrito]


def countingredients(a):
    quantity = []
    findex = 0
    while findex < len(a):
        name = a[findex]
        quality = a.count(a[findex])
        findex = findex + 1
        combo = (name, quality)
        if combo not in quantity:
            quantity.append(combo)
    print(quantity)


def day_of_the_week(a):
    today = ''
    if a == 0:
        today = 'monday'
    elif a == 1:
        today = 'tuesday'
    elif a == 2:
        today = 'wednesday'
    elif a == 3:
        today = 'thursday'
    elif a == 4:
        today = 'friday'
    elif a == 5:
        today = 'saturday'
    elif a == 6:
        today = 'sunday'
    else:
        print('mission failed well get them next time')
    print(today)


print('make sure to write everything in lowercase')
onhand = input('what do you have on hand?\n')
ingredients = onhand.split()
groceries = []
dayoftheweek = 0
while dayoftheweek < 7:
    dontbreakme=0
    while dontbreakme==0:
        try:
            day_of_the_week(dayoftheweek)
            chosen = int(input(' what do you wanna cook?\n 1.sudado de pollo \n 2.alfredo pasta\n 3.burrito\n'))
            if chosen<0 or chosen>3:
                print(3/0)
            dontbreakme=dontbreakme+1
        except:
            print('put a number you dingus')
    recipe = menu[(chosen - 1)]
    if type(recipe[0]) is int:
        print('true')
        del recipe[0]
    else:
        print('not true')
    needs = recipe
    dayoftheweek = dayoftheweek + 1
    for ingredient in ingredients:
        index = 0
        if ingredient in recipe:
            for need in needs:
                if need == ingredient:
                    del needs[index]
                    index = index + 1
                else:
                    index = index + 1
                    continue
        groceries.extend(needs)

countingredients(groceries)
