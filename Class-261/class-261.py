def visitors():
    f = open("./count.txt", "r")
    count = int(f.read())
    f.close

    count += 1
    print(count)

    f = open("./count.txt", "w")
    f.write(str(count))
    f.close


visitors()


def api():
    lat = input("Lat: ")
    long = input("Long: ")

    url = f"https://weather-l6tl.onrender.com/api/getCurrentWeather/{lat}/{long}"
    print(url)


api()
