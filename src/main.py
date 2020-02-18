from requests import get
from pandas import DataFrame, set_option
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import webbrowser as web
set_option('display.unicode.ambiguous_as_wide', True)
set_option('display.unicode.east_asian_width', True)

file = file_len = city_name = city_quezheng = city_yisi = None
city_siwang = city_chuyuan = city_dist = a = name_list = None


def download_json(url):
    global file, file_len
    file = get(url)
    file = file.json()
    file = file["results"][0]["cities"]
    file_len = len(file)


def analysis_json():
    global file_len, file, city_chuyuan, city_name, city_quezheng
    global city_siwang, city_yisi, city_dist, name_list
    name_list = [file[i]["cityName"] for i in range(file_len)]
    qezheng_list = [file[i]["currentConfirmedCount"] for i in range(file_len)]
    yisi_list = [file[i]["suspectedCount"] for i in range(file_len)]
    siwang_list = [file[i]["deadCount"] for i in range(file_len)]
    chuyuan_list = [file[i]["curedCount"] for i in range(file_len)]
    city_dist = {
        '确诊病例': qezheng_list,
        "疑似病例": yisi_list,
        '死亡病例': siwang_list,
        '出院病历': chuyuan_list
    }
    #city_dist = DataFrame(city_dist, index=name_list)


def data_visualization(name):
    global city_dist, a
    city = []
    #city_dist = list(city_dist.values())
    #print(city_dist)#..
    q, w, e, r = city_dist
    city = list(zip(q, w, e, r))
    #city_dist = city
    #print(city_dist)#..
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    bar.add_xaxis(name)
    t = [i for i in city_dist['确诊病例']]
    print(t)
    bar.add_yaxis(a+'确诊病例', t)
    bar.render('D:/temp.html')

def open_in_web():
    web.open('file:///D:/temp.html')

def main():
    global a, name_list
    a = input('请输入省份、地区或直辖市，如：湖北省、香港、北京市:')
    download_json(
        f'https://lab.isaaclin.cn/nCoV/api/area?latest=1&province={a}')
    analysis_json()
    data_visualization(name_list)
    open_in_web()


if __name__ == "__main__":
    main()
