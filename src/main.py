from requests import get

file = file_len = None


def download_json(url):
    global file
    global file_len
    file = get(url)
    file = file.json()
    file = file["results"][0]["cities"]
    file_len = len(file)

def analysis_json():
    global file_len, file
    for a in range(file_len):
        print(file[a]["cityName"])

def main():
    download_json('https://lab.isaaclin.cn/nCoV/api/area?latest=1&province=%E6%B1%9F%E8%A5%BF%E7%9C%81')
    analysis_json()
if __name__ == "__main__":
    main()