import scrapy


class Place(scrapy.Item):
    name = scrapy.Field()
    

    id = scrapy.Field()
    primaryTypeDisplayName = scrapy.Field()
    nationalPhoneNumber = scrapy.Field()
    internationalPhoneNumber = scrapy.Field()
    formattedAddress = scrapy.Field()
    location = scrapy.Field()
    rating = scrapy.Field()
    googleMapsUri = scrapy.Field()
    displayName = scrapy.Field()
