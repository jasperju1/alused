# https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/
#Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri lisatasu arvutamise funktsioon. Sisendina defineeri dictionary.

data = {
    'Revenue':{
        'Konata':{
            'Chocolate': 300,
            'Puffy': 200,
            'Manga': 1200,
            'Figure': 3400
        },

        'Lily':{
            'Chocolate': 300,
            'Puffy': 200,
            'Manga': 1200,
            'Figure': 3400
        },

        'Noelle':{
            'Chocolate': 300,
            'Puffy': 200,
            'Manga': 1200,
            'Figure': 3400
        },

        'Evan':{
            'Chocolate': 300,
            'Puffy': 200,
            'Manga': 1200,
            'Figure': 3400
        }
    }
},



for k in data['Revenue']:
    profit = 0
    for l in data['Revenue'][k]:
        print(k, l, data['Revenue'] - data['Expenses'][k][l])
        profit += data['Revenue'] - data['Expenses'][k][l]
print(profit)
