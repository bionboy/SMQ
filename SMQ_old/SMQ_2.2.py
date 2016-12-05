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
    print("\n ┌────────────────────────────────────────────────────────────┐" +
          "\n │               This test claims no finality.                │" +
          "\n ├────────────────────────────────────────────────────────────┤" +
          "\n │ Based off of the Sexuality Morality Quotient put forth by  │" +
          "\n │                  Raymond A. Belliotti                      │" +
          "\n └────────────────────────────────────────────────────────────┘")
    LA = (input("Do the partys involved provide voluntary and " +
                "informed consent?\n[Yes/No]: "))
    while (LA.isalpha() != True) or \
            (LA.upper() != 'YES' and LA.upper() != 'NO'):
        LA = input('Input Yes or no.')
    if (LA.upper() == 'NO'):
        print('Any form of sex without consent is immoral.')
        data.write('0\n')
    else:
        LAval = 1
        MC = askQuestion("If it weren’t sex would I act this way?\n[0-100]: ")
        SE = askQuestion("Would this be happening if they" +
                         "weren’t in a state of misfortune?\n[0-100]: ")
        TP = askQuestion("(Am I/Are we) affecting anyone " +
                         "who is not involved?\n[0-100]: ")
        SC = askQuestion("(Am I/Are we) reproducing or " +
                         "reinforcing broader social injustices?\n[0-100]: ")
        smq = LAval * (MC + SE + TP + (SC/2))
        data.write(str(smq) + '\n')
        print(str(LAval) + ' * (' + str(MC) + ' + ' + str(SE) + ' + ' +
              str(TP) + ' + (' + str(SC) + '/2))' + ' = ' + str(smq))
        data.write('\n')
        data.close()
SMQ()
# add file logging and an arguement to SMQ() that will either run the...
# questions or show you the data.
