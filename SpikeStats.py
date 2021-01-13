from tkinter import *
import csv
import tkinter.messagebox
from PIL import Image, ImageTk
import datetime
import time

root = Tk()
root.minsize(1000,800)
root.maxsize()
mainframe = Frame(root)


def showFlow(flowList):

    flowFrame = Toplevel(root)
    cvwidth = 900
    flowCanvas = Canvas(flowFrame, width = cvwidth, height = 250, background = "#F1F1F1")
    exitButton = Button(flowFrame, text = 'Exit', command = flowFrame.destroy)
    boxwidth = 15
    flowCanvas.grid()
    exitButton.grid(pady = 50, ipadx = 80, ipady = 20)
    maxLength = len(flowList) * boxwidth
    initX = (cvwidth - maxLength) // 2
    for point in flowList:
        if point == 0:
            flowCanvas.create_rectangle(initX, 125, initX+boxwidth, 200, fill = 'Red', outline = '#F1F1F1')
        elif point == 1:
            flowCanvas.create_rectangle(initX, 125, initX+boxwidth, 50, fill = 'Blue', outline = '#F1F1F1')
        initX += boxwidth


####################################NON GUI CODE
       
def separateNameNum(player):
    global playerList
    if player in playerList:
        for c in player:
            if c.isdigit():
                i = player.index(c)
                return player[:i], player[i:]
    return '', 'Opp'
        

def makeLookup(num, d, count):
    d[num] = count
    
        
def getRoster():
    playerList = []

    with open('roster.txt') as fileIn:
    
        listIndex = 0

        for line in fileIn:
            
            line = line.strip()
            playerList.append(line)
    return playerList

def getLookup():
    playerLookup = {}
    with open('roster.txt') as fileIn:
    
        listIndex = 0

        for line in fileIn:
            
            line = line.strip()
            name, num = separateNameNum(line)
                        
            makeLookup(num, playerLookup, listIndex)
                            
            listIndex += 1

    return playerLookup

def getCategories():

    categories = []
    
    with open('categories.txt') as categoriesIn:
        for line in categoriesIn:
            
            line = line.strip()
            categories.append(line)

            
    return categories



def tallyList(playerList, categories):
    master = []
    for player in playerList:
        l = [player]
        for c in categories:
            if c == 'Player':
                pass
            else:
                l.append(0)
        master.append(l)
    return master



##############################################GUI CODE

changes = []

def numChanges(num):
    global changes
    for i in range(num-1):
        changes.pop()
    changes.append(num)

def addOppPoint():
    global statline, actionHistory, playerHistory
    statline[-1][2] += 1
    alertVar.set('+1 Opponents\' points')
    actionHistory.append(2)
    playerHistory.append(-1)
    numChanges(1)
    addToFlow(0)
    #saveData()

def addOppError():
    global statline
    statline[-1][3] += 1
    alertVar.set('+1 Opponents\' errors')
    actionHistory.append(3)
    playerHistory.append(-1)
    numChanges(1)
    addToFlow(1)
            
def addHit():
    if nameValid(checkEntry()):
        alertVar.set(f'+1 Hits for {playerNameVar.get()}')
        saveData(1)
        numChanges(1)

def addKill():
    if nameValid(checkEntry()):
        addHit()
        alertVar.set(f'+1 Kills for {playerNameVar.get()}')
        saveData(2)
        numChanges(2)
        addToFlow(1)

def addError():
    if nameValid(checkEntry()):
        addHit()
        addOppPoint()
        alertVar.set(f'+1 Errors for {playerNameVar.get()}')
        saveData(3)
        numChanges(3)

def addServeIn():
    if nameValid(checkEntry()):
        alertVar.set(f'+1 Serves In for {playerNameVar.get()}')
        saveData(4)
        numChanges(1)

def addServeOut():
    if nameValid(checkEntry()):
        addOppPoint()
        alertVar.set(f'+1 Serves Out for {playerNameVar.get()}')
        saveData(5)
        numChanges(2)

def addAce():
    if nameValid(checkEntry()):
        alertVar.set(f'+1 Aces for {playerNameVar.get()}')
        saveData(6)
        numChanges(1)
        addToFlow(1)

def addPass():
    if nameValid(checkEntry()):
        saveData(7)
        numChanges(1)

def add1():
    if nameValid(checkEntry()):
        addPass()
        alertVar.set(f'+1 1Pass for {playerNameVar.get()}')
        saveData(9)
        numChanges(2)
    

def add2():
    if nameValid(checkEntry()):
        addPass()
        alertVar.set(f'+1 2Pass for {playerNameVar.get()}')
        saveData(10)
        numChanges(2)

def add3():
    if nameValid(checkEntry()):
        addPass()
        alertVar.set(f'+1 3Pass for {playerNameVar.get()}')
        saveData(11)
        numChanges(2)

def addShank():
    if nameValid(checkEntry()):
        addPass()
        alertVar.set(f'+1 0Pass for {playerNameVar.get()}')
        saveData(8)
        numChanges(2)

