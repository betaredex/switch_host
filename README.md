# switch_host
A script for switching the host ip on cloudflare

To use this script, copy `config.py_SAMPLE` to `config.py` and replace the dummy values (the ones in brackets) with your own. Then, run `switch_host.py`.

These values include:
- main_ip: The IP address of the primary server.
- backup_ip: The IP address of the backup server. This is the server that will be switched to when the main server is down.
- api_urls: A list of url endpoints on the cloudflare api, corresponding to the records to be modified. Should look something like `https://api.cloudflare.com/client/v4/zones/ZONE_IDENTIFIER/dns_records/RECORD_IDENTIFIER`. This is a list so that you can modify your www entry as well if need be. Consult the cloudflare api documentation at https://api.cloudflare.com/#dns-records-for-a-zone-patch-dns-record for more info.
- headers: The headers for each request. Simply replace the value of the `Authorization` field with your cloudflare api token.
