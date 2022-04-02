# favhash
 Calculate Favicon Hash for Shodan

## Usage

```
➜ git clone https://github.com/imtiazsec/favhash.git
➜ cd favhash
➜ pip3 install -r requirements.txt

[!] Usage:
➜ python3 favhash.py http://target.com/favicon.ico
➜ cat target.txt | xargs -P 1 -I % bash -c "python3 favhash.py '%/favicon.ico' && echo % && echo '------------------------------------'"

[!] View Results:
http.favicon.hash:1848946384
------------------------------------

http.favicon.hash:-1596052821
------------------------------------

[!] Search in Shodan:
https://www.shodan.io/search?query=http.favicon.hash%3A1848946384
