#NOAA-GFS
#https://node.windy.com/forecast/v2.1/gfs/43.663/-79.399?source=detail
#EC
#https://node.windy.com/forecast/v2.1/ecmwf/43.663/-79.399?setup=summary&includeNow=true&source=hp
import json
import urllib.request
import time

def getWeatherData(org, lon, lat):
    try:
        if org == 'GFS':
            data = urllib.request.urlopen('https://node.windy.com/forecast/meteogram/gfs/' + str(lat) +'/' + str(lon)).read()
        if org == 'EC':
            data = urllib.request.urlopen('https://node.windy.com/forecast/meteogram/ecmwf/' + str(lat) +'/' + str(lon)).read()
        record = data.decode('UTF-8')
        data = json.loads(record)
        return data
    except:
        return {}

def analyzeDetailT(JSON):
    model = JSON['header']['model']
    reftime = JSON['header']['refTime']
    T1000 = JSON['data']['temp-1000h']
    T950 = JSON['data']['temp-950h']
    T900 = JSON['data']['temp-900h']
    T850 = JSON['data']['temp-850h']
    T800 = JSON['data']['temp-800h']
    T700 = JSON['data']['temp-700h']
    T600 = JSON['data']['temp-600h']
    T500 = JSON['data']['temp-500h']
    T400 = JSON['data']['temp-400h']
    T300 = JSON['data']['temp-300h']
    T200 = JSON['data']['temp-200h']

    T750 = []
    T650 = []
    T550 = []
    T450 = []
    T350 = []
    T250 = []
    count = 0
    for i in T800:
        T1000[count] -= 273.15
        T950[count] -= 273.15
        T900[count] -= 273.15
        T850[count] -= 273.15
        T800[count] -= 273.15
        T700[count] -= 273.15
        T600[count] -= 273.15
        T500[count] -= 273.15
        T400[count] -= 273.15
        T300[count] -= 273.15
        T200[count] -= 273.15
        T750.append((T700[count] + T800[count])/2.0)
        T650.append((T600[count] + T700[count]) / 2.0)
        T550.append((T500[count] + T600[count]) / 2.0)
        T450.append((T400[count] + T500[count]) / 2.0)
        T350.append((T300[count] + T400[count]) / 2.0)
        T250.append((T200[count] + T300[count]) / 2.0)
        count += 1

    # print('T analyzed.')
    return [T1000,T950,T900,T850,T800,T750,T700,T650,T600,T550,T500,T450,T400,T350,T300,T250,T200]

def analyzeDetailRH(JSON):
    model = JSON['header']['model']
    reftime = JSON['header']['refTime']
    RH1000 = JSON['data']['rh-1000h']
    RH950 = JSON['data']['rh-950h']
    RH900 = JSON['data']['rh-900h']
    RH850 = JSON['data']['rh-850h']
    RH800 = JSON['data']['rh-800h']
    RH700 = JSON['data']['rh-700h']
    RH600 = JSON['data']['rh-600h']
    RH500 = JSON['data']['rh-500h']
    RH400 = JSON['data']['rh-400h']
    RH300 = JSON['data']['rh-300h']
    RH200 = JSON['data']['rh-200h']

    RH750 = []
    RH650 = []
    RH550 = []
    RH450 = []
    RH350 = []
    RH250 = []
    count = 0
    for i in RH800:
        RH750.append((RH700[count] + RH800[count])/2.0)
        RH650.append((RH600[count] + RH700[count]) / 2.0)
        RH550.append((RH500[count] + RH600[count]) / 2.0)
        RH450.append((RH400[count] + RH500[count]) / 2.0)
        RH350.append((RH300[count] + RH400[count]) / 2.0)
        RH250.append((RH200[count] + RH300[count]) / 2.0)
        count += 1

    # print('RH analyzed.')
    return [RH1000,RH950,RH900,RH850,RH800,RH750,RH700,RH650,RH600,RH550,RH500,RH450,RH400,RH350,RH300,RH250,RH200]

