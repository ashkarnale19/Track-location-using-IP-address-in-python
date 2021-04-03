import pygeoip

gip=pygeoip.GeoIP("GeoLiteCity.dat")
rec=gip.record_by_addr('161.185.160.93')
for i,j in rec.items():
  print('%s : %s' % (i,j))
  