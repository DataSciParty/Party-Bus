# Welcome
Straight out of the [DataSciParty](http://DataSciParty.github.io) workshop, pumping noise into an otherwise peaceful suburb near you: Welcome to the Party Bus!

## Installation

To get on the Party Bus, you can install using the following command:

	pip install git+https://github.com/DataSciParty/Party-Bus.git

## Usage

### `load`

Provide an open data URL such as the one below, get back a pandas `DataFrame` with the contents. Magic! ✨

	>>> import partybus as pb
	>>>
	>>> data = pb.load('http://data.gov.au/dataset/asic-credit-licensee')
	>>> type(csv)
	<class 'pandas.core.frame.DataFrame'>

## To-Do

1. Everything as described [here](http://peterdowns.com/posts/first-time-with-pypi.html)
2. ???

## Contributors

[Blair Hudson](http://github.com/blairhudson)