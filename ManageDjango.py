#!/usr/bin/python

import sqlite3
import os
import configparser

def openFile(env):
    f = open(str(env), 'r')
    lines = f.readlines()
    for l in lines: 
        r = l.strip()

        os.chdir(r)

print('You are changed directory the new is {}'.format(os.getcwd()))
print('--------------------------')

def chooseFile():
    global file
    b=True

    while b:
        file = input("\nWhat is the name of the file for database ?\nsqlite3> ")
        sql = 'sqlite3'
        text = file.split(".")
        if text[1] == sql:
            b = False
        else:
            print("Use a file with extention sqlite3")

    print('')

def connectFile():
    c=os.system("ls {}".format(file))
    if c == 0:
        boolean = True
        con = sqlite3.connect(file) 
        cursor = con.cursor()
        while boolean:
            database = input("sqlite3> ")
            command = database.split(' ')
            if command[0] == 'use':
                global data
                data = command[1]

                try:
                    print(data)
                    query = con.execute("SELECT * FROM {}".format(data))
                    t = query.fetchall()
                    e = '\nYou are connect to table\n--------------------------\n'
                    boolean = False

                except sqlite3.Error:
                    e = '\nNot found table \'{}\''.format()

                    if not file == "db.sqlite3":
                        os.system("rm {}".format(file))

                print(e)
            elif command[0] == "show":
                if command[1] == "tables":
                    c = cursor.execute("select name from sqlite_master where type = 'table';")
                    for test in c.fetchall():
                        ls = test[:2]
                        print(ls)
                elif not command[1] == "tables":
                    print("Not found option '{}'".format(command[1]))
            else:
                error = database
                print("Command not found '{}'".format(error))       

        def insert():
            title = input("What's Title: ")
            path = input("What's image path: ")
            body = input("What's body: ")
            url = input("What's the url: ")
            timeCourse = input("What's time of course: ")
            mode = input("What's the difficulty: ")
            query = con.execute("INSERT INTO "+data+"(title, path, body, time, mode, url) values('"+title+"', '"+path+"', '"+body+"', '"+timeCourse+"', '"+mode+"', '"+url+"')")
            con.commit()
            print("Succefuly add !")
            con.close()
        
        insert()

    else:
        os._exit(1)

if __name__ == "__main__":
    openFile(".env")
    chooseFile()
    connectFile()