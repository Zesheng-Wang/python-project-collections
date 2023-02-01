import speedtest
wifi = speedtest.Speedtest()
print("******************开始测试******************")
wifi_download = wifi.download() / 1024 / 1024
wifi_upload = wifi.upload() / 1024 / 1024
print(f"Wifi Download Speed is {wifi_download:.2f}  Mbits")
print(f"Wifi Upload Speed is {wifi_upload:.2f}  Mbits")
print("******************测试完毕******************")
