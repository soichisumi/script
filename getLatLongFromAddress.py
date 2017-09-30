#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import math as ma
import sys
import googlemaps

apiKey = sys.argv[1]  # 0は実行するスクリプト
                      # python getLatlong.py {your apiKey}

gmaps = googlemaps.Client(key=apiKey)

resDf = pd.DataFrame(columns = [u'都道府県', u'市区町村', u'緯度', u'経度'])

df = pd.read_csv('jusho.csv')
for key, row in df.iterrows():
  address = row[1]
  if row.isnull()[2]:
    row[2] = ''
  address = row[1] + row[2]

  geoRes = gmaps.geocode(address)
  tmp = pd.Series([row[1],
                  row[2],
                  geoRes[0]['geometry']['location']['lat'], 
                  geoRes[0]['geometry']['location']['lng']],
                  index=resDf.columns)

  resDf = resDf.append(tmp, ignore_index=True)

resDf.to_csv('res.csv')


