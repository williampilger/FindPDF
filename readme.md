# PDF Finder (em desenvolvimento)

Este script auxilia na pesquisa em pastas com inúmeros arquivos PDF. A pesquisa é feita em todos os arquivos do doretório e subdiretórios.

**Ps**: Embora funcione no **windows**, ferramenta desenvolvida primeiramente para **Linux**, sistema no qual o desempenho atualmente é muito maior.
Para compatibilizar com o windows foi necessária uma ferramenta externa que tem baixa eficiência.

## Instalação

Tanto no windows quanto no linux a compilação da aplicação não funciona, e atualmente a única solução é a cópia de todos os arquivos para o diretório onde se deseja realizar a pesquisa.

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
