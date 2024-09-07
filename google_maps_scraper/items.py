import scrapy


class Place(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    types = scrapy.Field()

    primaryTypeDisplayName = scrapy.Field()
    nationalPhoneNumber = scrapy.Field()
    internationalPhoneNumber = scrapy.Field()
    formattedAddress = scrapy.Field()
    plusCode = scrapy.Field()
    location = scrapy.Field()
    rating = scrapy.Field()
    googleMapsUri = scrapy.Field()
    websiteUri = scrapy.Field()
    regularOpeningHours = scrapy.Field()
    userRatingCount = scrapy.Field()
    displayName = scrapy.Field()
