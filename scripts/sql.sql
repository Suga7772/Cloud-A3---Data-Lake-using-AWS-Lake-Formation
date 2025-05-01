-- 1. Avg temperature by city (2013-2017)  
SELECT city, AVG(temperature) as avg_temp  
FROM weatherdb.weather_data  
GROUP BY city  
ORDER BY avg_temp DESC;  

-- 2. Monsoon humidity trends in Mumbai  
SELECT month, AVG(humidity)  
FROM weatherdb.weather_data  
WHERE city = 'Mumbai' AND month IN (6,7,8,9)  
GROUP BY month;  