import os
from os.path import join 
import shutil 

class Folder:
    def __init__(self, path = '/'):
        self.path = path 
        self.root = []
        self.files = {}
        self.file = {}
        


    @property
    def path(self):
        return self._path    

    @path.setter
    def path(self, name):
        self.check(name)
        self._path = name

    @staticmethod
    def check(name):
        if not isinstance(name, str):
            raise TypeError('it need to be a string')
        

    @staticmethod
    def format_size(size):
        base = 1024
        kilo = base 
        mega = base ** 2
        giga = base ** 3
        tera = base ** 4 
        peta = base ** 5

        if size < kilo:
            text = 'B'

        elif size < mega:
            size /= kilo
            text = 'B'

        elif size < giga:
            size /= mega
            text = 'M'

        elif size < tera:
            size /= giga
            text = 'G'
        
        elif size < peta:
            size /= tera
            text = 'T'

        else:
            size /= peta 
            text = 'P'

        size = round(size, 2)
        return f'{size}{text}'
            
            

    def search(self):       
        for root, directories, files in os.walk(self.path):
            for file in files:
                full_path = os.path.join(root, file)
                file_name, ext_file = os.path.splitext(file)
                size = os.path.getsize(full_path)
                formated_size = self.format_size(size) 
                self.files.update({file_name: [full_path, ext_file, size, formated_size]})
        return root, directories, files

    def find(self, search_for):
        self.check(search_for)
        counter = 0
        for key, value in self.files.items():
            if search_for.lower() in key.lower():
                self.file.update({key: value})
                counter +=1
        return f'{counter} were found \n'


    def show(self):
        for key, value in self.file.items():
            print('file found:', key + value[1])
            print('file path:', value[0])
            print('name:', key)
            print('extension:', value[1])
            print('size:', value[2])
            print('formatted size:', value[3])
            print(end='\n\n')


    def move(self, new_path, original_path = None):
        if original_path == None:
            original_path = self.path 
            
        try:
            os.mkdir(new_path)
        except FileExistsError as e:
            print(f"the folder '{new_path}' already exist")

        for root, dirs, files in os.walk(original_path):
            for self.file in files:
                old_file_path = os.path.join(root, self.file)
                new_file_path = os.path.join(new_path, self.file)

                shutil.move(old_file_path, new_file_path)

        if len(self.file) > 0:
            print(f'File {self.file} has been moved successfully ')
        else:
            print('no files were moved')
        
        

if __name__ == '__main__':

    f1 = Folder('/home/mack/Livros')
    f1.search()
    print(f1.find('alge'))
    f1.show()

'''
f2 = Folder('/home/mack/Documents/chromedriver')
f2.move('/home/mack/Documents/test')

'''






