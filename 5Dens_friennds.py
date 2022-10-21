s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

def takeSecond(e):
    return e[1]

#тут список отримує зручніший для програми вигляд
def doBetterList(meh):
    meh = meh.upper()
    lst = meh.split(";")
    betterlst = []
    for i in range(len(lst)):
        betterlst.append(lst[i].split(":"))
    return betterlst

def sortByLastName(fixedlst):
    #спочатку список сортується по іменам, потім по фаміліям, завдяки key=takeSecond
    return sorted(sorted(fixedlst), key=takeSecond)

print(sortByLastName(doBetterList(s)))