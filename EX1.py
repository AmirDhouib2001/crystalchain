def entryTime(s, keypad):
    pos = {}
    for i in range(len(keypad)):
        pos[keypad[i]] = (i  // 3, i % 3)
    temps = 0
    curPos = pos[s[0]]
    for i in range(1, len(s)):
        nextPos = pos[s[i]]
        distance = abs(nextPos[0] - curPos[0]) + abs(nextPos[1] - curPos[1])
        temps += distance
        curPos = nextPos
    return temps

s = input("code : ")
keypad = input("keypad : ")

time= entryTime(s, keypad)
print(time)
