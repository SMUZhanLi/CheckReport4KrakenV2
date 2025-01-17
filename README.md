# CheckReport4KrakenV2: Check and fixed null taxonomic levels for report of kraken V2

## :newspaper: Description

See, https://github.com/jenniferlu717/Bracken/issues/296.

## :arrow_double_down: Usage

``` Shell
python3 check_kraken2_report.py check_kraken2_report.py -i kraken.report -d KrakenDatabase/standard -o new.report
```
Note: (i) The 'kraken.report' is report file from kraken V2. (ii) The 'KrakenDatabase/standard' is the path of reference database for kraken V2 and it contains a file named 'ktaxonomy.tsv'.

