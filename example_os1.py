import os
import shutil

print(os.getcwd())

# print(os.path.exits('movies'))

if os.path.exists('movies'):
    print("present")
else:
    os.mkdir('movies')

os.chdir(r'/home/vector/xpad/python/movies')
open('abc.txt','w').close()
os.chdir(r'/home/vector/xpad/python')

print(os.listdir())

for item in os.listdir():
    print(os.path.join(os.getcwd(),item))
    
print(os.walk(os.getcwd()))

fileitr =  os.walk(os.getcwd())

shutil.rmtree('movies')
os.makedirs('movies/new')
os.makedirs('movies/doc')
os.chdir(r'/home/vector/xpad/python/movies')
open('abc.txt','w').close()
os.chdir(r'/home/vector/xpad/python')
shutil.copytree('movies','movies/doc1')
shutil.copy('movies/abc.txt','movies/doc1/abc.txt')
shutil.move('movies/abc.txt','movies/abc11.txt')



for path,folder,file_name in fileitr:
    print(f'Current path {path} have folder {folder} and file {file_name}')

# os.rmdir('movies')
shutil.rmtree('movies')