import lief
import os
def Main():
    lief.disable_leak_warning()
    pe_bin = lief.parse("C:\\Windows\\explorer.exe")
    for peb in pe_bin.sections:
        print(peb.virtual_address)
        print(peb.size)
        print("This Example is Created by RikkoMatsumatoOfficial!!!")
        os._exit(334)

if __name__ == "__main__":
    Main()