import duckdb
import argparse


def read_parquet(input_parquet: str):
    try:
        print("\n--- Exibição Nativa do DuckDB ---")
        resultado_duck = duckdb.query(
            f"SELECT * FROM read_parquet('{input_parquet}')"
        )
        return(resultado_duck)

    except Exception as e:
        print(f"Erro ao ler o arquivo Parquet: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Lê um arquivo parquet"
        )

    parser.add_argument(
            "input_file", type=str, help="Caminho do arquivo parquet de entrada."
        )
    
    args = parser.parse_args()

    return_parquet = read_parquet(input_parquet=args.input_file)
    if return_parquet:
        print(return_parquet)
    else:
        print("Deu ruim!")