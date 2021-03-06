
try:
    import backend as be
    import multiplat as mp
    import os
    from os import path
    import webbrowser
except:
    print("Biblioteca necessária não disponível.\n\nEstamos finalizando.")
    quit()

if(mp.eh_linux):
    try:
        import textract #para converter PDF em TXT
    except:
        mp.install_lib("textract")
        mp.restart_program()

# retorna string com conteúdo do PDF
def pdf2txt(fileName):
    if(mp.eh_linux):
        try:
            texto = textract.process(fileName).decode("utf-8")
        except Exception as e:
            be.registra_log_geral(str(e))
            texto = ""
        texto = texto.replace("\\n", "\n")
        return texto
    elif(mp.eh_windows):
        raise Exception("No windows, é OBRIGATÓRIO habilitar o modo CACHE.")
    else:
        raise Exception("Função não disponível para sua plataforma")

# retorna string com conteúdo do PDF
# Se $salvaCache, salva os arquivos em TXT na pasta .processados, ou lê de lá, caso já exista
# Se $forceRefresh, sobrescreve os arquivos se já existirem.
def getTxt(fileName, salvaCache, forceRefhesh):

    cachePath = ".tempProcess"
    if(salvaCache):
        if( not path.isdir(cachePath)):
            mp.mkdir(cachePath)
        tempName = path.join(cachePath, fileName.replace(mp.dirSep, "__") + ".txt")
        if( (not forceRefhesh) and path.isfile(tempName)):
            with open(tempName, 'rt') as file:
                texto = file.read()
        else:#precisa ser atualizado
            if(mp.eh_linux):
                with open(tempName, 'wt') as file:
                    texto = pdf2txt(fileName)
                    file.write(texto)
            elif(mp.eh_windows):
                os.system(f"pdftotext \"{fileName}\" \"{tempName}\"")
                with open(tempName, "rt") as file:
                    texto = file.read()
            else:
                raise Exception("Função não disponível para sua plataforma.")
    else:
        texto = pdf2txt(fileName)

        
    return texto
            

# Retorna todos os arquivos encontrados no diretório dir e seus subdiretórios
def filesList(dir, extencao):
    caminhos = [os.path.join(dir, nome) for nome in os.listdir(dir)]
    arquivos = []
    for item in caminhos:
        if(path.isfile(item)):
            if(item.lower().endswith(f".{extencao}".lower())):
                arquivos.append(item)
        else:
            arquivos += filesList(item, extencao)
    return arquivos


# Pesquisar $text(string) nas CHAVES E NOS VALORES do $dic(dicionário)
# RETURN: array com strings encontradas
def pesquisa_dict(dic, text):
    resp = []
    for chave in dic:
        if(text == "" or text in chave or text in dic[chave]):
            resp.append(chave)
    return resp


def finder():
    try:
        import readchar #para ler caractere único
    except:
        mp.install_lib('readchar')
        mp.restart_program()

    #Configurações
    configFile = "config.ini"
    if( not path.isfile(configFile)):#se não existe arquivo de configurações, o cria
        with open(configFile, "wt") as file:
            file.write("""mode	cache
cachemode	ram
ResultPrint	50
TamPrint	120""")
    config = be.appConfig(configFile)
    ResultPrint = int(config.get("ResultPrint"))
    TamPrint = int(config.get("TamPrint"))

    print("Listando arquivos...")
    arquivos = filesList(be.__dir__, "pdf")

    if(config.get('mode') == 'cache' and config.get('cachemode') == 'ram'):
        cache = {}
        cont = 0
        total = len(arquivos)
        for arquivo in arquivos:
            mp.limpar_terminal()
            print(f"Processando o conteúdo dos arquivos... {cont}/{total}")
            try:
                cache[arquivo] = getTxt(arquivo, True, False)
            except Exception as e:
                be.registra_log_geral(f"Erro ao carregar arquivo '{arquivo}'. e:{str(e)}")
            cont += 1

    pesquisa = ''
    repesquisa = False
    p = []#array com as CHAVES das opções condizentes com a pesquisa
    sel = -1#indice do ítem selecionado. -1 quando nenhum selecionado
    while True:
        mp.limpar_terminal()
        print("\n\n  By: William Pilger")
        print(f"\n Faça sua pesquisa: {pesquisa}\n")
        if(repesquisa):
            sel = -1
            p = pesquisa_dict(cache, pesquisa)
            repesquisa = False
            maxResultPrint = ResultPrint
        if(len(p) > 0):#reprinta a lista de itens coerentes
            index = 0
            i = 0
            for item in p:
                i += 1
                if(i > maxResultPrint):
                    break
                if(sel == index):
                    carac = '♦'
                else:
                    carac = ' '
                if(len(item)>TamPrint):
                    tam = len(item)
                    text = "[...]" + item[tam-TamPrint-5:tam]
                else:
                    text = item
                print(f" {carac} {text}")
                index += 1
        dig = readchar.readkey()
        if(dig == readchar.key.ESC or dig == '\x1b'):#esc
            be.sair(1)
        elif(dig == '\t' or dig == '\r'):#tab ou enter
            if(sel != -1):#existe um ítem selecionado
                try:
                    if(mp.eh_linux):
                        webbrowser.open(p[sel])
                    elif(mp.eh_windows):
                        mp.startfile(p[sel])
                    else:
                        raise Exception("Função ainda não disponível na sua plataforma.")
                except Exception as e:
                    be.registra_log_geral(f"Impossível abrir o arquivo solicitado. e:{str(e)}")
            else:
                maxResultPrint += 10
        elif(dig == readchar.key.UP):#seta pra CIMA
            if(sel > 0):
                sel -= 1
        elif(dig == readchar.key.DOWN):#seta pra BAIXO
            if(sel < len(p)):
                sel += 1
        elif(dig == readchar.key.RIGHT):#seta para DIREITA
            mp.limpar_terminal()
            print(cache[p[sel]])
            input()
        elif(dig == readchar.key.BACKSPACE or dig == '\x08'):#back space
            pesquisa = pesquisa[:-1]
            repesquisa = True
        else:
            pesquisa += dig
            repesquisa = True



if __name__ == "__main__":
    finder()