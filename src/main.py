from requests import get
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import webbrowser as web

file = file_len = city_name = city_quezheng = city_yisi = None
city_siwang = city_chuyuan = city_dist = a = name_list = None


def download_json(url):
    global file, file_len
    file = get(url)
    file = file.json()
    file = file["data"]
    file_len = len(file)


def analysis_json():
    global file_len, file, city_chuyuan, city_name, city_quezheng
    global city_siwang, city_yisi, city_dist, name_list
    name_list = [file[i]["cityName"] for i in range(file_len)]
    qezheng_list = [file[i]["confirmedCount"] for i in range(file_len)]
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
    t1 = [i for i in city_dist['确诊病例']]
    t2 = [i for i in city_dist["疑似病例"]]
    t3 = [i for i in city_dist['死亡病例']]
    t4 = [i for i in city_dist['出院病历']]
    #print(t)
    bar.add_yaxis('确诊病例', t1)
    bar.add_yaxis('疑似病例', t2)
    bar.add_yaxis('死亡病例', t3)
    bar.add_yaxis('出院病例', t4)
    bar.render('D:/temp.html')

def open_in_web():
    web.open('file:///D:/temp.html')

def main():
    global a, name_list
    a = input('请输入省份、地区或直辖市，如：湖北、北京:')
    download_json(
        f'http://www.dzyong.top:3005/yiqing/area?area={a}')
    analysis_json()
    data_visualization(name_list)
    open_in_web()


if __name__ == "__main__":
    main()
