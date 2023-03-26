
print('Hello world\n'*4+'I love Pytnon\n'*4)
season = input('Imput a number of the month: ')
num_season = int(season)
if num_season >= 3 and num_season <= 5:
    print("It's spring")

if num_season >= 6 and num_season <= 8:
    print("It's summer")

if num_season >= 9 and num_season <= 11:
    print("It's autemn")

if num_season >= 1 and num_season <= 2 or num_season == 12:
    print("It's winter")

if num_season > 12:
    print("It's not a season, try one more time!")
