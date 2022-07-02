# 7/2/2022
# Check your network speed and notify you via email if the network upload and download speeds are below the predefined speeds in the 'speedTracker.ini' file.

import speedtest
from STTools import convert_bytes

# Speed test
st = speedtest.Speedtest()


# GETTING DOWNLOAD Speed
# ds = st.download()

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()
# print(convert_bytes(ds))
print(results_dict)
sample_data = {'download': 149760887.81690148, 'upload': 131314054.91164869, 'ping': 2.901, 'server': {'url': 'http://speedtest1.flowjamaica.com:8080/speedtest/upload.php', 'lat': '17.9683', 'lon': '-76.7827', 'name': 'Kingston', 'country': 'Jamaica', 'cc': 'JM', 'sponsor': 'FLOW Jamaica', 'id': '14260', 'host': 'speedtest1.flowjamaica.com:8080', 'd': 3.707838307522677, 'latency': 2.901}, 'timestamp': '2022-07-02T23:11:45.745337Z', 'bytes_sent': 151519232, 'bytes_received': 190362476, 'share': 'http://www.speedtest.net/result/13359052207.png', 'client': {'ip': '216.10.217.245', 'lat': '17.9962', 'lon': '-76.8019', 'isp': 'Flow', 'isprating': '3.7', 'rating': '0', 'ispdlavg': '0', 'ispulavg': '0', 'loggedin': '0', 'country': 'JM'}}