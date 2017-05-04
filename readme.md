
# Bloom filter based spell checker

## Code Kata Problem

[Code Kata problem](http://codekata.com/kata/kata05-bloom-filters/)

This repository contains an implementation of bloom filter based spell checker. I have used the wordlist from the code kata problem above. For hashing, I have used murmurhash3 in python. The bitarray size chosen in this case is a tradeoff between false positive rate and performance of the program.


### Prerequisites

```
Python  > = 2.7

pip install -r requirements.txt
```

### Installation steps

1.  Install Prerequisites
2. Run the following command

```
python spellcheck.py

```

### Testing

 ```
python test.py
 ```