def addDig():
    if nameValid(checkEntry()):
        alertVar.set(f'+1 Digs for {playerNameVar.get()}')
        saveData(12)
        numChanges(1)

def addBlock():
    if nameValid(checkEntry()):
        alertVar.set(f'+1 Blocks for {playerNameVar.get()}')
        saveData(13)
        numChanges(1)

def addBlocked():
    if nameValid(checkEntry()):
        alertVar.set(f'+1 Blocked for {playerNameVar.get()}')
        saveData(14)
        numChanges(1)

def addBlockError():
    if nameValid(checkEntry()):
        addOppPoint()
        alertVar.set(f'+1 Block Errors for {playerNameVar.get()}')
        saveData(15)
        numChanges(2)


def nameValid(entry):
    if 'press' in entry:
        playerNameVar.set("Press Enter First")
        alertVar.set('Changes could not be made')
        return False
    elif entry not in getLookup():
        playerNameVar.set("Not a valid jersey number")
        alertVar.set('Changes could not be made')
        return False
    else:
        return True

def checkEntry():
    if playerNumVar.get() != playerEntry.get():
        return 'press enter first'
    else:
        return playerNumVar.get()


    
def saveData(action):
    global playerList, playerLookup, statline, actionHistory, playerHistory
    l = playerList
    d = playerLookup
    playerLine = statline
    playerNum = checkEntry()
    
    if nameValid(playerNum):
        errorVar.set('')
        
        pos = d[playerNum]
        playerNameVar.set(l[pos])

        playerLine[pos][action] += 1

        playerHistory.append(pos)
        actionHistory.append(action)

def undo():
    global playerList, statline, categories, actionHistory, playerHistory, gameFlow, changes
    if len(playerHistory) != 0:

        s = ''
        point = False
        for change in range(changes.pop()):
            player = playerHistory.pop()
            action = actionHistory.pop()
            statline[player][action]-=1
            s += f'-1 {categories[action]} for {playerList[player]}\n'

            if action in [2,3,5,6,15]:
                point = True
        if point == True:
            gameFlow.pop()
        alertVar.set(s)
    else:
        alertVar.set('No actions available to undo')


def changePlayer(event):
    global playerList, playerLookup, statline
    l = playerList
    d = playerLookup
    playerLine = statline
    playerNumVar.set(playerEntry.get())
    playerNum = playerNumVar.get()
    
    if nameValid(playerNum):
        errorVar.set('')
        
        pos = d[playerNum]
        playerNameVar.set(l[pos])



def generateTitle():
    d = datetime.date.today()
    vs = teamVsEntry.get()
    if vs == 'test':
        title = 'test.csv'
    else:
        title = f'{d} vs. {vs}.csv'
    teamVsVar.set(title)
    teamVsConfirmLabel.config(text = 'VS Team confirmed!')



def end(categories, statline):
    title = teamVsVar.get()
    ans = tkinter.messagebox.askquestion ('End Program',f'You are about to create a new CSV File called {title}, are you sure?',icon = 'warning')
    ans = ans.upper()
    
    if 'Y' in ans:
        with open(title, 'w', newline='') as fileOut:
            writer = csv.writer(fileOut)
            writer.writerow(categories)
            for player in statline:
                writer.writerow(player)
    else:
        print('File was not created.')

def addToFlow(team):
    global gameFlow
    if team == 1:
        gameFlow.append(1)
    else:
        gameFlow.append(0)


##########################################MAIN




categories = getCategories()
playerList = getRoster()
playerLookup= getLookup()
statline = tallyList(playerList, categories)
actionHistory = []
playerHistory = []
gameFlow = []


###########################################VAR DECLARATIONS
#def setVars():
##intStringLookup = {'0': 'zeroP', '1':'oneP', '2':'twoP', '3':'threeP'}
##varNames = []
##with open('categories.txt') as categoriesIn:
##    for line in categoriesIn:
##
##        line = line.strip().replace(' ','').lower()
##        
##        varName = line + 'Var'
##        
##        if "Player" in line:
##            
##            vars()[varName] = StringVar()
####
####            elif line[0].isdigit():
####                varName = d[line[0]] + varName[2:]
####                vars()[varName] = IntVar()
##            
##        else:
##            if line[0].isdigit():
##                varName = intStringLookup[line[0]] + varName[2:]
##            vars()[varName] = IntVar()
####        print(varName)
##        varNames.append(varName)
##    #for name in varNames:
##        #print(vars()[varName].get())

def printList():
    global playerList, playerLookup, statline, categories, gameFlow, playerHistory, actionHistory, changes
    l=playerList
    c = categories
    playerLine = statline
    d = playerLookup
    
    s = ''
    for i in c:
        
        if i == c[0]:
            s += f'{i:<8}'
        else:
            s += f'{i:<11}'
    print(s)
    for row in playerLine:
        
        s=''
        for col in row:
            if col == row[0]:
                name, num = separateNameNum(col)
                s += f'{num:<8}'
            else:
                s += f'{col:<11}'
        print(s)


