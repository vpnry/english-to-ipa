# to-ipa.py

Convert English text to IPA using `python3` and Python module [eng_to_ipa](https://pypi.org/project/eng-to-ipa/)

## Install

+ System requirements: `python3`, and module `eng_to_ipa`
+ On Ubuntu, install Python3 with:

```bash
sudo apt install python3
```

And **eng_to_ipa** module:

```bash
pip3 install eng_to_ipa
```

## Usase

+ In Terminal CLI:

```bash
# insert IPA paragraphs follows English paragraphs
python3 to-ipa.py input.txt 1

# insert IPA transcription next to each word
python3 to-ipa.py input.txt 0
```

+ For function call: 

```python3
toIPA(f, 1) # insert IPA paragraphs follows English paragraphs
toIPA(f, 0) # insert IPA transcription next to each word
```

## Example

```bash
python3 to-ipa.py input.txt 1
```


+ Input file `input.txt` content:

```text
Adapted from https://en.m.wikipedia.org/wiki/Computer
A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. 

Modern computers have the ability to follow generalized sets of operations, called programs. These programs enable computers to perform an extremely wide range of tasks.
```

We should get this output file:

+ Output file `_ipa_input.txt` (in current directory)

```text
[1] Adapted from https://en.m.wikipedia.org/wiki/Computer

[1] əˈdæptɪd frəm https://en.m.wikipedia.org/wiki/computer*

[2] A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming.

[2] ə kəmˈpjutər ɪz ə məˈʃin ðət kən bi ˌɪnˈstrəktɪd tɪ ˈkɛri aʊt ˈsikwənsɪz əv ˌɛrɪθˈmɛtɪk ər ˈlɑʤɪkəl ˌɑpərˈeɪʃənz ˌɔtəˈmætɪkli ˈviə kəmˈpjutər ˈproʊˌgræmɪŋ.

[3] 

[3] 

[4] Modern computers have the ability to follow generalized sets of operations, called programs. These programs enable computers to perform an extremely wide range of tasks.

[4] ˈmɑdərn kəmˈpjutərz hæv ðə əˈbɪləˌti tɪ ˈfɑloʊ ˈʤɛnərəˌlaɪzd sɛts əv ˌɑpərˈeɪʃənz, kɔld ˈproʊˌgræmz. ðiz ˈproʊˌgræmz ɪˈneɪbəl kəmˈpjutərz tɪ pərˈfɔrm ən ɪkˈstrimli waɪd reɪnʤ əv tæsks.
```