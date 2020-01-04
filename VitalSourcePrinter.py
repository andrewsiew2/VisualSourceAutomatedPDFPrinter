
try:   
    import PyPDF2
    import pyautogui
    import os
    import sys
    import time
    import warnings
    from tkinter import *
    import tkinter.filedialog as filedialog
except:
    print("Please install PyPDF2 and pyautogui. Refer to video or documentation for help")
    sys.exit()

def main():

    start_time = time.time() 
    warnings.filterwarnings("ignore") #Gets rid of harmless warnings on the console for excess whitespace

  
    print("Welcome to the VitalSource Ebook Printer. \n")
    NumberStart = 1
    NumberEnd = 2

    while(True):
        try:
            NumberStart = int(input("First page: "))
            NumberEnd = int(input("Last page: "))
            if (type(NumberStart) != int) or (type(NumberStart) != int):
                print("Please enter valid numbers.\n")
                continue
            elif (NumberStart > NumberEnd):
                print("First page must be less than last page.\n")
                continue                    
            else:
                break          
        except:
            print("Please enter valid page numbers.\n")

    NumberList = []
    for i in range(int(NumberStart), int(NumberEnd)+1):
        NumberList += [ str(i) ]

    # root = Tk()
    # root.withdraw()
    # root.overrideredirect(True)
    # root.geometry('0x0+0+0')
    # root.deiconify()
    # root.lift()
    # root.focus_force()
    # # credits to http://stackoverflow.com/questions/3375227/how-to-give-tkinter-file-dialog-focus

    # filedir = filedialog.askdirectory() + '//'

    if len(NumberList)%2 != 0 :
        NumberList += [ NumberList[-1] ]

    print("\nClick on the active VitalSource window to get started.\nThe program will start in: 8")
    for seconds in range(8):
        time.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
        
    for x in range(NumberStart, NumberEnd, 2):
        
        PageEntry1 = str(x)
        PageEntry2 = str(int(x) + 1)

        #16 tabs
                #enter
                #tab
                #page 1
                #tab
                #page 2
                #tab enter
                # wait 6
                # 18 tabs
                #enter 
                #enter
                # page number_ pagenumber 2.pdf
                #enter
                # 5 tabs
                # 1 tab
                # enter rightx2
                # tab x4

        # pyautogui.press('tab', 16, interval = 0.1)
        pyautogui.click(x=1471, y=977)
        pyautogui.moveTo(500, 500)
        time.sleep(0.2)
        pyautogui.press('tab')
        pyautogui.press('delete')
        time.sleep(0.2)
        pyautogui.typewrite(PageEntry1)
        time.sleep(0.2)
        pyautogui.press('tab')
        pyautogui.press('delete')
        time.sleep(0.2)
        pyautogui.typewrite(PageEntry2)
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('enter')

        time.sleep(10)

        pyautogui.click(x=1771, y=238)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        print(PageEntry1 + "_" + PageEntry2)
        pyautogui.press('delete')
        pyautogui.typewrite(PageEntry1 + "_" + PageEntry2 + ".pdf")
        time.sleep(0.2)
        pyautogui.press('enter')

        # pyautogui.hotkey('ctrl', 'p')
        # pyautogui.press(keys = 'tab', presses = 2, interval = 0.25)
        # pyautogui.press('delete', 5)
        # pyautogui.typewrite(PageEntry1)
        # pyautogui.press('tab')
        # pyautogui.press('delete', 5)
        # pyautogui.typewrite(PageEntry2)
        # pyautogui.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
        # pyautogui.typewrite("Ebook", interval = 0.50)
        # pyautogui.press('enter', interval = 0.5)
        time.sleep(0.70)

   
    print("\nDone!")
    print("This took " + "%.2f" % (elapsed_time/3600) + " hours.")

if __name__ == "__main__": main()


