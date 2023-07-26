# Processing the BACI dataset

The [BACI](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37) is an annual dataset of bilateral merchandise trade flows at the product level. Compiled and maintained by the French think tank [CEPII](http://www.cepii.fr/CEPII/en/cepii/cepii.asp), it is a cleaned version of the [UN COMTRADE](https://comtradeplus.un.org/) dataset and is released with a two-year lag. Trade flows are disaggregated at the product level according to different editions of the [Harmonized System](https://www.wcoomd.org/en/topics/nomenclature/overview.aspx). More information on the BACI's construction is available at the CEPII website.

Each BACI table is a csv file corresponding to one year of trade. It has the following columns:

- `t`: year
- `i`: ISO numeric code of the exporting country
- `j`: ISO numeric code of the importing country
- `k`: HS product code
- `v`: value of trade flow in thousands of USD
- `q`: weight of trade flow in metric tons

Each row is therefore the dollar amount `v` of product `k` sent by country `i` to country `j` in the year `t`. Dictionaries for the country and product codes are included in the downloaded zip file.

## Scripts

This repo contains the following scripts to process the BACI files. The [DuckDB](https://duckdb.org/) Python API is used extensively.

| Notebook | Description |
| -------- | ----------- |
| [`1-save-to-parquet.ipynb`](1-save-to-parquet.ipynb)| Compiles yearly BACI csv files into one table and exports it as a Parquet file. |
| [`2-aggregate.ipynb`](2-aggregate.ipynb) | Aggregates the BACI dataset to the 4-digit, 2-digit, and country levels. |
| [`3-summary-stats.ipynb`](3-summary-stats.ipynb) | Compiles summary statistics for datasets generated. |

## Citing

```bibtex
@misc{ksreyes2023baciscripts,
    title = {{Working with the BACI dataset}},
    author = {{Kenneth S. Reyes}},
    url = {https://github.com/ksreyes/baci},
    year = {2023},
}
```