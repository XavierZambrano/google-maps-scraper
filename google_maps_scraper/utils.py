from datetime import datetime


# https://developers.google.com/custom-search/docs/xml_results_appendices?hl=en#supported-interface-languages
GOOGLE_SUPPORTED_LANGUAGES = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Burmese": "my",
    "Catalan": "ca",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English (UK)": "en-GB",
    "English": "en",
    "Estonian": "et",
    "Filipino": "fil",
    "Finnish": "fi",
    "French (Canadian)": "fr-CA",
    "French": "fr",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Korean": "ko",
    "Kyrgyz": "ky",
    "Laothian": "lo",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Macedonian": "mk",
    "Malay": "ms",
    "Malayam": "ml",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Nepali": "ne",
    "Norwegian (Bokmal)": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese (Brazil)": "pt-BR",
    "Portuguese (Portugal)": "pt-PT",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian (Latin)": "sr-Latn",
    "Serbian": "sr",
    "Sinhalese": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish (Latin America)": "es-419",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
}

def get_weekday_descriptions(periods):
    descriptions = []
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Initialize a list to hold open hours for each day
    hours = [[] for _ in range(7)]

    # Populate the hours list with opening periods
    for period in periods:
        day = period['open']['day']
        open = datetime.strptime(f"{period['open']['hour']}:{str(period['open']['minute']).zfill(2)}", "%H:%M")
        close = datetime.strptime(f"{period['close']['hour']}:{str(period['close']['minute']).zfill(2)}", "%H:%M")


        if open.strftime('%p') == close.strftime('%p'):
            hours[day].append(f"{open.strftime('%-I:%M')}\u2009–\u2009{close.strftime('%-I:%M')}\u202f{close.strftime('%p')}")
        else:
            hours[day].append(f"{open.strftime('%-I:%M')}\u202f{open.strftime('%p')}\u2009–\u2009{close.strftime('%-I:%M')}\u202f{close.strftime('%p')}")

    # Create descriptions for each day
    for index, times in enumerate(hours):
        if times:
            descriptions.append(f"{days[index]}: {', '.join(times)}")
        else:
            descriptions.append(f'{days[index]}: Closed')

    # move sunday to the last position
    descriptions = descriptions[1:] + descriptions[:1]

    return descriptions

def get_periods(data4):
    days_of_the_week = 7

    period_days_raw = data4[203][0]
    periods = []
    for pdr in period_days_raw:
        # 0 == sunday, monday == 1 ...
        day = pdr[1] % days_of_the_week
        if pdr[3] == [['Closed']]:
            continue
        for p in pdr[3]:
            # cases:
            # [] it means 0 hours, 0 minutes
            # [15], it means 15 hours, 0 minutes
            # [15, 30], it means 15 hours, 30 minutes
            # [None, 30], it means 0 hours, 30 minutes
            period = {
                'open': {
                    'day': day,
                    'hour': p[1][0][0] if len(p[1][0]) > 0 and bool(p[1][0][0]) else 0,
                    'minute': p[1][0][1] if len(p[1][0]) > 1 else 0,
                },
                'close': {
                    'day': day,
                    'hour': p[1][1][0] if len(p[1][1]) > 0 and bool(p[1][1][0]) else 0,
                    'minute': p[1][1][1] if len(p[1][1]) > 1 else 0,
                }
            }
            periods.append(period)

    periods = sorted(periods, key=lambda x: (x['open']['day'], x['open']['hour']))
    return periods