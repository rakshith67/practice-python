import datetime
import pytz

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {0} timezone is {1}".format(country, local_time))
print('UTC time is {}'.format(datetime.datetime.utcnow()))

for timezone in pytz.all_timezones:
    print(timezone)

for timezone in sorted(pytz.country_names):
    print("timezone: " + pytz.country_names[timezone])

for country_name in sorted(pytz.country_names):
    print("{0}: {1}".format(country_name, pytz.country_names[country_name]), end=": ")
    if country_name in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[country_name]):
            current_tz = pytz.timezone(zone)
            current_localtime = datetime.datetime.now(tz=current_tz)
            print("\t\t{}: {}".format(current_tz, current_localtime))
    else:
        print("No TimeZone Available")

utc_time = datetime.datetime.utcnow()
localtime = pytz.utc.localize(utc_time).astimezone()
print("UTC time {0} and time zone {1}".format(utc_time, utc_time.tzinfo))
print("Local time {0} and time zone {1}".format(localtime, localtime.tzinfo))

gap_time = datetime.datetime(2019, 10, 12, 6, 34, 0, 0)
print(gap_time)
print(gap_time.timestamp())

timestamp1 = 1445733000
timestamp2 = timestamp1 + (60 * 60)

datetime1 = pytz.utc.localize(datetime.datetime.fromtimestamp(timestamp1))
datetime2 = pytz.utc.localize(datetime.datetime.fromtimestamp(timestamp2))

print("{0} seconds from epoch is {1}".format(timestamp1, datetime1))
print("{0} seconds from epoch is {1}".format(timestamp2, datetime2))

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}

print("Please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{}: {}".format(place, available_zones[place]))

while True:
    choice = input()

    if input == '0':
        break

    print("UTC time is {0}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
    print("local time is {0}".format(datetime.datetime.now().strftime('%A %x %X')))
    zone = pytz.timezone(available_zones[choice])
    print("time at {0} is {1}".format(available_zones[choice], datetime.datetime.now(tz=zone)))
    print()
