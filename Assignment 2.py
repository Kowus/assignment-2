#Nana Ama Atombo-Sackey
#22nd September,2017
#Assignment 2
#Data Structures and Algorithm

class RedoUndoStack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def printMenu():
    print('I understand the following commands:\n'+
      'ADD <value>\nSUBTRACT <value>\n'+
      'MULTIPLY <value>\nDIVIDE <value>\n' +
      'UNDO\nREDO\nEND\n')

# Read a command any arguments
def readCommand(self):
    command = input('Please enter a command: ')
    args = command.lower().split()
    return args

  
# The main program
def main():
    redo= RedoUndoStack()
    undo= RedoUndoStack()
    
    x = float(input('Pick a starting number. '))
    print('Your starting value is ' + str(x))
    undo.push(x)
    while (args[0] != 'end'):
        if (args[0] == 'add'):
            x = x + float(args[1])
            undo.push(x)
        elif (args[0] == 'subtract'):
            x = x - float(args[1])
            undo.push(x)
        elif (args[0] == 'multiply'):
            x = x * float(args[1])
            undo.push(x)
        elif (args[0] == 'divide'):
            x = x / float(args[1])
            undo.push(x)
        elif (args[0] == "undo"):
            x= x/float(args[1])
            

        print('Executed ' + ' '.join(args) +
              ': Current value is ' + str(x))
        args = stack.readCommand()
        stack.push(args)

    print('Your final value was',x)
    print('Goodbye!')

main()



        
        
        







