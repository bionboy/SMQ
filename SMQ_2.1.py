def askQuestion(question):

    val = 101
    while (val > 100 or val < 0):
        while True:
            try:
                val = int(input(question))
            except ValueError:
                print("Please input a integer between 0 and 100.")
                continue
            else:
                break
            return val
    return val


def SMQ():  # def SMQ(mode): '','avg','data'

    data = open('smqLog.txt', 'a')
    print("\n ┌──────────────────────────────────────────────────────────────────────────────────────┐" +
          "\n │            This test claims no finality and should be viewed accordingly.            │" +
          "\n ├──────────────────────────────────────────────────────────────────────────────────────┤" +
          "\n │  For each parameter besides the initial the higher the value, the more moral it is.  │" +
          "\n └──────────────────────────────────────────────────────────────────────────────────────┘")
    LA = (input("{Consent} Do I have any reason to believe that " +
                "anyone involved here is or would be unwilling? [Yes/No]: "))
    while (LA.isalpha() != True):
            LA = input("Input text.")
    while (LA.upper() != 'YES' and LA.upper() != 'NO'):
            LA = input('Input Yes or no.')
    while (LA.upper() == 'YES'):
        print('Any form of sex without consent is immoral.')
        data.write('0\n')
        # data.write('0\n0\n0\n0\n0\n')
        break
    else:
        LAval = 1
        MC = askQuestion("If it weren’t sex would I act this way? [0-100]: ")
        SE = askQuestion("{Exploitation} Would this be happening if they" +
                         "weren’t in such a state of misfortune? [0-100]: ")
        TP = askQuestion("{Third Party} (Am I/Are we) affecting anyone " +
                         "who is not involved? [0-100]: ")
        SC = askQuestion("{Social Context} (Am I/Are we) reproducing or " +
                         "reinforcing broader social injustices? [0-100]: ")
        smq = LAval * (MC + SE + TP + (SC/2))
        # data.write('1\n')
        # data.write(str(MC) + '\n')
        # data.write(str(SE) + '\n')
        # data.write(str(TP) + '\n')
        # data.write(str(SC) + '\n')
        data.write(str(smq) + '\n')
        print(str(LAval) + ' * (' + str(MC) + ' + ' + str(SE) + ' + ' +
              str(TP) + ' + (' + str(SC) + '/2))' + ' = ' + str(smq))
        data.write('\n')
        data.close()
SMQ()
# add file logging
# add an arguement to SMQ() that will either run the questions...
# or show you the data.