IRImg = Image.open("IR.jpg").resize((100,100))
IRPhoto = ImageTk.PhotoImage(IRImg)
IRLabel = Label(mainframe, image=IRPhoto)
IRLabel.image = IRPhoto


teamVsVar = StringVar()
teamVsConfirmLabel = Label(mainframe, text = 'Enter the VS Team')
teamVsEntry = Entry(mainframe)
teamVsEntry.insert(END, 'VS Team')
teamVsConfirmButton = Button(mainframe, text = "Confirm", command = generateTitle)

oppPointsButton = Button(mainframe, text = 'Opponent Point', command = addOppPoint)


oppErrorsButton = Button(mainframe, text = 'Opponent Error', command = addOppError)

hitsButton = Button(mainframe, text = 'Hit', command = addHit)


killsButton = Button(mainframe, text = 'Kill', command = addKill)


errorsButton = Button(mainframe, text = 'Error', command = addError)


servesinButton = Button(mainframe, text = 'Serve In', command = addServeIn)


servesoutButton = Button(mainframe, text = 'Serve Error', command = addServeOut)


acesButton = Button(mainframe, text = 'Ace', command = addAce)


onePassesButton = Button(mainframe, text = '1 Pass', command = add1)


twoPassesButton = Button(mainframe, text = '2 Pass', command = add2)


threePassesButton = Button(mainframe, text = '3 Pass', command = add3)


zeroPassesButton = Button(mainframe, text = '0 Pass', command = addShank)


digsButton = Button(mainframe, text = 'Dig', command = addDig)


blocksButton = Button(mainframe, text = 'Block', command = addBlock)

blockedButton = Button(mainframe, text = 'Blocked', command = addBlocked)

blockErrorsButton = Button(mainframe, text = 'Block Errors', command = addBlockError)

alertVar = StringVar()
alertVar.set('No changes made yet')
alertLabel = Label(mainframe, textvariable = alertVar)

playerNumVar = StringVar()
playerNameVar = StringVar()
playerNameVar.set("")
playerNameLabel = Label(mainframe, textvariable = playerNameVar, font = ("Arial 12 bold"))

errorVar = StringVar()
errorVarLabel = Label(mainframe, textvariable = errorVar)
playerEntry = Entry(mainframe)
playerEntry.insert(END, "Jersey Number")
playerEntry.bind("<Return>", changePlayer)

undoButton = Button(mainframe, text = 'Undo', command = undo)

checkStatsButton = Button(mainframe, text = 'Check Stats', command = printList)
endButton = Button(mainframe, text = 'End', command = lambda: end(categories, statline))
checkFlowButton = Button(mainframe, text = 'Check Flow', command = lambda: showFlow(gameFlow))


mainframe.grid(padx=50, pady=50)
IRLabel.grid(row=1, column=1)
teamVsConfirmLabel.grid(row=2, column=1, padx=50)
teamVsEntry.grid(row=2, column=2, padx=50, sticky=E+W)
teamVsConfirmButton.grid(row=2, column=3, padx=50, pady=20)
hitsButton.grid(row=6, column=1, ipadx=15, ipady=15)
killsButton.grid(row=7, column=1, ipadx=15, ipady=15)
errorsButton.grid(row=8, column=1, ipadx=15, ipady=15, pady = 40)
servesinButton.grid(row=6, column=2, ipadx=15, ipady=15)
servesoutButton.grid(row=7, column=2, ipadx=15, ipady=15)
acesButton.grid(row=8, column=2, ipadx=15, ipady=15)
onePassesButton.grid(row=6, column=3, ipadx=15, ipady=15)
twoPassesButton.grid(row=7, column=3, ipadx=15, ipady=15)
threePassesButton.grid(row=8, column=3, ipadx=15, ipady=15)
zeroPassesButton.grid(row=6, column=4, padx=50, ipadx=15, ipady=15)
digsButton.grid(row=7, column=4, ipadx=15, ipady=15)
blocksButton.grid(row=8, column=4, ipadx=15, ipady=15)
playerNameLabel.grid(row=3, column=2)
playerEntry.grid(row=3, column=1)
alertLabel.grid(row=3, column=3, columnspan=2, padx=50, pady=40)
blockedButton.grid(row = 5, column = 4, ipadx = 10, ipady = 10)
blockErrorsButton.grid(row = 5, column = 3, ipadx = 10, ipady = 10)
oppErrorsButton.grid(row = 5, column = 6, ipadx=10, ipady=10)
oppPointsButton.grid(row=5, column=5, ipadx=10, ipady=10)
checkStatsButton.grid(row = 7, column = 5, ipadx=15, ipady=15)
checkFlowButton.grid(row = 7, column = 6, ipadx = 15, ipady = 15)
endButton.grid(row=6, column=5, ipadx=50, padx=50, ipady=50, pady=10)
undoButton.grid(row = 6, column = 6, ipadx = 50,  ipady = 50)
