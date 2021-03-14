import os
import subprocess
import csv
import re


class Module:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


Index = 0
ASPICE_LEVEL = ''
ASPICE_LEVEL_Down = ''
ASPICE_LEVEL_SourcePath = []
ASPICE_LEVEL_SourcePath_ALLFiles = False
ASPICE_LEVEL_Down_SourcePath = []
ASPICE_LEVEL_Down_SourcePath_ALLFiles = False
ASPICE_LEVEL_SourcePath_Files = []
ASPICE_LEVEL_Down_SourcePath_Files = []
ASPICE_LEVEL_SearchString = ''
ASPICE_LEVEL_Down_SearchString = ''


def Scan_Configuration():
    MODULE_WITH_ALL_FILE_SCANS = []
    MODULE_WITH_FILE_BASED_SCANING = []
    with open('config.csv') as config_file:
        csv_reader = csv.reader(config_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                ASPICE_LEVEL = row[1]
                ASPICE_LEVEL_SourcePath.append(row[2])
                ASPICE_LEVEL_SourcePath_ALLFiles = row[3]
                print(row[3])
                if row[3] == '-':
                    MODULE_WITH_FILE_BASED_SCANING.append(row[2])
                    if row[4] == '':
                        print(
                            "Modules which are configured as FILES BASED SCAN cant have FILES NAME coloumn empty!")
                    ASPICE_LEVEL_SourcePath_Files = row[4]
                else:
                    MODULE_WITH_ALL_FILE_SCANS.append(row[2])
                    if row[4] != '':
                        print(
                            "Modules which are configured as ALL FILES SCAN cant have FILES NAME coloumn filled!")
        for MAFS in MODULE_WITH_ALL_FILE_SCANS:
            for MFS in MODULE_WITH_FILE_BASED_SCANING:
                if MAFS == MFS:
                    print(
                        MAFS + 'and' + MFS + 'are contradicting each other on ALL FILE scans vs FILE based configuration!')
        print(MODULE_WITH_ALL_FILE_SCANS)
    #             ASPICE_LEVEL_SearchString = row[9]
    #             ASPICE_LEVEL_Down = row[5]
    #             ASPICE_LEVEL_Down_SourcePath.append(row[6])
    #             ASPICE_LEVEL_Down_SourcePath_ALLFiles = row[7]
    #             if ASPICE_LEVEL_Down_SourcePath_ALLFiles.find('-') != -1:
    #                 ASPICE_LEVEL_Down_SourcePath_Files = row[8]
    #             ASPICE_LEVEL_Down_SearchString = row[10]
    #             line_count += 1
    #     print(f'Processed {line_count} lines.')
    # print(ASPICE_LEVEL)
    # print('\n')
    # print(ASPICE_LEVEL_SourcePath)
    # print('\n')
    # print(ASPICE_LEVEL_SourcePath_ALLFiles)
    # print('\n')
    # print(ASPICE_LEVEL_SearchString)
    # print('\n')
    # print(ASPICE_LEVEL_Down)
    # print('\n')
    # print(ASPICE_LEVEL_Down_SourcePath)
    # print('\n')
    # print(ASPICE_LEVEL_Down_SourcePath_ALLFiles)
    # print('\n')
    # print(ASPICE_LEVEL_Down_SearchString)
    # print('\n')


def Scan_SourceFile(path, files, regex):
    if files == []:
        for file in os.listdir(path):
            if file.endswith(".txt"):
                print(os.path.join(path, file))
                print(re.findall('TREACE{^}', file))
