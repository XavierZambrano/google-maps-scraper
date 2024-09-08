# google-maps-scraper

Fast Google Maps Scraper: Extract data from Google Maps Search, emulates the Places API [Text Search](https://developers.google.com/maps/documentation/places/web-service/text-search).

The project doesn't use webdrivers, which allows for high-speed scraping.
  
## Overview

### Fields

- name
- id
- types
- primaryTypeDisplayName
- nationalPhoneNumber
- internationalPhoneNumber
- formattedAddress
- plusCode
- location
- rating
- googleMapsUri
- websiteUri
- regularOpeningHours
- userRatingCount
- displayName


## Installation

### Setup

1. Clone the repository
```
git clone https://github.com/XavierZambrano/google-maps-scraper
```
2. Create a virtual environment
3. Install the dependencies
```bash
pip install -r requirements.txt
```


### Set proxy (optional)
Set HTTP_PROXY and HTTPS_PROXY in the `.env` file.
```bash
HTTP_PROXY=http://host:port
HTTPS_PROXY=http://host:port
```

## Usage
Note: Remember activate the virtual environment before running the commands.

Scrape the data and save in a CSV file.
```bash
scrapy crawl text_search -a queries="restaurants in sydney,second query" -a language="en" -a max_results=120 -O results.csv
```

Scrape the data and save in JSON.
```bash
scrapy crawl text_search -a queries="restaurants in sydney,second query" -a language="en" -a max_results=120 -O results.json
```

For more information about scrapy crawl arguments, refer to the [scrapy docs](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl).


Example result: 
```
[
    {
        "id": "ChIJdxxU1WeuEmsR11c4fswX-Io",
        "name": "places/ChIJdxxU1WeuEmsR11c4fswX-Io",
        "types": [
            "fine_dining_restaurant",
            "australian_restaurant"
        ],
        "primaryTypeDisplayName": {
            "text": "Fine dining restaurant"
        },
        "nationalPhoneNumber": "(02) 9240 2255",
        "internationalPhoneNumber": "+61 2 9240 2255",
        "formattedAddress": "1 Macquarie St, Sydney NSW 2000, Australia",
        "plusCode": {
            "globalCode": "4RRH46R7+88"
        },
        "location": {
            "latitude": -33.8592041,
            "longitude": 151.2132635
        },
        "rating": 4.5,
        "userRatingCount": 2054,
        "googleMapsUri": "https://maps.google.com/?cid=10013779938516686807",
        "websiteUri": "https://www.ariasydney.com.au/?utm_source=google&utm_medium=organic&utm_campaign=gbp&utm_content=Aria_Restaurant_Sydney&utm_term=plcid_18420151015366914459",
        "regularOpeningHours": {
            "periods": [
                {
                    "open": {
                        "day": 0,
                        "hour": 12,
                        "minute": 0
                    },
                    "close": {
                        "day": 0,
                        "hour": 15,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 0,
                        "hour": 17,
                        "minute": 0
                    },
                    "close": {
                        "day": 0,
                        "hour": 22,
                        "minute": 0
                    }
                },
                {
                    "open": {
                        "day": 1,
                        "hour": 17,
                        "minute": 30
                    },
                    "close": {
                        "day": 1,
                        "hour": 22,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 2,
                        "hour": 17,
                        "minute": 30
                    },
                    "close": {
                        "day": 2,
                        "hour": 22,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 3,
                        "hour": 17,
                        "minute": 30
                    },
                    "close": {
                        "day": 3,
                        "hour": 22,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 4,
                        "hour": 12,
                        "minute": 0
                    },
                    "close": {
                        "day": 4,
                        "hour": 15,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 4,
                        "hour": 17,
                        "minute": 30
                    },
                    "close": {
                        "day": 4,
                        "hour": 23,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 5,
                        "hour": 12,
                        "minute": 0
                    },
                    "close": {
                        "day": 5,
                        "hour": 15,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 5,
                        "hour": 17,
                        "minute": 0
                    },
                    "close": {
                        "day": 5,
                        "hour": 23,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 6,
                        "hour": 12,
                        "minute": 0
                    },
                    "close": {
                        "day": 6,
                        "hour": 15,
                        "minute": 30
                    }
                },
                {
                    "open": {
                        "day": 6,
                        "hour": 17,
                        "minute": 0
                    },
                    "close": {
                        "day": 6,
                        "hour": 23,
                        "minute": 30
                    }
                }
            ],
            "weekdayDescriptions": [
                "Monday: 5:30 – 10:30 PM",
                "Tuesday: 5:30 – 10:30 PM",
                "Wednesday: 5:30 – 10:30 PM",
                "Thursday: 12:00 – 3:30 PM, 5:30 – 11:30 PM",
                "Friday: 12:00 – 3:30 PM, 5:00 – 11:30 PM",
                "Saturday: 12:00 – 3:30 PM, 5:00 – 11:30 PM",
                "Sunday: 12:00 – 3:30 PM, 5:00 – 10:00 PM"
            ]
        },
        "displayName": {
            "text": "Aria Restaurant Sydney"
        }
    }, ...
]
```


### Contributing

Your contributions are always welcome!


TODO
- [ ] Add reviews field
- [ ] Add photos field