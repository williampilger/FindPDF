# PDF Finder

Este script auxilia na pesquisa em pastas com inúmeros arquivos PDF. A pesquisa é feita em todos os arquivos do doretório e subdiretórios.

## Instalação

**Linux**

Basta sair usando, o pacote instala as dependências sozinho.

**Windows**

No windows, a aplicação ainda não funciona.
Existem algumas dependências que precisam ser instaladas **manualmente**, veja o passo-a-passo:

- Instale o **Anaconda**
    - Baixe o instalador preferido do [site oficial](https://docs.conda.io/en/latest).
    - Execute o instalador, e **instale para todos os usuários**
    - Marque a opção **Adicionar ao PATH do windows**
- Instale o **Swig**, **poppler** e **pkg-config** usando o conda
    - Abra o CMD **como administrador** e digite:
    - > conda install swig
    - > conda install poppler
    - > conda install pkg-config
- Instalar **Ebooklib**
    - Baixe o repositório [EbookLib](https://github.com/aerkalov/ebooklib) como ZIP
    - Extraia todo o conteúdo
    - Abra o CMD, e navegue até dentro da pasta do repositório extraido
    - > pip install .
- Instale os pacotes necessários (isso pode ser ignorado, na maior parte dos casos, se você estiver no windows 10)
    - Abra o CMD e digite:
    - > pip install textract
    - Se o comando acima **NÃO FUNCIONAR**, tente adicionar ` --user` ao final do comando e repetir

## Configuração

Juntamente com o script (ou executável, em caso de aplicação compilada), salve um arquivo nomeado `config.ini` com as configurações, uma por linha.

- **mode**
    - `cache` - Para que os arquivos sejam processados todos ANTES da pesquisa.
    - `real-time` - Para que a carga ocorra durante a pesquisa
- **cachemode**
    - `ram` - Para carregar e manter todos os arquivos na RAM
    - `hibrido` - Para manter uma quantidade limitada de dados na RAM
    - `real-time` - Não mantém nenhum dado retido na RAM
- **ResultPrint**
    - INT, que representa a quantidade de resultados que aparecem inicialmente
- **TamPrint**
    - INT, que representa a quantidade de caracteres de LARGURA que a tela tem.
