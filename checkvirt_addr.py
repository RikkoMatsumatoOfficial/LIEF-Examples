import lief
import os
def Main():
    lief.disable_leak_warning()
    pe_bin = lief.parse("C:\\Windows\\explorer.exe")
    for pe_section_expl in pe_bin.sections:
        print(pe_section_expl.virtual_address)
        print(pe_section_expl.size)
        print("This Example is Created by RikkoMatsumatoOfficial!!!")
        os._exit(334)

if __name__ == "__main__":
    Main()
