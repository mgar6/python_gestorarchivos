import os
import argparse

def main():
    args = parser.parse_args()
    #argsDiccionario = vars(args) 
    #print(argsDiccionario)  

    parser.add_argument('-cf', '--create-file')
    parser.add_argument('-rf', '--read-file')
    parser.add_argument('-df', '--delete-file')
    parser.add_argument('-cd', '--create-directory') 
    parser.add_argument('-lc', '--list-contents',)
    parser.add_argument('-dd', '--delete-directory')
    
    if args.create_directory:
        create_directory(args.create_directory)

    if args.list_contents:
          list_contets(args.list_contents)

    if args.delete_directory:
        delete_directory(args.delete_directory)

    if args.create_file:
          create_file(args.create_file)

    if args.read_file:
        read_file(args.read_file)
       
    if args.delete_file:
          delete_file(args.delete_file)
          
def create_directory(myPath):
    if not os.path.exists(myPath):
        os.makedirs(myPath)

def list_contents(myPath):
    if os.path.exists(myPath):
        #print(os.listdir(mmyPath))) #otra opcion
            for elemento in os.scandir(myPath):
                print(elemento)  

def delete_directory(myPath):
    if os.path.exists(myPath):
        os.rmdir(myPath)

def create_file(fileName):
    newFile = open(fileName, 'a')
    newFile.close()     

def read_file(fileName):
    newFile = open(fileName, 'r')
    print(newFile.read())

def delete_file(fileName):
    os.remove(fileName)

if __name__ == '__main__':
    main()

 