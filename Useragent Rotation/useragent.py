# pip install scrapy-user-agents

# Then in add it to your projects settings.py file, and disable Scrapy's default UserAgentMiddleware by setting its value to None:

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# The scrapy-user-agents download middleware contains about 2,200 common user agent strings, and rotates through them as your scraper makes requests.
