# favhash
 Calculate Favicon Hash for Shodan

## Usage
...

python3 favhash.py http://target.com/favicon.ico
cat target.txt | xargs -P 1 -I % bash -c "python3 favhash.py '%/favicon.ico' && echo % && echo '------------------------------------'"

...
