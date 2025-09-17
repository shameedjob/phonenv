# Phonenv

Phonenv is a Python library for dealing with word pluralization.
## Input File
Input files should be a list of words with each entry having it's own line.

## CLI Usage

### Find a phoneme
Look for all environments surrounding a character or substring in a selected file.
Each line in the file is treated as a unique entry.
```bash
> python3 phonenv_cl.py analyze 'a' --filename 'data/input.txt'
================================
Local Env       (Count)  Words
================================
b__#            (1)      (&c)ib[a]
n__#            (1)      (&c)in[a]
m__#            (1)      (&z)im[a]
#__(&z)         (1)      [a](&z)imola
l__#            (2)      a(&z)imol[a], tobol[a]
#__l            (1)      [a]loha
h__#            (1)      aloh[a]
#__w            (1)      [a]wesome
k__s            (1)      k[a]su
k__#            (1)      kesok[a]
t__n            (1)      t[a]nu
g__#            (1)      zeng[a]
```
filename is an optional parameter, the default file is located in the data folder of this repository.

### Special characters
In case there are characters that can't be represented in a standard text file, you can define special characters. These special characters are also stored in the data folder in this workspace.
```bash
python3 phonenv_cl.py add_special '&z'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## License

[MIT](https://choosealicense.com/licenses/mit/)
