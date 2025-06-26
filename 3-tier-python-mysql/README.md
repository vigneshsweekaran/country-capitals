## 3-tier


### Load data into mysql db
```
CREATE DATABASE IF NOT EXISTS my_country_db;
USE my_country_db;
mysql -u your_username -p my_country_db < countries_dump.sql
```