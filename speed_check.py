import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    # Download speed in Mbps
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download Speed in Mbps:", down_speed)

    # Upload speed in Mbps
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed in Mbps:", up_speed)

    # Ping in ms
    ping = test.results.ping
    print("Ping:", ping)

# Run the test
Speed_Test()
