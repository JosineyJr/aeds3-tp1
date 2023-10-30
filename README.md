# Trabalho Prático 1

Este projeto envolve a implementação e análise de diferentes algoritmos de busca, incluindo busca sequencial, busca em árvore binária e busca em árvore AVL. O objetivo é comparar o desempenho desses algoritmos em diferentes cenários, como dados ordenados e não ordenados, e quando a chave de busca está presente ou ausente.

Os dados para a busca são carregados de arquivos CSV, e o desempenho de cada algoritmo é avaliado em termos do número de comparações realizadas e do tempo gasto. Os resultados são então visualizados em gráficos e tabelas, que são gerados automaticamente pelo programa e salvos em arquivos PNG e PDF, respectivamente.

## Pré-requisitos

- Python 3 ou superior
- Variável de ambiente com o nome 'python' que execute o python em uma das versões citadas acima
- Make instalado na máquina

## Instalação

Para instalar as dependências do projeto, execute:

```bash
make install
```

Ou:

```bash
pip install -r requirements.txt
```

## Execução

Para rodar o projeto, execute:

```bash
make run
```

Ou:

```bash
python src/main.py
```

## Relatório

Esta presente no diretório "reports". Sendo divido por pasta para cada estrutura de dado. Na raiz, esta presente o arquivo "relatorio.pdf" que contém a tabela com os dados obtidos da execução mais recente.