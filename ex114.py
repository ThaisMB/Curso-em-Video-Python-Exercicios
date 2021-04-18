import urllib
import urllib.request
from time import sleep
import webbrowser

try:
    site=urllib.request.urlopen('http://pudim.com.br/')

except urllib.error.URLError:
    print('\033[31mO site Pudim está sendo acessado com sucesso.\033[m')

else:
    print('\033[32mO site pudim está acessível no momento.\033[m')
    print(site.read())
    print('Abrindo o site em 3...2...1...')
    webbrowser.open('http://pudim.com.br/')