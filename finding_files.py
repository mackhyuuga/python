import os 

path = '/home/mack/Livros'
search_for = 'física'

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

counter = 0
for root, directories, files in os.walk(path):
    for file in files:
        if search_for in file:
            try:
                counter += 1
                full_path = os.path.join(root, file)
                file_name, ext_file = os.path.splitext(file)
                size = os.path.getsize(full_path)
                print('file found:', file)
                print('file path:', path)
                print('name:', file_name)
                print('extension:', ext_file)
                print('size:', size)
                print('formatted size:', format_size(size))
                print(end='\n\n')
            except PermissionError as e:
                print('without permission')
            except  FileNotFoundError as e:
                print('File not found')
            except Exception as e:
                print('unknown error')

print(f'{counter} files were found')







    

