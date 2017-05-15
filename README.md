# The Party Bus has arrived! 🎉🚌
Straight out of the [DataSciParty](http://DataSciParty.github.io) workshop, pumping noise into an otherwise peaceful suburb near you: **Welcome to the Party Bus!**

## Installation

### From PyPI

🚌 To get on the Party Bus, you can install using the following command:

	pip install partybus

### From Git

🚌 If you like to live on the wild side, you can install Party Bus from the git repo using the following command:

	pip install git+https://github.com/DataSciParty/Party-Bus.git

## Usage

### `load`

Provide an open data URL such as the one below, get back a pandas `DataFrame` with the contents. Magic! ✨

```python
>>> import partybus as pb
>>>
>>> data = pb.load('http://data.gov.au/dataset/asic-credit-licensee')
>>> type(data)
<class 'pandas.core.frame.DataFrame'>
```

## License

BSD

## Want to contribute?

This is the todo list for improving the magic loader 👇:

1. JSON file support
2. Better error handling when no files are found
3. Better handling when multiple compatible files are found
4. Remove package dependencies

## Contributors

[Blair Hudson](http://github.com/blairhudson)