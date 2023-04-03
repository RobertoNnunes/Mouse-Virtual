# Mouse Virtual

Realize os principais movimentos do seu mouse utilizando a webcam e sua mão. 

Construído utilizando-se a linguagem de programação Python com bibliotecas utilizadas para visão computacional e um módulo que integra as funções da biblioteca mediapipe o qual encontrei junto a recursos tecnológicos da [CV Zone](https://www.computervision.zone/).

## :wrench: Como utilizar

Após estar com os arquivos em seu computador, instale as bibliotecas necessárias utilizando pip no arquivo requeriments.txt:
      
      pip install -r requirements.txt

Execute o arquivo HandMouse.py:

      python HandMouse.py

## :hammer: Construindo um executável com Pyinstaller

Execute:

      pyinstaller HandMouse.py
      
O pyinstaller permite a utilização de alguns parâmetros que pode ser usados para sua configuração desejada, como por exemplo:

      --onefile # para gerar apenas um arquivo, o executável que encontra-se na pasta dist, que será criada.
      --windowed # para esconder a janela do terminal

Nesse caso específico pode acontecer de o pyinstaller não encontrar o mediapipe sendo necessário informar o caminho que ele deve buscar para implementar no .exe gerado. Pode-se utilizar a seguinte opção para informar onde o arquivo mediapipe deve ser buscado:

     --add-data "local\onde\encontrar\mediapipe;mediapipe"
 

