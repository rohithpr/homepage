predefined_category_details = [
		('Social', 0, 0, '#6495ed'),
		('News', 0, 1, '#c41414'),

		('E-commerce', 1, 0, '#548b54'),
		('Business', 1, 1, '#c1cdc1'),

		('Entertainment', 2, 0, '#cd5c5c'),
		('Sports', 2, 1, '#ffb90f'),

		('E-mail', 3, 0, '#cdcd00'),
		('Reference', 3, 1, '#81d8d0'),

		('Tech', 4, 0, '#ffa500'),
		('Science', 4, 1, '#8b1a1a'),
		('Educational', 4, 2, '#338167'),

		('Travel', 5, 0, '#1f45d0'),
		('Random', 5, 1, '#473c8b'),
	]

predefined_category_names = [
		'Social', 'News',
		'E-commerce', 'Business',
		'Entertainment', 'Sports',
		'E-mail', 'Reference',
		'Tech', 'Science', 'Educational',
		'Travel', 'Random',
	]

predefined_bookmarks = {
	'Social': [
		('Facebook', 'http://www.facebook.com/', 0, ''),
		('Twitter', 'https://twitter.com/', 1, ''),
		('Google+', 'https://plus.google.com/', 2, ''),
		('Quora', 'http://www.quora.com/', 3, ''),
		('Instagram', 'http://instagram.com/', 4, 'glyphicon-camera'),
		('Flickr', 'https://www.flickr.com/', 5, 'glyphicon-camera'),
		('LinkedIn', 'http://www.linkedin.com/', 6, ''),
		('Reddit', 'http://www.reddit.com/', 7, ''),
		('Meetup', 'http://www.meetup.com/', 8, ''),
		('Digg', 'http://www.digg.com/', 9, ''),
		('9gag', 'http://9gag.com/', 10, ''),

	],

	'News': [
		('Reuters', 'http://www.reuters.com/', 0, ''),
		('Google News', 'https://news.google.com/', 1, ''),
		('Yahoo News', 'http://news.yahoo.com/', 2, ''),
		('CNN', 'http://edition.cnn.com/', 3, ''),
		('The Guardian', 'http://www.theguardian.com/', 4, ''),
		('BBC News', 'http://www.bbc.com/news/', 5, ''),
		('Fox News', 'http://www.foxnews.com/', 6, ''),
		('The Hindu', 'http://www.thehindu.com/', 7, ''),
		('Times of India', 'http://timesofindia.indiatimes.com/', 8, ''),
		('Deccan Herald', 'http://www.deccanherald.com/', 9, ''),
		('Russian Times', 'http://rt.com/', 10, ''),
		('Time', 'http://time.com/', 11, '')
	],

	'E-commerce': [
		('Amazon', 'http://www.amazon.com/', 0, ''),
		('Ebay', 'http://www.ebay.com/', 1, ''),
		('PayPal', 'https://www.paypal.com/', 2, ''),
		('Paytm', 'https://paytm.com/', 3, ''),
		('Flipkart', 'http://www.flipkart.com/', 4, ''),
		('Snapdeal', 'http://www.snapdeal.com/', 5, ''),
		('Groupon', 'http://www.groupon.com/', 6, ''),
		('Best Buy', 'http://www.bestbuy.com/', 7, ''),
		('Etsy', 'https://www.etsy.com/', 8, ''),
	],

	'Business': [
		('Forbes', 'http://www.forbes.com/', 0, ''),
		('Yahoo Finance', 'http://finance.yahoo.com/', 1, ''),
	],

	'Entertainment': [
		('Youtube', 'https://www.youtube.com/', 0, ''),
		('Spotify', 'https://www.spotify.com/', 1, ''),
		('Metacafe', 'http://www.metacafe.com/', 2, ''),
		('Pandora', 'http://www.pandora.com/', 3, ''),
		('IMDb', 'http://www.imdb.com/', 4, ''),
		('Rotten Tomatoes', 'http://www.rottentomatoes.com/', 5, ''),
	],

	'Sports': [
		('Goal', 'http://www.goal.com/', 0, ''),
		('ESPN Cricinfo', 'http://www.espncricinfo.com/', 1, ''),
		('Yahoo Sports', 'sports.yahoo.com/', 2, ''),
		('ESPN', 'espn.go.com/', 3, ''),
		('NFL', 'http://www.nfl.com/', 4, ''),
		('NBA', 'http://www.nba.com/', 5, ''),
		('Sky Sports', 'http://www.skysports.com/', 6, ''),
		('WWE', 'http://www.wwe.com/', 7, ''),
		('Cricbuzz', 'http://www.cricbuzz.com/', 8, ''),
	],

	'E-mail': [
		('Gmail', 'https://mail.google.com/', 0, ''),
		('Gmail Light', 'https://mail.google.com/mail/h/', 1, ''),
		('Outlook', 'https://bay176.mail.live.com/', 2, ''),
		('Yahoo', 'https://mail.yahoo.com/', 3, ''),
	],

	'Reference': [
		('Wikipedia', 'https://www.wikipedia.org/', 0, ''),
		('Archive.org', 'https://archive.org/', 1, ''),
		('Urban Dictionary', 'http://www.urbandictionary.com/', 2, ''),
		('WordReference', 'http://www.wordreference.com/', 3, ''),
		('Goodreads', 'http://www.goodreads.com/', 4, ''),
		('Thesaurus', 'http://www.thesaurus.com/', 5, ''),
		('How Stuff Works', 'http://www.howstuffworks.com/', 6, ''),
		('Brainy Quote', 'http://www.brainyquote.com/', 7, ''),
		('White Pages', 'http://www.whitepages.com/', 8, ''),
		('Yellow Pages', 'http://www.yellowpages.com/', 9, ''),
	],

	'Tech': [
		('Github', 'https://github.com/', 0, ''),
		('Stack Overflow', 'http://www.stackoverflow.com/', 1, ''),
		('TechCrunch', 'http://techcrunch.com/', 2,''),
	],

	'Educational': [
		('Coursera', 'https://www.coursera.org/', 0, ''),
		('W3C', 'http://www.w3.org/', 1, ''),
		('Udemy', 'https://www.udemy.com/', 2, ''),
		('MIT', 'http://web.mit.edu/', 3, ''),
		('Stanford', 'online.stanford.edu/', 4, ''),
		('Duolingo', 'https://www.duolingo.com/', 5, ''),
	],

	'Science': [
		('Elsevier', 'http://www.elsevier.com/', 0, ''),
	],

	'Travel': [
		('Bookings', 'https://www.booking.com/', 0, ''),
		('Trip Advisor', 'http://www.tripadvisor.in/', 1, ''),
		('Expedia', 'http://www.expedia.com/', 2, ''),
		('Zomato', 'https://www.zomato.com/', 3, ''),
		('Lonely Planet', 'http://www.lonelyplanet.com/', 4, ''),

	],

	'Random': [
		('Cracked', 'http://www.cracked.com/', 0, ''),
		('StumbleUpon', 'http://www.stumbleupon.com/', 1, ''),
		('Blah Therapy', 'http://blahtherapy.com/', 2, ''),
		('Cleverbot', 'http://www.cleverbot.com/', 3, ''),
	],

}