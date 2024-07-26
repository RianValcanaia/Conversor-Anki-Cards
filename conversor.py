import csv
import argparse

def txt_to_anki_csv(txt_file, csv_file, delimiter=';', line_break='\\n'):
    try:
        with open(txt_file, 'r', encoding='utf-8') as infile, open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            blocks = infile.read().strip().split('\n\n')

            for block in blocks:
                if delimiter in block:
                    parts = block.split(delimiter, 1)
                    
                    if len(parts) == 2:
                        front, back = parts
                        
                        back = back.replace(line_break, '\n')
                        
                        if front.strip() and back.strip():
                            writer.writerow([front.strip(), back.strip()])
                    else:
                        print(f"Formato incorreto no bloco: {block}")
                else:
                    print(f"Delimitador ausente no bloco: {block}")

        print(f"Conversão concluída com sucesso. Arquivo salvo em: {csv_file}")
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {txt_file}")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    parser = argparse.ArgumentParser(description='Converte um arquivo de texto para um arquivo CSV no formato Anki.')
    parser.add_argument('txt_file', type=str, help='Caminho para o arquivo de texto de entrada.')
    parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV de saída.')
    parser.add_argument('--delimiter', type=str, default=';', help='Delimitador usado no arquivo de texto.')
    parser.add_argument('--line_break', type=str, default='\\n', help='Sequência usada no arquivo de texto para representar quebras de linha.')
    
    args = parser.parse_args()

    txt_to_anki_csv(args.txt_file, args.csv_file, delimiter=args.delimiter, line_break=args.line_break)

if __name__ == '__main__':
    main()
