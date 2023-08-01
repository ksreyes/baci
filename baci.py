import os
import duckdb

def baci_to_parquet(hs, release, input_folder='raw', output_folder='final'):

    # Determine input path
    
    baci_folder = f'BACI_{hs}_V{release}'
    
    if input_folder is not None:
        input_path = os.path.join(input_folder, baci_folder)
    else:
        input_path = baci_folder
    
    # Determine output file

    if output_folder is not None:

        output_file = os.path.join(output_folder, f'{baci_folder}.parquet')

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    
    else:
        output_file = f'{baci_folder}.parquet'
    
    # Compile all BACI tables into one table

    duckdb.sql(f"COPY( SELECT * FROM read_csv_auto('{input_path}/BACI*.csv') ) TO '{output_file}'")

    # Report result

    if output_folder is not None:
        print(f"'{baci_folder}.parquet' successfully saved in '{output_folder}'.")
    else:
        print(f"'{baci_folder}.parquet' successfully saved in project root.")

def aggregate_baci(input, output, aggregation='country'):

    if aggregation == '2digit':
        duckdb.sql(
            f"""
            COPY (
                SELECT t, i, j, k2, SUM(v) AS v
                FROM (SELECT t, i, j, SUBSTRING(k, -6, 2) AS k2, v FROM '{input}')
                GROUP BY t, i, j, k2
                ORDER BY t
            ) TO '{output}'
            """
        )

    elif aggregation == '4digit':
        duckdb.sql(
            f"""
            COPY (
                SELECT t, i, j, k4, sum(v) AS v
                FROM (SELECT t, i, j, substring(k, -6, 4) AS k4, v FROM '{input}')
                GROUP BY t, i, j, k4
                ORDER BY t
            ) TO '{output}'
            """
        )

    else:
        duckdb.sql(
            f"""
            COPY (
                SELECT t, i, j, SUM(v) AS v
                FROM '{input}'
                GROUP BY t, i, j
                ORDER BY t
            ) TO '{output}'
            """
        )