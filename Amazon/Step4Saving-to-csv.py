# To configure Scrapy to save all our data to a new CSV file everytime
# we run the scraper we simply need to create a Scrapy Feed and
# configure a dynamic file path.

# If we add the following code to our settings.py file,
# Scrapy will create a new CSV file in our data folder using
# the spider name and time the spider was run.
 
# settings.py 

FEEDS = {
    'data/%(name)s_%(time)s.csv': {
        'format': 'csv',
        }
}
