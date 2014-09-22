# configurant proxy
export http_proxy="http://10.2.201.33:8080"

# neteja de temporals
rm -fr /c/tmp/tiempo
mkdir /c/tmp/tiempo
cd /c/tmp/tiempo

# downloading...
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_1.gif
mv alturah_1.gif alturah_01.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_4.gif
mv alturah_4.gif alturah_04.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_7.gif
mv alturah_7.gif alturah_07.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_10.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_13.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_16.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_19.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_22.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_25.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_28.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_31.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_34.gif
wget http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_37.gif