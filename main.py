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
    try:
        duckdb.execute(
            f"COPY (SELECT * FROM read_csv_auto('{input_path_file}', delim=',')) TO '{output_file}' (FORMAT PARQUET);"
        )
        return True
    except Exception as e:
        print(f"Deu ruim no duckdb: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converte um arquivo CSV (delimitador ',') para Parquet usando DuckDB."
    )

    parser.add_argument(
        "input_file", type=str, help="Caminho do arquivo CSV de entrada."
    )
    parser.add_argument(
        "output_file", type=str, help="Caminho do arquivo Parquet de saída."
    )

    args = parser.parse_args()

    sucesso = convert_csv_to_parquet(
        input_path_file=args.input_file, output_file=args.output_file
    )

    if sucesso:
        print("Conversão concluída com sucesso!")
    else:
        print("Falha na conversão.")
