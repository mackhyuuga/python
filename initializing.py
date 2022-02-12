import subprocess 
import time

list =['/home/mack/Livros/Einstein gravity in a nutshell ( PDFDrive ).pdf',
    '/home/mack/Livros/Spacetime and Geometry_ An Introduction to General Relativity ( PDFDrive ).pdf',
    '/home/mack/Livros/MECANICA ANALITICA - NIVALDO LEMOS.pdf',
    '/home/mack/Livros/pós-graduação/Lições de Física de Feynman - Volume 1 - Mecânica, Radiação e Calor -  Richard P. Feynman.pdf',
    '/home/mack/Livros/pós-graduação/Fundamentos_de_Mecanica_Vol_2_Renato_Bri.pdf',
    '/home/mack/Livros/pós-graduação/Análise Combinatória e Probabilidade - Morgado.pdf',
    '/home/mack/Livros/pós-graduação/1000_Solved_Problem_in_Modern_Physics.pdf'
]

program = ['rstudio']



for file in list:
    subprocess.Popen(['xdg-open', file])
    time.sleep(1)


for program in program:
    subprocess.Popen(program)
    time.sleep(1)