# Python-API-Challenge

7/24:
- Initially, was unable to create dataframe as some cities had missing values.  Realized that error was in some cities not having a JSON file and returning 404 error; created if conditoin to test for correct repsonse code
- Sill unable to correctly build dataframes withouth having some missing values.  Created troubleshooting test by pringting city, query_url link, and variables, and than at end of print log, an item count for each variable.  Discovered I was appending city and lat / long lists before running url_query, so that those lists would include data even if no weather data was returned from OpenWeather.  Moved append function after if condition to correct.

7/23:
- Pulled in cities from citipy
- Developed preliminary loop