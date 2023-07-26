# Working with the BACI dataset

This repository contains scripts for working with the CEPII BACI trade dataset. It shows how the yearly csv files can be compiled into one table and exported as a space-efficient [Parquet](https://parquet.apache.org/) file. It also demonstrates how this may be queried and manipulated with SQL using [DuckDB's](https://duckdb.org/) Python API.

## About BACI

The [BACI](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37) (*Base pour l’Analyse du Commerce International*) dataset is an annual record of bilateral merchandise trade flows published by the French think tank [CEPII](http://www.cepii.fr/CEPII/en/cepii/cepii.asp) (*Centre d’Etudes Prospectives d’Informations Internationales*). Flows are recorded at the product level according to different editions of the [Harmonized System](https://www.wcoomd.org/en/topics/nomenclature/overview.aspx). The dataset builds from the raw entries found in [UN COMTRADE](https://comtradeplus.un.org/), fixing as much as possible missing and inconsistent data (Gaulier and Signago 2010). 

Each BACI table is a csv file corresponding to one year of trade. It has the following columns:

- `t`: year
- `i`: ISO numeric code of the exporting country
- `j`: ISO numeric code of the importing country
- `k`: HS product code
- `v`: value of trade flow in thousands of USD
- `q`: weight of trade flow in metric tons

Each row is therefore the dollar amount `v` of product `k` sent by country `i` to country `j` in the year `t`. Dictionaries for the country and product codes are included when downloading an edition of BACI. Note that `q` is missing in about 2% of entries.

## Scripts

The following are the notebooks contained in this repo.

| Notebook | Description |
| -------- | ----------- |
| [`1-save-to-parquet.ipynb`](1-save-to-parquet.ipynb)| Compiles yearly BACI csv files into one table and exports it as a Parquet file. |
| [`2-aggregate.ipynb`](2-aggregate.ipynb) | Aggregates the BACI dataset to the 4-digit, 2-digit, and country levels. |
| [`3-summary-stats.ipynb`](3-summary-stats.ipynb) | Compiles summary statistics for datasets generated. |

## References

G. Gaulier and S. Signago. (2010). [BACI: international trade database at the product-level. The 1994-2007 version.](http://www.cepii.fr/PDF_PUB/wp/2010/wp2010-23.pdf) *CEPII Working Paper No. 2010-23*.
## Citing

```bibtex
@misc{ksreyes2023baciscripts,
    title = {{Working with the BACI dataset}},
    author = {{Kenneth S. Reyes}},
    url = {https://github.com/ksreyes/baci},
    year = {2023},
}
```