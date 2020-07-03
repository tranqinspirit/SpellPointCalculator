def SpellPointsAvailable(level):
    spellpool = [4, 6, 14, 17, 27, 32, 38, 44, 57, 64, 73, 73, 83, 83, 94, 94, 107, 114, 123, 133]
    return spellpool[level-1]

def SpellPointCost(castingLevel):
    spellcost = [0, 2, 3, 5, 6, 7, 9, 10, 11, 13]
    return spellcost[castingLevel]

def main():
    level = 8
    haveCastlevel6 = False
    haveCastlevel7 = False
    haveCastlevel8 = False
    haveCastlevel9 = False
    
    if level > 20:
        print("Invalid character level")
        return
    
    spellPoints = SpellPointsAvailable(level)
    print("Spell Point Pool: " + str(spellPoints))
    
    while spellPoints > 0:
        castingLevel = int(input("Spell Level: "))
        if castingLevel > 9:
            print("Invalid spell level" + "\n")
            continue
        else:
            pointsUsed = SpellPointCost(castingLevel)
        
        if castingLevel == 6 and haveCastlevel6 == True:
            print("6th Level spell already used for the day" + "\n")
            continue
        elif castingLevel == 7 and haveCastlevel7 == True:
           print("7th Level spell already used for the day" + "\n")
           continue
        elif castingLevel == 8 and haveCastlevel8 == True:
            print("8th Level spell already used for the day" + "\n")
            continue
        elif castingLevel == 9 and haveCastlevel9 == True:
            print("9th Level spell already used for the day" + "\n")
            continue
        
        elif pointsUsed > spellPoints:
            print("Not enough points to cast")
            break
        else:
            # Make sure we can't cast these more than once per day
            if castingLevel == 6:
                haveCastlevel6 = True
                print("6th level spell used up for the day" + "\n")
            if castingLevel == 7:
                haveCastlevel7 = True
                print("7th level spell used up for the day" + "\n")
            if castingLevel == 8:
                haveCastlevel8 = True
                print("8th level spell used up for the day" + "\n")
            if castingLevel == 9:
                haveCastlevel9 = True
                print("9th level spell used up for the day" + "\n")
                
            spellPoints -= pointsUsed
            print("Spell Point cost: " + str(pointsUsed))
        print("Spell Points left: " + str(spellPoints) + "\n")

if __name__ == "__main__":
    main()
