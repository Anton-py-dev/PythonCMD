import emoji

from FileCounter import FileCounter


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def printOSinfo(osInfo):
    print('Your system is:', osInfo.system, emoji.emojize(':thumbs_up:'))
    print('Version:', osInfo.version, emoji.emojize(':thumbs_up:'))
    print('Processor:', osInfo.processor, emoji.emojize(':thumbs_up:'))


if __name__ == '__main__':
    FC = FileCounter()
    printOSinfo(FC.osInfo())
    inp = ""

    while inp != "exit":
        FC.printCurrDir()
        inp = input().split(" ")

        try:
            if "cd" in inp:
                FC.cd(inp[1])
            if "ls" in inp:
                FC.ls()
            if "mkdir" in inp:
                FC.mkdir(inp[1])
            if "del" in inp:
                FC.delete(inp[1])
        except:
            print("The syntax of the command is incorrect.")
