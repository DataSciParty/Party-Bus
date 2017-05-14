def load(url):
	import requests, json, pandas, bs4

	print('Looking up URL provided...')
	html = requests.get(url).content

	# turn html content into a beautiful soup (and find what we need)
	json_url = bs4.BeautifulSoup(html, 'html.parser').find(rel="alternate", type="application/json").get("href")

	print('Fetching metadata...')
	json_doc = json.loads(requests.get(json_url).text)

	csv_url = ''

	# there has to be a CSV in there somewhere
	for resource in json_doc["result"]["resources"]:
		if resource['format'] == 'CSV':

			# woohoo, found it!
			csv_url = resource['url']
			break

	if csv_url == '':
		raise Error('💥 No data found')

	print('Fetching actual data...')
	csv = pandas.read_csv(csv_url)

	print('Done!')
	return csv