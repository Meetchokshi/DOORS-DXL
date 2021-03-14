import WriteFile
import SearchFiles
import os
if __name__ == '__main__':
    pwd = os.getcwd()
    print(pwd)
    SearchFiles.Scan_Configuration()
