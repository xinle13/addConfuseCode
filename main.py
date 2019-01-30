
import os
import addRename
import addRubbishCode
import modifyAssetsMd5
import modifypngname

def main():
    os.system("python3 addRename.py")
    addRubbishCode.addRubbish()
    modifyAssetsMd5.modifyAssetsPNG()
    modifypngname.modifyPngName()
    print('add spam code finished!!')

if __name__ == '__main__':
    main()
