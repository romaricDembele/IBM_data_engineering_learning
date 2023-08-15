
# Copy the data in the file ‘web-server-access-log.txt.gz’ to the table ‘access_log’ in the PostgreSQL database ‘template1’.

# The file is available at the location : https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz

# The following are the columns and their data types in the file:

# a. timestamp - TIMESTAMP

# b. latitude - float

# c. longitude - float

# d. visitorid - char(37)

# and two more columns: accessed_from_mobile (boolean) and browser_code (int)

# The columns which we need to copy to the table are the first four coumns : timestamp, latitude, longitude and visitorid.

# NOTE: The file comes with a header. So use the ‘HEADER’ option in the ‘COPY’ command.

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz
# Unzip the file to extract the .txt file.
gunzip -f web-server-access-log.txt.gz

# Extract required fields from the file
cut -d"#" -f1-4 web-server-access-log.txt > extracted_data.txt

# Transform the data into CSV format
tr "#" "," < extracted_data.txt > transformed_data.csv

echo "\c template1;\COPY access_logusers FROM 'transformed_data.csv' DELIMITERS ',' CSV HEADER;" | psql --username=postgres --host=localhost
