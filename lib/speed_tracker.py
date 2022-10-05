# 7/2/2022
# Check your network speed and notify you via email if the network upload and download speeds are below the predefined speeds in the 'speedTracker.ini' file.

from configparser import ConfigParser
from time import sleep
import speedtest
from STTools import (environ_var_exists, send_email,
                     settings_exists, create_settings,
                     email_is_valid, convert_bytes)

# Speed test
st = speedtest.Speedtest()

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1




while True:
    config_file_path = 'setting/speedTracker.ini'
    app_settings = ConfigParser()
    app_settings.read(config_file_path)

    if environ_var_exists() and settings_exists():
        email_provider = app_settings['DEFAULT']['emailProvider']
        min_ds = app_settings['DEFAULT']['minDownloadSpeed']
        min_us = app_settings['DEFAULT']['minUploadSpeed']
        receiver_email = app_settings['DEFAULT']['receiverEmail']
        modem_loc = app_settings['DEFAULT']['modemLocation']
        print('PASS: evn and settings test')
        

        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()
        results_dict = s.results.dict()
        
        ds = convert_bytes(results_dict.get('download'))
        us = convert_bytes(results_dict.get('upload'))
        ping = results_dict.get('ping')
        link = results_dict.get('share')
        
        # print('PASS: speed test')
        
        if email_is_valid(receiver_email, email_provider):
            send_email(us, ds, ping, link, receiver_email, modem_loc)
            # print('PASS: validate  and send email test')
            break
        else:
            # print('PASS: email is not valid test')
            # print('Go to setting and change the receiver email.')
            break
    else:
        create_settings()      
        # print('PASS: create settings test')
























sample_data = {'download': 149760887.81690148, 'upload': 131314054.91164869, 'ping': 2.901, 'server': {'url': 'http://speedtest1.flowjamaica.com:8080/speedtest/upload.php', 'lat': '17.9683', 'lon': '-76.7827', 'name': 'Kingston', 'country': 'Jamaica', 'cc': 'JM', 'sponsor': 'FLOW Jamaica', 'id': '14260', 'host': 'speedtest1.flowjamaica.com:8080', 'd': 3.707838307522677, 'latency': 2.901}, 'timestamp': '2022-07-02T23:11:45.745337Z', 'bytes_sent': 151519232, 'bytes_received': 190362476, 'share': 'http://www.speedtest.net/result/13359052207.png', 'client': {'ip': '216.10.217.245', 'lat': '17.9962', 'lon': '-76.8019', 'isp': 'Flow', 'isprating': '3.7', 'rating': '0', 'ispdlavg': '0', 'ispulavg': '0', 'loggedin': '0', 'country': 'JM'}}
