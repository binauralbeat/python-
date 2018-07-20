stock_dict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]


def report(list=purchases, stocks=stock_dict):
	lump_sum = []
	for stock in list:
		name = stocks[stock[0]]
		value = "$" + str(stock[1] * stock[3])
		value_report.append({name, value})
	return value_report

def report_by_ticker(list=purchases, stocks=stock_dict):
	stock_names = {}
	for stock in list:
		name = stocks[stock[0]]
		value = stock[1]
		if name in tickers.keys():
			value += tickers[name]
			print(value)
		tickers.update({name: value})
	return tickers

print(report())
print(report_by_ticker())