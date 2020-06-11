import pygame
from random import choice

branco = (255, 255, 255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)


pygame.init()

relogio = pygame.time.Clock()
janela = pygame.display.set_mode((940,780))
pygame.display.set_caption('jogo da forca')


def texto(msg, cor, fundo, tam, x, y): #função para colocar texto na tela
    fonte = pygame.font.SysFont('arial', tam)
    texto1 = fonte.render(msg, True, cor, fundo)
    janela.blit(texto1, [x, y])


def boneco(erros):
    pygame.draw.rect(janela, preto, [20, 50, 10, 500])             #parte do poste da forca
    pygame.draw.rect(janela, preto, [20, 50, 200, 10])             #parte do poste da forca
    pygame.draw.rect(janela, preto, [210, 60, 10, 30])             #parte do poste da forca
    if erros >= 1:
        pygame.draw.circle(janela, vermelho, [215, 110], 20)           #cabeça do boneco
    if erros >= 2:
        pygame.draw.rect(janela, vermelho, [210, 130, 10, 150])        #tronco do boneco
    if erros >= 3:
        pygame.draw.line(janela, vermelho, [190, 190], [210, 130], 10) #braço esquerdo do boneco
    if erros >= 4:
        pygame.draw.line(janela, vermelho, [240, 190], [220, 130], 10) #braço direito do boneco
    if erros >= 5:
        pygame.draw.line(janela, vermelho, [190, 340], [215, 280], 10) #perna esquerda do boneco
    if erros >= 6:
        pygame.draw.line(janela, vermelho, [240, 340], [215, 280], 10) #perna direta do boneco


def jogo():
    aberto = True
    text = '' #selecionar a letra
    resposta = ''
    erros = 0
    acertos =[] #coloca a quantidade de letras na tela e ver se a letra ta certa com o chute
    chutes = [] #todas as letras chutadas
    for x in palavra:
        if x == '-':   #para os '-' não precisarem ser chutados
            acertos.append('-')
        elif x == ' ':   #para os espaços não precisarem ser chutados
            acertos.append('-')
        else:          #para as letras aparecerem como '_' e precisar adivinhar
            acertos.append('_')

    palavra_sem_acento = ''  # para não diferenciar uma letra acentuada
    for p in palavra:
        if p in 'ãâáà':
            palavra_sem_acento += 'a'
        elif p in 'êéè':
            palavra_sem_acento += 'e'
        elif p in 'íìî':
            palavra_sem_acento += 'i'
        elif p in 'õôóò':
            palavra_sem_acento += 'o'
        elif p in 'ûúù':
            palavra_sem_acento += 'u'
        elif p in 'ç':
            palavra_sem_acento += 'c'
        else:
            palavra_sem_acento += p

    while aberto:
        janela.fill(branco)

        boneco(erros)

        if erros == 6: #verifica se perdeu e aparece a mensagem de fim de jogo
            fim_de_jogo('Perdeu')
            aberto = False

        texto(text, preto, None, 30, 50, 650)
        texto('_', preto, None, 30, 50, 650)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #necessario para clicar no X e sair do jogo
                pygame.quit()
            if event.type == pygame.KEYDOWN:  #input da letra selecionada
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if text != '':
                        resposta = text
                        text = ''
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_SPACE:
                    text = text[:-1]
                elif event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:
                    pass
                else:
                    text = event.unicode

        for letra in range(len(palavra_sem_acento)):  #ver se a resposta esta certa ou errada
            if resposta == palavra_sem_acento[letra] and resposta not in chutes:
                acertos[letra] = palavra[letra]
            texto(acertos[letra], preto, verde, 30, letra * 50, 600)

        if resposta not in palavra_sem_acento and resposta not in chutes and resposta != '':
            #verifica se a resposta esta errada, não valendo letra já falada
            erros += 1
        if resposta not in chutes:
            chutes.append(resposta)
        resposta = ''

        for x in range(len(chutes)): #aparecer as letras já ditas
            texto(chutes[x], vermelho, None, 30, x * 20, 700)

        if '_' not in acertos: #verificar se ganhou e aparece a mensagem de fim de jogo
            fim_de_jogo('Ganhou')
            aberto = False

        pygame.display.update()
        relogio.tick(120)

def selecionar_palavra():
    aberto = True
    palavra = ''

    while aberto:
        janela.fill(branco)

        texto('Qual palavra para a forca', azul, verde, 60, 50, 220)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #necessario para clicar no X e sair do jogo
                pygame.quit()
            if event.type == pygame.KEYDOWN:  #input para inserir a palavra
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    aberto = False
                elif event.key == pygame.K_BACKSPACE:
                    palavra = palavra[:-1]
                elif event.key == pygame.K_UNDERSCORE:
                    pass
                else:
                    palavra += event.unicode
        palavra = palavra.replace('_', '-').lower()

        pygame.draw.line(janela, vermelho, [50, 295], [600, 295], 10)
        texto(palavra, preto, verde, 60, 50, 300)
        pygame.draw.line(janela, vermelho, [50, 370], [600, 370], 10)

        pygame.display.update()
        relogio.tick(120)
    return palavra


