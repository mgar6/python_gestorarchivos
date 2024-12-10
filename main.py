import os
import argparse

if __name__ == '__main__':
     parser = argparse.ArgumentParser(description='Gestor de archivos')
     parser.add_argument('-cf', '--create-file')
     parser.add_argument('-rf', '--read-file')
     parser.add_argument('-df', '--delete-file')
     parser.add_argument('-cd', '--create-directory') 
     parser.add_argument('-lc', '--list-contents',)
     parser.add_argument('-dd', '--delete-directory')

     args = parser.parse_args()
     #argsDiccionario = vars(args) 
     #print(argsDiccionario)  
	
     if args.create_directory:
          mypath = args.create_directory
          if not os.path.exists(mypath):
               os.makedirs(mypath)

     if args.list_contents:
          mypath = args.list_contents
          if os.path.exists(mypath):
          #print(os.listdir(mypath)) #otra opcion
               for elemento in os.scandir(mypath):
                    print(elemento)  
			
     if args.delete_directory:
          mypath = args.delete_directory
          if os.path.exists(mypath):
               os.rmdir(mypath)
			
     if args.create_file:
          fileName = args.create_file
          newFile = open(fileName, 'a')
          newFile.close()

     if args.read_file:
          fileName = args.read_file
          newFile = open(fileName, 'r')
          print(newFile.read())

     if args.delete_file:
          ileName = args.delete_file
          os.remove(fileName)