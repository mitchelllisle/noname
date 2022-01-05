##  noname

> 1️⃣ version: 0.1.0

> ✍️ author: Mitchell Lisle

📛 An experimental data anonymisation library

## Install

```shell
pip install noname
```

## Usage

```python
from noname import Anonymiser, AusPostCode, AusDriversLicence

anonymiser = Anonymiser(info_types=[AusPostCode, AusDriversLicence])

# returns an AnonymisedText Object with metadata and information and text replaced with a like-for-like example
anonymised = anonymiser.anonymise('Milhouse Van Houten 2203 18423441')
anonymised.text # Milhouse Van Houten 7862 R90715
```

The `AnonymisedText` object contains all information about what was matched. The
example below shows `matches` that we found with some information about where in the string they occurerd.
`info_types` is a list of all info_types that we looked for in the given string.

```python
AnonymisedText(
    original='Milhouse Van Houten 2203 18423441',
    text='Milhouse Van Houten 7862 R90715',
    matches=[
        Match(text='2203', start=20, end=24, len=4, type=<class 'noname.info_types.AusPostCode'>),
        Match(text='18423441', start=25, end=33, len=8, type=<class 'noname.info_types.AusDriversLicence'>)
    ],
    info_types=[
        <class 'noname.info_types.AusPostCode'>,
        <class 'noname.info_types.AusDriversLicence'>
    ]
)

```
