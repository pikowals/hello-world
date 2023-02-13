#! python3
import shelve,pyperclip,sys
mcbShelf = shelve.open('mcb')                               # otwieramy stały słownik na dysku twardym do zapisu i odczytu
if len(sys.argv) == 3 and sys.argv[1].lower() =='save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for k,v in mcbShelf.items():
            del mcbShelf[k]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()