def analyzeDetailwindV(JSON):
    model = JSON['header']['model']
    reftime = JSON['header']['refTime']
    WV1000 = JSON['data']['wind_v-1000h']
    WV950 = JSON['data']['wind_v-950h']
    WV900 = JSON['data']['wind_v-900h']
    WV850 = JSON['data']['wind_v-850h']
    WV800 = JSON['data']['wind_v-800h']
    WV700 = JSON['data']['wind_v-700h']
    WV600 = JSON['data']['wind_v-600h']
    WV500 = JSON['data']['wind_v-500h']
    WV400 = JSON['data']['wind_v-400h']
    WV300 = JSON['data']['wind_v-300h']
    WV200 = JSON['data']['wind_v-200h']

    WV750 = []
    WV650 = []
    WV550 = []
    WV450 = []
    WV350 = []
    WV250 = []
    count = 0
    for i in WV800:
        WV750.append((WV700[count] + WV800[count]) / 2.0)
        WV650.append((WV600[count] + WV700[count]) / 2.0)
        WV550.append((WV500[count] + WV600[count]) / 2.0)
        WV450.append((WV400[count] + WV500[count]) / 2.0)
        WV350.append((WV300[count] + WV400[count]) / 2.0)
        WV250.append((WV200[count] + WV300[count]) / 2.0)
        count += 1

    # print('WV analyzed.')
    return [WV1000,WV950,WV900,WV850,WV800,WV750,WV700,WV650,WV600,WV550,WV500,WV450,WV400,WV350,WV300,WV250,WV200]

def analyzeDetailwindU(JSON):
    model = JSON['header']['model']
    reftime = JSON['header']['refTime']
    WU1000 = JSON['data']['wind_u-1000h']
    WU950 = JSON['data']['wind_u-950h']
    WU900 = JSON['data']['wind_u-900h']
    WU850 = JSON['data']['wind_u-850h']
    WU800 = JSON['data']['wind_u-800h']
    WU700 = JSON['data']['wind_u-700h']
    WU600 = JSON['data']['wind_u-600h']
    WU500 = JSON['data']['wind_u-500h']
    WU400 = JSON['data']['wind_u-400h']
    WU300 = JSON['data']['wind_u-300h']
    WU200 = JSON['data']['wind_u-200h']

    WU750 = []
    WU650 = []
    WU550 = []
    WU450 = []
    WU350 = []
    WU250 = []
    count = 0
    for i in WU800:
        WU750.append((WU700[count] + WU800[count]) / 2.0)
        WU650.append((WU600[count] + WU700[count]) / 2.0)
        WU550.append((WU500[count] + WU600[count]) / 2.0)
        WU450.append((WU400[count] + WU500[count]) / 2.0)
        WU350.append((WU300[count] + WU400[count]) / 2.0)
        WU250.append((WU200[count] + WU300[count]) / 2.0)
        count += 1

    # print('WU analyzed.')
    return [WU1000,WU950,WU900,WU850,WU800,WU750,WU700,WU650,WU600,WU550,WU500,WU450,WU400,WU350,WU300,WU250,WU200]

def analyzeDetailPressure(JSON):
    T800 = JSON['data']['temp-800h']
    P = []
    for row in range(0, 17):
        P.append([])
        for i in range(0, len(T800)):
            P[row].append(1000 - 50 * row)
    return P

def getTimeSeriesVerticalWeather(org, lon, lat):
    source = org
    try:
        lon = float(lon)
        lat = float(lat)
    except:
        return False

    iodata = getWeatherData(source, lon, lat)
    hourspoint = iodata['data']['hours']

    for i in range(0, len(hourspoint)):
        hourspoint[i] = hourspoint[i] / 1000.0

    dates = [time.strftime('%d%Hz', time.localtime(ts)) for ts in hourspoint]
    newdates = []
    ticks = []
    count = 1
    for i in dates:
        if count % 2 == 0:
            newdates.append(i)
            ticks.append(count)
        count += 1

    return [dates, analyzeDetailPressure(iodata), analyzeDetailT(iodata), analyzeDetailRH(iodata), analyzeDetailwindU(iodata), analyzeDetailwindV(iodata)]