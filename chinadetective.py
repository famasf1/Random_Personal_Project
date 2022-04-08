# First i need to write all the value from the game
dictlist = {"a" : [84,161],"b" : [102,108],"c" : [90,143], "d" : [99,101] , "e" : [109,171] , "f" : [121,150], "g" : [88,100],
"h" : [91,163], "g" : [88,100] , "h" : [91,163], "i" : [112,194],"j" : [72,94], "k" : [87,130], "l" : [144,158], "m" : [103,117], "n" : [69,81],
"o" : [75,120], "p" : [58,111], "q" : [133,180], "r" : [86,192], "s" : [104,125], "t" : [115,190], "u" : [77,173], "v" : [123,95],
"w" : [142,183], "x" : [97,105], "y" : [155,182], "z" : [73,166]}

#All 3 Puzzle from the game
value1 = [144,77,99,104,115,75,142,69]
value2 = [142,109,101,69,109,104,99,84,155]
value3 = [125,112,97,121,120,86,115,182]

#Algorithm
for index, value in enumerate(value1 + value2 + value3):
    for i in dictlist.keys():
        if value in dictlist[i]:
            with open("solved.txt","a") as result:
                result.write(i)