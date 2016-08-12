def toInt(time):
    time = list(time)
    time.remove(':')
    return int(''.join(time))


def toTime(intTime):
    intTime = list(str(intTime))
    intTime.insert(-2,':')
    return str(''.join(intTime))


def checkRush(time):
    if time < 1000 and time >= 700:
        return 1
    elif time < 1900 and time >= 1500:
        return 1
    else:
        return 0

def correctTime(time):
    time=int(time)
    if (time // 10) % 10 == 6:
        time += 40
        if time > 2400:
            return 100
        else:
            return time
    else:
        return time

def check(cT,di):
    cT = correctTime(cT)
    if di == 0:
        return(toTime(cT))
    elif checkRush(cT):
        return(check(cT + 20,di - 20))
    else:
        return(check(cT + 10,di - 20))

curTime = toInt(input())
print(check(curTime,240))