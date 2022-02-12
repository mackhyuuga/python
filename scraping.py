import requests
from bs4 import BeautifulSoup


url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
print(html)

for questions in html.select('.question-summary'):
    titulo = questions.select_one('.question-hyperlink')
    data = questions.select_one('.relativetime')
    votos = questions.select_one('.vote-count-post')

    print(data.text, titulo.text, votos.text, sep='\t')