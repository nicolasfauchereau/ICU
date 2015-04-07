#!/Users/nicolasf/anaconda/bin/python
import os, sys, time
from datetime import datetime
from pytz import timezone
from pytz import all_timezones
sys.path.append("./")
import countryinfo
info = countryinfo.countries

icu, year, month, day, hour, minute = map(int, sys.argv[1:])

### ===========================================================================
### list of the countries for which the local date and times have to be determined
list_countries = ['New Zealand', \
'Australia', 'New Caledonia', 'Vanuatu', 'French Polynesia', 'Washington', \
'Hawai', 'Samoa', 'Fiji', 'Kiribati']

def find_country_tz(location):
    """
    find the time zone info of a country
    """
    c = 0
    for l in info:
        if (l['name'] == location) or (l['capital'] == location) or (location in l['timezones']):
            return info[c]['timezones'][0]
            break
        else:
            c += 1
            continue

dict_tz = {}
for location in list_countries:
    dict_tz[location] = find_country_tz(location)

fmt = "%Y-%m-%d %H:%M / %Z%z"

dict_countries = {}
dict_countries['Australia (Melbourne)'] = 'Australia/Melbourne'
dict_countries['French Polynesia'] = 'Pacific/Tahiti'
dict_countries['The Marquesas'] = 'Pacific/Marquesas'
dict_countries['New Caledonia'] = 'Pacific/Noumea'
dict_countries['Fiji'] = 'Pacific/Fiji'
dict_countries['Hawai'] = 'Pacific/Honolulu'
dict_countries['Vanuatu'] = 'Pacific/Efate'
dict_countries['Samoa'] = 'Pacific/Apia'
dict_countries['Kiribati'] = 'Pacific/Tarawa'


### what time it's gonna be here in Auckland

auck = timezone('Pacific/Auckland')
auck = auck.localize(datetime(year,month,day,hour,minute))

utc = auck.astimezone(timezone('UTC'))

Auckland = "%s the %s of %s %s at %s New Zealand time" % (auck.strftime("%A"), auck.strftime("%d"), auck.strftime("%B"), auck.strftime("%Y"), auck.strftime("%H:%M"))
UTC = "%s the %s of %s %s at %s %s" % (utc.strftime("%A"), utc.strftime("%d"), utc.strftime("%B"), utc.strftime("%Y"), utc.strftime("%H:%M"), utc.strftime("%Z%z"))

# and loop over the list of TZ to generate the proper date and time

text =  ""

tzinfo = []

for country in dict_countries.keys():
    res = auck.astimezone(timezone(dict_countries[country]))
    #print "%s the %s of %s %s at %s in %s (%s)." % (res.strftime("%A"), res.strftime("%d"), res.strftime("%B"), res.strftime("%Y"), res.strftime("%H:%M"), country, res.strftime("%Z%z"))
    tzinfo.append("%s the %s of %s %s at %s in %s (%s).\n" % (res.strftime("%A"), res.strftime("%d"), res.strftime("%B"), res.strftime("%Y"), res.strftime("%H:%M"), country, res.strftime("%Z%z")))

tzinfo = "".join(tzinfo)


text = """Subject: ICU forecasts guidance teleconference

Kia Ora Tatou,

The Teleconference to discuss forecasts for Issue %s of the Island Climate Update will be held on: \n
%s (%s).\n
The teleconference will include a discussion of the regional ENSO diagnostics and then the forecast guidance from METPI in this call. \n\n\
All invited parties are welcome to attend. Pacific Island Meteorological services are encouraged to bring their most recent SCOPIC results for comparison to METPI so consensus can be reached for ICU %s.

Please confirm your participation with Nico at least one hour before the teleconference time and indicate at which phone number you will be reachable.

For info %s will translate in:\n
%s

Best regards

The ICU Team (Nicolas Fauchereau, Andrew Lorrey, Nava Fedaeff, Petra Chappell, Doug Ramsay)

""" % (str(icu), UTC, Auckland, str(icu), Auckland, tzinfo)

print(text)
