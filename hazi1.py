nums = [3, 4, 9, 6, 2]

for num in nums:
    if num % 2 == 0:
        print(str(num) + ': osztható')
    else:
        print(str(num) + ': nem osztható')

players = ['Peter', 'Kate', 'John']

for player in players:
    print(str(players.index(player) + 1) + '. ' + player)

x = ['', 4, True]


def myfunc(list):
    a = []
    for index in list:
        if type(index) is int:
            a.append('integer')
        elif type(index) is str:
            a.append('string')
        else:
            a.append('boolean')
    return a


print(myfunc(x))