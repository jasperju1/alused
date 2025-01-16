# Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

from random import randint

choices = ['kivi', 'paber', 'käärid']
question = 'y'

while question == 'y':
    human = ''

    computer = choices[randint(0, 2)]

    while human not in choices:

        human = input('Sisesta enda valik (kivi, paber või käärid): ')
        print(computer, human)

    if computer == 'kivi' and human == 'käärid' \
        or computer == 'paber' and human == 'kivi' \
        or computer == 'käärid' and human == 'paber':
        print('Sa kaotasid!')

    elif computer == human:
        print('Teil tekkis viik!')

    else:
        print('Sa võitsid!')
    
    question = input("Kas sa soovid uuesti mängida? (y/n): ")

    





