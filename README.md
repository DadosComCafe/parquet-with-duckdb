# Handle Parquet
Um repositório cujo objetivo é de explorar o uso do formato parquet com o framework duckdb

## Como usar

### __1. Clone o repositório:__
Com um servidor aberto na raiz do repositório, rodar:
    
    git clone https://github.com/DadosComCafe/parquet-with-duckdb.git
e entre na raíz do projeto:
    
    cd parquet-with-duckdb

### __2. Configure seu ambiente:__
Com o terminal aberto na raíz do projeto, rode para configurar seu ambiente virtual python com uv:

    uv sync

Com isso, um diretório chamado .venv será criado na raiz do projeto. Este diretório contem o ambiente python isolado.

### __3. Crie os diretórios dos arquivos, input e output:__
Para este projeto, é necessário que haja um arquivo .csv no diretório __csv_files__, para que um arquivo no parquet seja criado no diretório __parquet_files__. Para a execução do script de conversão, é necessário que os dois diretório sejam previamente criados. Portanto, com o terminal aberto na raíz do projeto, execute:

    mkdir csv_files && mkdir parquet_files

### __4. Rode os scripts python:__
Como a ideia deste projeto é de algo simples, foi utilizado na criação dos scripts, a lib builtin argparse. Com ela, é possível a passagem de parâmetros através da linha de comando. Logo, para a execução do script __convert_csv.py__, rode (dado que é necessário que haja um arquivo .csv em csv_files):

    uv run convert_csv.py csv_files/meu_input.csv parquet_files/meu_output.parquet
E para a executar o script __read_parquet.py__ rode (dado que é necessário que haja um arquivo parquet dentro de parquet_files):

    uv run read_parquet.py parquet_files/offers-1000.parquet


## Documentação
 * ### Formato parquet:
    * https://parquet.apache.org/docs/

 * ### Framework duckdb:
    * https://duckdb.org/docs/current/

