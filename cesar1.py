line1 = (input(""))
line2 = (input(""))
line3 = (input(""))
line4 = (input(""))

line11 = len(line1)
line21 = len(line2)
line31 = len(line3)
line41 = len(line4)

shift = ord(line1[0]) - ord("H")
if shift==0:  
    print(line1)
    print(line2)
    print(line3)
    print(line4)
if shift != 0:
    check1 = 0
    final1 = ""
    for i in range(0, line11, 1):
        stafur = line1[check1]
        stafur = ord(stafur) - shift
        if stafur>126:
            stafur -= 95
        if stafur<32:
            stafur += 95
        ord1 = chr(stafur)
        final1 += ord1
        check1 += 1
    check2 = 0
    final2 = ""
    for i in range(0, line21, 1):
        stafur = line2[check2]
        stafur = ord(stafur) - shift
        if stafur>126:
            stafur -= 95
        if stafur<32:
            stafur += 95
        ord2 = chr(stafur)
        final2 += ord2
        check2 += 1
    check3 = 0
    final3 = ""
    for i in range(0, line31, 1):
        stafur = line3[check3]
        stafur = ord(stafur) - shift
        if stafur>126:
            stafur -= 95
        if stafur<32:
            stafur += 95
        ord3 = chr(stafur)
        final3 += ord3
        check3 += 1
    check4 = 0
    final4 = ""
    for i in range(0, line41, 1):
        stafur = line4[check4]
        stafur = ord(stafur) - shift
        if stafur>126:
            stafur -= 95
        if stafur<32:
            stafur += 95
        ord4 = chr(stafur)
        final4 += ord4
        check4 += 1
    print(final1)
    print(final2)
    print(final3)
    print(final4)
