# PhiX-IT

## Requirements
Environement
- Python 3.11.1
Packages
- « geopy » pip install geopy 
- « serial » pip install serial

## Dashboard

To run the app you need to launch the file
- dashboard.py

and open in your browser the next link: 
- http://localhost:5000/dashboard/

If you enter a city on the field "City" it will redirect at http://localhost:5000/city/. The information by city is not implemented. The variable city exist on the dashboard.py and it recevice the input user. An improvement could be talking the function with the city as argument. 


## APIS

If you want to see the data received, you can acces to :

### API weather
Forecaster 5 days
http://localhost:5000/api/weather/

### API forecaster
24 h
http://localhost:5000/api/forecaster/

### API volcanic activity
http://localhost:5000/api/volcanic_activity/

### API earthquake
http://localhost:5000/api/earthquake/

### API flood
http://localhost:5000/api/flood/

### API avalanche
http://localhost:5000/api/avalanche/


It is preferable to run the localhost on a private browser to avoid problems related to localhost history