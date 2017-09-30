#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as tm
import pandas as pd
import math as ma
import sys
import googlemaps

apiKey = sys.argv[1]  # 0は実行するスクリプト
                      # python getLatlong.py {your apiKey}

gmaps = googlemaps.Client(key=apiKey)

resDf = pd.DataFrame(columns = [u'PostalCode', u'Prefecture', u'City', u'following' , u'Latitude', u'Longitude'])

errs = []

df = pd.read_csv('jusho5-utf8.csv')
for key, row in df.iterrows():
  tm.sleep(0.5)
  address = '0'* (7-len(str(row[0]))) + str(row[0]) # excelで最初の0が消されてしまうのでつける

  print(address)

  geoRes = gmaps.geocode(address)

  if len(geoRes)==0 :
    print('geoRes equal 0...\n address is {0}'.format(address))
    errs.append(address)
    continue 

  following = row[3] if row[3] != '以下に掲載がない場合' else '-'
  tmp = pd.Series([address,
                  row[1],
                  row[2],
                  following,
                  geoRes[0]['geometry']['location']['lat'],
                  geoRes[0]['geometry']['location']['lng']],
                  index=resDf.columns)
  print('res={0}'.format(str(tmp)))
  resDf = resDf.append(tmp, ignore_index=True)



resDf.to_csv('res-PostalCode.csv')


