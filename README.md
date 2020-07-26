# Python-API-Challenge

Summary of Data:
Latitude vs. Tempuratare
- Strong correlation between latitude and tempurature as you would expect (adn as noted by rvalue)
- While one relationship looks positive and the other negative, the correlation is in fact the same
- Further away from 0 degress latitude (equator), the colder the tempuratures will be
- Difference in regression slopes is due to +/- sign convention of latitude above and below equator
- If measured as distance from equator (abs (latitude) - 0 degress latitude), then charts would look similar

Latitude vs. Humidity
- Very little correlation between latitude and humidity as noted by shape of scatter, flat regression line, and low rvalue
- Appers to be a slighty higher concentration of high humid zones near equator in southern hemisphere than northern

Latitude vs. Cloudiness
- Very little correlation between latitude and cloudiness as noted by shape of scatter, flat regression line, and low rvalue
- There are some interesting datapoints, which appear to cluster around 0, 40 +/-, and 75 +/- degress latitude
- Observations are more prevalent in northern hemisphere, but likely due to more datapoints in northern hemisphere
- More datapoints in northern hemisphere likely due to greater population density in north and not sampling issue

Latitude vs. Windspeed
- Very little correlation between latitude and cloudiness as noted by shape of scatter, flat regression line, and low rvalue
- Windspeeds appear to be equally distributed across degrees of latitude

Log:
7/26:
- All code working with exception of hotel markers on last graph

7/25:
- Workign version of google maps

7/24:
- Initially, was unable to create dataframe as some cities had missing values.  Realized that error was in some cities not having a JSON file and returning 404 error; created if conditoin to test for correct repsonse code
- Sill unable to correctly build dataframes withouth having some missing values.  Created troubleshooting test by pringting city, query_url link, and variables, and than at end of print log, an item count for each variable.  Discovered I was appending city and lat / long lists before running url_query, so that those lists would include data even if no weather data was returned from OpenWeather.  Moved append function after if condition to correct.

7/23:
- Pulled in cities from citipy
- Developed preliminary loop