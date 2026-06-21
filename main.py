import duckdb
import argparse

def convert_csv_to_parquet(input_path_file: str, output_file: str) -> bool:
    """_summary_

    Args:
        input_path_file (str): _description_
        output_file (str): _description_

    Returns:
        bool: _description_
    """
    duckdb.execute(
    f"COPY (SELECT * FROM read_csv_auto('{input_path_file}', delim=',')) TO '{output_file}' (FORMAT PARQUET);"
    )

if __name__ == "__main__":
    # 1. Cria o objeto do parser
    parser = argparse.ArgumentParser(
        description="Converte um arquivo CSV (delimitador ',') para Parquet usando DuckDB."
    )

    # 2. Define os argumentos que o terminal deve aceitar
    parser.add_argument(
        "input_file", type=str, help="Caminho do arquivo CSV de entrada."
    )
    parser.add_argument(
        "output_file", type=str, help="Caminho do arquivo Parquet de saída."
    )

    # 3. Faz o parse dos argumentos da linha de comando
    args = parser.parse_args()

    # 4. Chama a sua função passando os argumentos capturados
    sucesso = convert_csv_to_parquet(
        input_path_file=args.input_file, output_file=args.output_file
    )

    # Opcional: Feedback visual baseado no retorno booleano da sua função
    if sucesso:
        print("Conversão concluída com sucesso!")
    else:
        print("Falha na conversão.")
