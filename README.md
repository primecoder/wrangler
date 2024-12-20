# wrangler
Data wrangler - like Jeep Wrangler, it 'wrangling' data ;-)

## Dependencies

### Python 3
Python3! Can't leave home without it. If you see something like 3 or newer, you are good to go.

```bash
python3 --version
Python 3.9.6
```

### JQ

This is a super tool to process and view JSON files from CLI. 
Highly recommended.

```bash
brew install jq
```

### Pandas

Many scripts from this repo use Pandas.

```bash
pip3 install pandas
```

## Project: csvmerge

Merge 2 CSV files with uneven columns.
For example:
- file1 has columns: A, B, E.
- file2 has columns: C, D
- output file will have columns: A, B, C, D, E

This script can produce output file in CSV and JSON formats.

Sample usage:

This one writes output in CSV format to standard console.

```bash
./csvmerge.py --file1 test1.csv --file2 test2.csv 
```

To produce output in JSON, use:


```bash
./csvmerge.py --file1 test1.csv --file2 test2.csv --outtype json
```

You can use JQ to beautify the JSON output, i.e.

```bash
./csvmerge.py --file1 test1.csv --file2 test2.csv --outtype json | jq -C '.' | less
```

To save the outputs, you can redirect them to a file, i.e.

```bash
./csvmerge.py --file1 test1.csv --file2 test2.csv > out.csv
./csvmerge.py --file1 test1.csv --file2 test2.csv --outtype json > out.json
```





