from zipfile import ZipFile
import os 


class closing:
    def __init__(self, starting_path, ending_path, name):
        self.starting_path = starting_path
        self.ending_path = ending_path
        self.name = name
    
    def zip(self):
        with ZipFile('/'.join((self.ending_path, self.name)), 'w') as zip:
            for file in os.listdir(self.starting_path):
                full_path = os.path.join(self.starting_path, file)
                zip.write(full_path, file)

    def show(self):
        with ZipFile('/'.join((self.ending_path, self.name)), 'r') as zip:
            for file in zip.namelist():
                print(file)

    def extract(self, name = None):
        if name == None:
            name = 'unzipped'
        with ZipFile('/'.join((self.ending_path, self.name)), 'r') as zip:
            zip.extractall('/'.join((self.ending_path, name)))





if __name__ == "__main__":


    c1 = closing('/home/mack/Documents/code/JavaScript', '/home/mack/Documents/code/python/', 'arquivo')
    c1.zip()
    c1.show()
    c1.extract()