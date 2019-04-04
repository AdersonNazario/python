import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    resultado=0
    for x in range(len(as_a)) :
        resultado+=abs(as_a[x]-as_b[x])
    resultado /=6
    return resultado
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    sal_calculo = 0
    pal_calculo = 0
    wal_calculo = 0
    for s in sentencas :
        sal_calculo+=len(s)
        frases +=separa_frases(s)
    for f in frases :
        pal_calculo +=len(f)
        palavras +=separa_palavras(f)
    for p in palavras :
        wal_calculo+=len(p)
    wal_calculo /=len(palavras)
    ttr_calculo = n_palavras_diferentes(palavras) / len(palavras)
    hlr_calculo = n_palavras_unicas(palavras) / len(palavras)
    sal_calculo /=len(sentencas)
    sac_calculo = len(frases)/len(sentencas)
    pal_calculo /=len(frases)
    return [wal_calculo, ttr_calculo, hlr_calculo, sal_calculo, sac_calculo, pal_calculo]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    as_a=calcula_assinatura(textos[0])
    r = compara_assinatura(as_a,ass_cp)
    x=1
    retorno = x
    for x in range(len(textos)) :
        as_a = calcula_assinatura(textos[x])
        if r > compara_assinatura(as_a, ass_cp) :
            retorno=x+1
    return retorno

def main() :
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos,ass_cp)
    print("O autor do texto", avalia_textos(textos,ass_cp),"está infectado com COH-PIAH")
