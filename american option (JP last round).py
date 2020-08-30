'''
Given a fair coin, toss it for at most 100 times, you can stop anytime, then payoff will be n/N.
where N = num of toss before you stop, where N <= 100
where n = num of head you get
Price the following game.

[Hint]
It can be regarded as American option with :

     S0 =  0
    dSt = +1 with prob = 1/2
 or dSt =  0 with prob = 1/2
 payoff = St/t (suppose we exercise at t)
where t = 1,2,3,4, ..., 100
'''

def coin_game_price(maturity) :
    price = []
    for n in range(maturity+1) : price.append(n/maturity)
    for t in range(maturity-1,0,-1) :
        price1 = []
        for n in range(len(price)-1) : price1.append(max(n/t, (price[n]+price[n+1])/2.0))
        price = list(price1)

    if len(price) != 2 : print('ERROR')
    return (price[0]+price[1])/2

for t in [10,100,1000,2000,5000,10000,20000] : print('price for maturity ', t, '=', coin_game_price(t))

