import os
import subprocess
import csv

Index = 0
ASPICE_LEVEL = ''
ASPICE_LEVEL_Down = ''
ASPICE_LEVEL_SourcePath = ''
ASPICE_LEVEL_SourcePath_ALLFiles = False
ASPICE_LEVEL_Down_SourcePath = ''
ASPICE_LEVEL_Down_SourcePath_ALLFiles = False
ASPICE_LEVEL_SourcePath_Files = []
ASPICE_LEVEL_Down_SourcePath_Files = []
ASPICE_LEVEL_SearchString = ''
ASPICE_LEVEL_Down_SearchString = ''


def Scan_Configuration():
    with open('config.csv') as config_file:
        csv_reader = csv.reader(config_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                ASPICE_LEVEL = row[1]
                ASPICE_LEVEL_SourcePath = row[2]
                ASPICE_LEVEL_SourcePath_ALLFiles = row[3]
                if ASPICE_LEVEL_SourcePath_ALLFiles.find('-') != -1:
                    ASPICE_LEVEL_SourcePath_Files = row[4]
                ASPICE_LEVEL_SearchString = row[9]
                ASPICE_LEVEL_Down = row[5]
                ASPICE_LEVEL_Down_SourcePath = row[6]
                ASPICE_LEVEL_Down_SourcePath_ALLFiles = row[7]
                if ASPICE_LEVEL_Down_SourcePath_ALLFiles.find('-') != -1:
                    ASPICE_LEVEL_Down_SourcePath_Files = row[8]
                ASPICE_LEVEL_Down_SearchString = row[10]
                line_count += 1
        print(f'Processed {line_count} lines.')
    print(ASPICE_LEVEL)
    print('\n')
    print(ASPICE_LEVEL_SourcePath)
    print('\n')
    print(ASPICE_LEVEL_SourcePath_ALLFiles)
    print('\n')
    print(ASPICE_LEVEL_SearchString)
    print('\n')
    print(ASPICE_LEVEL_Down)
    print('\n')
    print(ASPICE_LEVEL_Down_SourcePath)
    print('\n')
    print(ASPICE_LEVEL_Down_SourcePath_ALLFiles)
    print('\n')
    print(ASPICE_LEVEL_Down_SearchString)
    print('\n')
