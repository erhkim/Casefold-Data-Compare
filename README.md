# README

A script to quickly compare two sources of same valued columns using `casefold()` for true caseless comparison.
Mainly used so that I could find intersecting values in a column of Excel to a result of SSMS quickly.

Complements nimbletext.

## Usage

Copy-paste data (newline separated) in _sourceA and the compared data to _sourceB and run the script:

```
python ./main.py
```

### Example Output

```
Number of unique elements in A: 1683
Number of unique elements in B: 1683
Number of intersecting elements in A and B: 1683
Number of elements in A but not in B: 0
Number of elements in B but not in A: 0
Number of non-intersecting elements : 0
Is A a subset of B: True
Is B a subset of A: True
```
