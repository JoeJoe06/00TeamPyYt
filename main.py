from _funcs import installer,info,clear
from help import interFace , helpMessage
from os import system,name




if __name__ == "__main__":
    
    system("cls" if name == "nt" else "clear")
    print(interFace)
    
    
    while 1:
        try:
            userInput: str = input("arch@hostname:$ ")
            
            if "help" == userInput:
                print(helpMessage)
            elif "clear" == userInput:
                clear()
            elif "exit" == userInput:
                exit()
            elif "info" in userInput:
                info(userInput[5:])
            elif "install" in userInput:
                installer(userInput[8:])   
            
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
