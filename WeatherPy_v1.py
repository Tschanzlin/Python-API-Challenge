{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: citipy in c:\\users\\todds\\anaconda3\\envs\\pythondata\\lib\\site-packages (0.0.5)\n",
      "Requirement already satisfied: kdtree>=0.12 in c:\\users\\todds\\anaconda3\\envs\\pythondata\\lib\\site-packages (from citipy) (0.16)\n"
     ]
    }
   ],
   "source": [
    "# Install citipy\n",
    "# !pip install citipy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'config1'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-62-7541b941b923>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;31m# Pull API key\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mconfig1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpy\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mapi_key\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'config1'"
     ]
    }
   ],
   "source": [
    "# Import dependendcies\n",
    "import matplotlib.pyplot as plt\n",
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy.stats import lineregress\n",
    "\n",
    "# from numpy import random\n",
    "\n",
    "# Pull API key\n",
    "# from config import api_key\n",
    "from api_keys import weather_api_key\n",
    "\n",
    "# Incorporated citipy to determine city based on latitude and longitude\n",
    "from citipy import citipy\n",
    "\n",
    "# Range of latitudes and longitudes\n",
    "lat_range = (-90, 90)\n",
    "long_range = (-180, 180)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'tw'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Test city pull\n",
    "\n",
    "city = citipy.nearest_city(22.99, 120.21)\n",
    "city.city_name\n",
    "city.country_code\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'jiuquan'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Random Test city pull\n",
    "# format is (lat, long, rounded to two decimal places)\n",
    "city = citipy.nearest_city(42.00, 100.00)\n",
    "city.city_name\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a random number generator to pull city name and lat, long for 500 cities using citipy\n",
    "    # iterative loop with lists for city name, city lat, city long\n",
    "# use openweathermap.org to pull weather data for representatitive city\n",
    "    # research API documentation to understand format to pull for each city\n",
    "    # single pull after city name list is created?\n",
    "# read data from JSON file; do this for a single city first\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-12"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a random city pull request\n",
    "# latitude = runs east-west, y-values range between -90 and +90\n",
    "# longitude = runs north_south, x-coordinates are between -180 and +180\n",
    "\n",
    "\n",
    "from numpy import random\n",
    "lat = random.randint(low=-90, high=90, size=1)\n",
    "long = random.randint(low=-180, high=180, size=1)\n",
    "\n",
    "int(lat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'toliary'"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city = citipy.nearest_city(lat, long)\n",
    "city_out = city.city_name\n",
    "city_out"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://api.openweathermap.org/data/2.5/weather?appid=73f5eef4ab6510912790a3c3d182fec9&q=nanortalik\n"
     ]
    }
   ],
   "source": [
    "# Create a single city open weather pull request\n",
    "\n",
    "# Set API key (Note:  not able to pull from config file)\n",
    "api_key = weather_api_key\n",
    "\n",
    "url = \"http://api.openweathermap.org/data/2.5/weather?\"\n",
    "city = city_out\n",
    "\n",
    "# Build query URL, and print output\n",
    "query_url = url + \"appid=\" + api_key + \"&q=\" + city\n",
    "print(query_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>terrace</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>290.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         0\n",
       "0  terrace\n",
       "1   290.15\n",
       "2       72\n",
       "3       90\n",
       "4      2.6"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get weather datafile\n",
    "weather_response = requests.get(query_url)\n",
    "weather_json = weather_response.json()\n",
    "\n",
    "# Select temperature (F), humidity (%), cloudiness (%), and wind speed (mph) from json\n",
    "temp = weather_json[\"main\"][\"temp\"]\n",
    "humid = weather_json[\"main\"][\"humidity\"]\n",
    "clouds = weather_json[\"clouds\"][\"all\"]\n",
    "windspd = weather_json[\"wind\"][\"speed\"]\n",
    "\n",
    "pd.DataFrame([city_out, temp, humid, clouds, windspd])\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Tempurature</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Cloudiness</th>\n",
       "      <th>Windspeed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>fianarantsoa</td>\n",
       "      <td>-21</td>\n",
       "      <td>47</td>\n",
       "      <td>279.34</td>\n",
       "      <td>96</td>\n",
       "      <td>58</td>\n",
       "      <td>2.57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>kankon</td>\n",
       "      <td>15</td>\n",
       "      <td>74</td>\n",
       "      <td>300.42</td>\n",
       "      <td>81</td>\n",
       "      <td>100</td>\n",
       "      <td>1.23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>bredasdorp</td>\n",
       "      <td>-53</td>\n",
       "      <td>18</td>\n",
       "      <td>287.15</td>\n",
       "      <td>93</td>\n",
       "      <td>0</td>\n",
       "      <td>0.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>san cristobal</td>\n",
       "      <td>-9</td>\n",
       "      <td>-90</td>\n",
       "      <td>291.50</td>\n",
       "      <td>90</td>\n",
       "      <td>69</td>\n",
       "      <td>1.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>tasiilaq</td>\n",
       "      <td>64</td>\n",
       "      <td>-41</td>\n",
       "      <td>277.15</td>\n",
       "      <td>93</td>\n",
       "      <td>7</td>\n",
       "      <td>1.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>rikitea</td>\n",
       "      <td>-29</td>\n",
       "      <td>-123</td>\n",
       "      <td>292.32</td>\n",
       "      <td>69</td>\n",
       "      <td>100</td>\n",
       "      <td>7.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>rikitea</td>\n",
       "      <td>-18</td>\n",
       "      <td>-114</td>\n",
       "      <td>292.32</td>\n",
       "      <td>69</td>\n",
       "      <td>100</td>\n",
       "      <td>7.76</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            City  Latitude  Longitude  Tempurature  Humidity  Cloudiness  \\\n",
       "0   fianarantsoa       -21         47       279.34        96          58   \n",
       "1         kankon        15         74       300.42        81         100   \n",
       "2     bredasdorp       -53         18       287.15        93           0   \n",
       "3  san cristobal        -9        -90       291.50        90          69   \n",
       "4       tasiilaq        64        -41       277.15        93           7   \n",
       "5        rikitea       -29       -123       292.32        69         100   \n",
       "6        rikitea       -18       -114       292.32        69         100   \n",
       "\n",
       "   Windspeed  \n",
       "0       2.57  \n",
       "1       1.23  \n",
       "2       0.50  \n",
       "3       1.20  \n",
       "4       1.30  \n",
       "5       7.76  \n",
       "6       7.76  "
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Simple loop with ten cities\n",
    "\n",
    "# Import dependencies\n",
    "from numpy import random\n",
    "from numpy import arange\n",
    "\n",
    "# Set API key (fix to pull from config file)\n",
    "api_key = \"73f5eef4ab6510912790a3c3d182fec9\"\n",
    "\n",
    "# Initialize lists to store values:\n",
    "\n",
    "cities = []\n",
    "latitude = []\n",
    "longitude = []\n",
    "tempurature = []\n",
    "humidity = []\n",
    "cloudiness = []\n",
    "windspeed = []\n",
    "\n",
    "counter2 = arange(1, 8)\n",
    "\n",
    "for count in counter2:\n",
    "\n",
    "    # generate random coordinates for cities, store latitude and longitude\n",
    "    lat = int(random.randint(low=-90, high=90, size=1))\n",
    "    long = int(random.randint(low=-180, high=180, size=1))\n",
    "    latitude.append(lat)\n",
    "    longitude.append(long)\n",
    "\n",
    "\n",
    "    # find city using citipy, store city\n",
    "    city = citipy.nearest_city(lat, long)\n",
    "    city_out = city.city_name\n",
    "    city_out\n",
    "    cities.append(city_out)\n",
    "\n",
    "    # Set endoint and build query-url\n",
    "    url = \"http://api.openweathermap.org/data/2.5/weather?\"\n",
    "    query_url = url + \"appid=\" + api_key + \"&q=\" + city_out\n",
    "\n",
    "    # Get weather datafile\n",
    "    weather_response = requests.get(query_url)\n",
    "    weather_json = weather_response.json()\n",
    "\n",
    "    # Select temperature (F), humidity (%), cloudiness (%), and wind speed (mph) from json\n",
    "    temp = weather_json[\"main\"][\"temp\"]\n",
    "    humid = weather_json[\"main\"][\"humidity\"]\n",
    "    clouds = weather_json[\"clouds\"][\"all\"]\n",
    "    windspd = weather_json[\"wind\"][\"speed\"]\n",
    "\n",
    "    # store weather data to file\n",
    "    tempurature.append(temp)\n",
    "    humidity.append(humid)\n",
    "    cloudiness.append(clouds)\n",
    "    windspeed.append(windspd)\n",
    "\n",
    "# format output to DataFrame    \n",
    "output = {\"City\": cities, \"Latitude\": latitude, \"Longitude\": longitude, \"Tempurature\": tempurature, \n",
    "      \"Humidity\": humidity, \"Cloudiness\": cloudiness, \"Windspeed\": windspeed}\n",
    "\n",
    "pd.DataFrame(output)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
