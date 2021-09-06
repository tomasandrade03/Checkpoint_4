Checkpoint_4 - Ransomware Cifra de Caesar

O script tem o objetivo de buscar um arquivo com a extensão ".txt" na máquina do usuário, criptografar e descriptografar o conteúdo. Foi desenvolvido e debugado em uma VM Linux.
O usuário, antes de rodar o código, deve criar um arquivo txt no Desktop da máquina e escrever um texto para ser criptografado.

As bibliotecas necessárias para o desenvolvimento do script foram:

![image](https://user-images.githubusercontent.com/83794673/132261014-09f070fb-207f-4535-a231-ff7047a9618d.png)

Essa variável é criada para determinar as extensões de arquivos que serão buscadas.

![image](https://user-images.githubusercontent.com/83794673/132261106-99af269b-8b1b-4c73-8ee7-a0cdb54535ec.png)

O Desktop será acessado e uma verificação nos arquivos será feita.

![image](https://user-images.githubusercontent.com/83794673/132261227-930210a6-bedb-4f3f-9abc-fd0b5e2f5418.png)

Nessa etapa, há uma verificação para saber se existem arquivos no Desktop que correspondem à extensão que está sendo buscada (.txt). Quando o arquivos é encontrado, o nome dele é
printado e ele é aberto. É pedida a chave de criptogtrafia para que ela possa ser executada. A partir disso, o conteúdo do arquivo é lido e criptografado.

![image](https://user-images.githubusercontent.com/83794673/132261261-d2babebd-d281-4fb9-9676-42aaebd7fe1c.png)

O resultado da criptografia é transcrito para o arquivo, substituindo seu conteúdo anterior.

![image](https://user-images.githubusercontent.com/83794673/132261272-96ea1e7a-3f7a-4e18-b116-b4944cc85187.png)

Após a criptografia ser finalizada, uma senha para liberação e descriptografia do arquivo é pedida. Caso o usuário digite a senha correta, o processo inverso da criptografia
ocorre e então o conteúdo criptografado é substituído pelo conteúdo original, que estava presente anteriormente no arquivo. Caso contrário, uma mensagem será exibida dizendo que a
senha não está correta e então o usuário não poderá descriptografar seu arquivo.

![image](https://user-images.githubusercontent.com/83794673/132261318-5007b062-bc4d-4e01-91a0-ed63c2f0312a.png)


FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Fábio Henrique Cabrini
Atividade: Checkpoint 1 - 2º Semestre
Alunos:
Gabriel Anselmo Pires Dos Santos - RM87010
Tomás Esteves Andrade - RM89081
