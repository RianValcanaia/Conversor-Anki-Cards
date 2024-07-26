# Conversor de Texto para CSV (Formato Anki)

Este script em Python converte um arquivo de texto em um arquivo CSV no formato Anki, facilitando a criação de cartões para estudos.

## Funcionalidades

- Converte blocos de texto separados por duas novas linhas (`\n\n`) em entradas CSV.
- Usa um delimitador (por padrão, `;`) para separar a frente e o verso do cartão.
- Substitui uma sequência específica (por padrão, `\n`) por quebras de linha reais no verso do cartão.

## Como Usar

### Pré-requisitos

- Python 3.x
- Biblioteca `csv`

### Execução


Para executar o script, utilize a linha de comando conforme o exemplo abaixo:



<!-- 
```bash
python script.py <caminho_para_arquivo_txt> <caminho_para_arquivo_csv> [--delimiter <delimitador>] [--line_break <quebra_de_linha>] -->


### Argumentos
* txt_file: Caminho para o arquivo de texto de entrada.
* csv_file: Caminho para o arquivo CSV de saída.
* --delimiter: (Opcional) Delimitador usado no arquivo de texto. Padrão é ;.
* --line_break: (Opcional) Sequência usada no arquivo de texto para representar quebras de linha. Padrão é \n.

### Exemplo
'''
python script.py entrada.txt saida.csv --delimiter ";" --line_break "\\n"
'''

Formato do arquivo de texto:
'''
frente1;verso1\\nlinha2
frente2;verso2\\nlinha2
frente3;verso3
'''