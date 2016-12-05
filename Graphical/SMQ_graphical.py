from graphics import *


win = GraphWin("SMQ", 1000, 500)
win.setBackground('green')

def textInput (x, y, promptText, x1, y1):
    textBox = Rectangle(Point(100, 50), Point(900, 150))
    textBox.setFill('white')
    textBox.draw(win)
    textPrompt = Text(Point(x, y), promptText)
    textPrompt.draw(win)
    textField = Entry(Point(x1, y1), 50)
    textField.draw(win)
    win.getMouse()
    textPrompt.undraw()
    textIn = textField.getText()
    textBox.undraw()
    testText = Text(Point(500, 200), textIn)
    return textIn

def errorMessage ():
    message = "Please input a integer between 0 and 100."
    textInput(500, 100, message, 500, 400)
    
def SMQ():
    data = open('smqLog.txt', 'a')
    prompt1 = "{Consent} \n Do I have any reason to believe that " + \
              "anyone involved here is or would be unwilling? " + \
              "[Yes/No]: \n (Click on the window to continue)"
    LA = textInput(500, 100, prompt1, 500, 400)
    while LA.isalpha() != True:
        LA = textInput(500, 100, "Please input yes or no.", 500, 400)
    while LA.upper() != 'YES' and LA.upper() != 'NO':
        LA = textInput(500, 100, "Input Yes or no.", 500, 400)
    while LA.upper() == 'YES':
        textInput(500, 200, "Any form of sex without consent is immoral.", 500, 400)
        win.close()
        data.write('0\n')
        # data.write('0\n0\n0\n0\n0\n')
        break
    else:
        LAval = 1
        while True:
            try:
                prompt2 = "If it weren’t sex would I act this way? [0-100]: "
                MC = int(textInput(500, 100, prompt2, 500, 400))
            except ValueError:
                errorMessage()
                continue
            else:
                break
        while True:
            try:
                prompt3 = "{Exploitation} Would this be happening if " + \
                               "they weren’t in such a state of misfortune? [0-100]: "
                SE = int(textInput(500, 100, prompt3, 500, 400))
            except ValueError:
                errorMessage()
                continue
            else:
                break
        while True:
            try:
                prompt4 = "{Third Party} (Am I/Are we) affecting anyone who is not involved? [0-100]: "
                TP = int(textInput(500, 100, prompt4, 500, 400))
            except ValueError:
                errorMessage()
                continue
            else:
                break
        while True:
            try:
                prompt5 = "{Social Context} (Am I/Are we) reproducing " + \
                               "or reinforcing broader social injustices? [0-100]: "
                SC = int(textInput(500, 100, prompt5, 500, 400))
            except ValueError:
                errorMessage()
                continue
            else:
                break
        smq = LAval * (MC + SE + TP + (SC/2))
        # data.write('1\n')
        # data.write(str(MC) + '\n')
        # data.write(str(SE) + '\n')
        # data.write(str(TP) + '\n')
        # data.write(str(SC) + '\n')
        data.write(str(smq) + '\n')
        calculation = str(LAval) + ' * (' + str(MC) + ' + ' + str(SE) + ' + ' + str(TP) + \
              ' + (' + str(SC) + '/2))' + ' = ' + str(smq)
        textInput(500, 200, calculation, 500, 400)
        data.write('\n')
        data.close()
        win.close()


        
SMQ()
# add file logging
# add an arguement to SMQ() that will either run the questions or show you the data.
