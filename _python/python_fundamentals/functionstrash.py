import random
def randInt(min = 0,max = 100):
    if max<0:
        print('sorry we need a max number greater than 0')
    elif min > max:
        print('sorry please give a max greater than the min')
    else: 
        if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
    return round(random.random()*100)
