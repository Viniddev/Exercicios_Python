import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLerror:
    print('O site não está acessivel no momento')
else:
    print('O site está disponível')
    print(site.read())