# Mouse Virtual

Com este sistema de mouse virtual, é possível controlar o cursor do mouse com a ajuda da câmera integrada no seu computador ou webcam externa. Além disso, o usuário pode realizar cliques com gestos simples, tornando o processo de navegação mais intuitivo e natural.

![Mao1](https://user-images.githubusercontent.com/81125536/232862028-0ae77373-80c9-4010-aad2-568b5dc86213.png)

Construído utilizando-se a linguagem de programação Python com bibliotecas utilizadas para visão computacional e um módulo que integra as funções da biblioteca mediapipe o qual encontrei junto a recursos tecnológicos da [CV Zone](https://www.computervision.zone/).

## :wrench: Como utilizar

Após estar com os arquivos em seu computador, instale as bibliotecas necessárias utilizando pip no arquivo requeriments.txt:
      
      pip install -r requirements.txt

Execute o arquivo HandMouse.py:

      python HandMouse.py
      
Os movimentos do ponteiro do mouse são guiados pelo ponto verde no inicio do dedo médio. O retaângulo verde na tela delimita o tamanho da tela, porporcionando moviemtar menos a mão para abranger o tamanho total da tela.

A função que permite utilizar os cliques do mouse é acionada com a posição da mão conforme imagem abaixo:

![Click1](https://user-images.githubusercontent.com/81125536/232878386-8a43ab55-6bea-4289-81e2-d95fdd86a2de.png)

Perceba que na posição inferior esquerda da tela aparece uma mensagem "Click Ativado", indicando que a função está ativa. No momento em que essa posição for feita novamente a função é desativada.

Os cliques funcionam da seguinte forma:

  * Click botão esquerdo: abaixando o dedo indicador
  * Click botão direito: abaixando o dedo médio
  * Pressionar: Fechando a mão
 
 OBS.: A mão deve sempre estar na posição vertical em frente a câmera para funcionar corretamente conforme as imagens acima.
 
 Para fechar a aplicação pessione a tecla **q** em seu teclado.

## :hammer: Construindo um executável com Pyinstaller

Execute:

      pyinstaller HandMouse.py
      
O pyinstaller permite a utilização de alguns parâmetros que pode ser usados para sua configuração desejada, como por exemplo:

      --onefile # para gerar apenas um arquivo, o executável que encontra-se na pasta dist, que será criada.
      --windowed # para esconder a janela do terminal

Nesse caso específico pode acontecer de o pyinstaller não encontrar o mediapipe sendo necessário informar o caminho que ele deve buscar para implementar no .exe gerado. Pode-se utilizar a seguinte opção para informar onde o arquivo mediapipe deve ser buscado:

     --add-data "local\onde\encontrar\mediapipe;mediapipe"
 