def menu():
    aberto = True
    numero = ''

    while aberto:
        janela.fill(branco)

        texto('FORCA DA COVID19', branco, preto, 60, 240, 50)
        texto('1 - Jogar com palavras pre existentes', preto, None, 60, 50, 120)
        texto('2 - Escolher a palavra', preto, None, 60, 50, 190)
        texto('selecione outra tecla para sair', preto, None, 60, 50, 260)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #necessario para clicar no X e sair do jogo
                pygame.quit()
            if event.type == pygame.KEYDOWN:  #input para inserir o numero
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    aberto = False
                elif event.key == pygame.K_BACKSPACE:
                    numero = numero[:-1]
                else:
                    numero = event.unicode

        texto(numero, preto, vermelho, 60, 50, 500)

        pygame.display.update()
        relogio.tick(120)
    return numero


def fim_de_jogo(vitoria_derrota):

    tempo = 0   #para marcar o tempo é sair depois de um determinado numero
    aberto = True
    while aberto:
        janela.fill(azul)

        texto(vitoria_derrota, branco, None, 60, 350, 50)
        texto(f'A palavra é {palavra}', branco, None, 60, 50, 120)
        explicacao()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #necessario para clicar no X e sair do jogo
                aberto = False

        pygame.display.update()
        relogio.tick(120)

        tempo += 1
        if tempo == 500:
            aberto = False


def explicacao(): #complemento da função fim_de_jogo
    def texto_explicacao(*textos): #para poder escrever mais de uma linha
        for n in range(len(textos)):
            texto(textos[n], branco, None, 30, 50, 200 + 40 * n)

    if palavra == 'vírus':
        texto_explicacao('O covid-19 é um virus contagioso, podendo causar até a morte')

    if palavra == 'contágio':
        texto_explicacao('O covid-19 é muito contagioso. Temos que tomar as preucações',
                         'necessárias para evitar o contagio e impedir que o vírus espalhe')

    if palavra == 'tratamento':
        texto_explicacao('Até o momento (junho de 2020), não há vacinas,',
                         'ou medicamentos específicos para a COVID-19.',
                         'Os tratamentos estão sendo investigados ',
                         'e serão testados por meio de estudos clínicos')

    if palavra == 'saúde':
        texto_explicacao('Mesmo sendo uma pessoa saudavel, é possivel',
                         'contrair o COVID19. E os sintomas podem aparecer',
                         'em qualquer individuo independente da idade ou saúde')

    if palavra == 'pandemia':
        texto_explicacao('Em 11 de março de 2020 o COVID19 se tornou uma pandemia.',
                         'Isto é se espalhou em diversas regiões do mundo',
                         'se tornando uma preocupação em nivel global')

    if palavra == 'solidariedade':
        texto_explicacao('A solidariedade nesses tempo de pandemia é algo',
                         'essencial para que possamos superar esse tempo dificil.',
                         'Mesmo a distancia, devemos nos unir')

    if palavra == 'prevenção':
        texto_explicacao('Ainda (junho de 2020) não existe vacinas ou cura',
                         'para o COVID19, então a prevenção é o melhor remédio')

    if palavra == 'higiene':
        texto_explicacao('A higienização é uma forma eficiente de',
                         'combater o contágio do COVID19 e também de',
                         'outros virus ou bactérias. Lave bem as maões')

    if palavra == 'conscientização':
        texto_explicacao('Atravez da conscientização e da informação',
                         'podemos evitar situações de risco para contrair',
                         'doenças')

    if palavra == 'confinamento':
        texto_explicacao('A quarentena serve para que o virus COVID19',
                         'não se espalhe. Essencial para achatar a',
                         'curva de contaminação, isto é ter o menor',
                         'numero de contaminados ao mesmo tempo')

    if palavra == 'distanciamento':
        texto_explicacao('O distanciamento social se faz necessário',
                         'para evitar o contágio. Se necessário sair',
                         'para lugares com pessoas, use máscara')

    if palavra == 'máscara':
        texto_explicacao('A máscara ajuda a impedir que o virus se espalhe.',
                         'Sendo um item essencial para evitar tanto que uma',
                         'pessoa contaminada espalhe a doença e uma pessoa',
                         'saudável contraia ela')

    if palavra == 'álcool em gel':
        texto_explicacao('O álcool em gel é utilizado para higienizar as mãos',
                         'matando o vírus')

while True:
    try:
        num = menu()
    except:
        break
    if num == '1':
        palavras = ('vírus', 'contágio', 'tratamento', 'saúde', 'pandemia',
                    'solidariedade', 'prevenção', 'higiene', 'conscientização',
                    'confinamento', 'distanciamento', 'máscara', 'álcool em gel')
        palavra = choice(palavras)
        try:
            jogo()
        except:
            break
    elif num == '2':
        palavra = selecionar_palavra()
        jogo()
    else:
        break

pygame.quit()
