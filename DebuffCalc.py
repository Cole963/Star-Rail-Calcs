import easygui
import math


title = "Hit Rate Calculator"

baseChance = easygui.enterbox("Enter Base Chance: ", title, "")
baseChance = float(baseChance)/100

hitRate = easygui.enterbox("Enter Hit Rate: ", title, "")
hitRate = float(hitRate)/100

effRes = easygui.enterbox("Enter Effect Resistance: ", title, "")
effRes = float(effRes)/100

debuffRes = easygui.enterbox("Enter Debuff Resistance: ", title, "")
debuffRes = float(debuffRes)/100


def hitRateCalc(baseChance, hitRate, effRes, debuffRes):

    realEffProb = baseChance * (1 + hitRate) * (1 - effRes) * (1 - debuffRes)
    return realEffProb
  

resultTitle = "Result"

results = hitRateCalc(baseChance, hitRate, effRes, debuffRes)

message = "The chance of landing a debuff is: " + str(results*100) + "%"

easygui.msgbox(message, resultTitle)