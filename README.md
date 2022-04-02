# favhash
 Calculate Favicon Hash for Shodan

### Examples

#### Favicon-file
##### python3 favhash.py http://target.com/favicon.ico
#### Favicon-url
##### cat target.txt | xargs -P 1 -I % bash -c "python3 favhash.py '%/favicon.ico' && echo % && echo '------------------------------------'"
