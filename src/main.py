from reptile import reptile
import gui
from pyecharts import Bar


def main():

    data = reptile('https://lab.isaaclin.cn/nCoV/api/area?latest=1&province=' +
                   gui.var.get())
    data = data["results"][0]["cities"]
    name = [i["cityName"] for i in data]
    quezheng = [i['confirmedCount'] for i in data]
    chuyuan = [i['curedCount'] for i in data]
    siwang = [i for i in data]
    bar = Bar(gui.var.get(), '疫情状态')
    bar.add('确诊病例',
            name,
            quezheng,
            mark_line=["average"],
            mark_point=["max", "min"])
    bar.add('出院病例',
            name,
            chuyuan,
            mark_line=["average"],
            mark_point=["max", "min"])
    bar.add('死亡病例',
            name,
            siwang,
            mark_line=["average"],
            mark_point=["max", "min"])
    bar.render(path='D:/temp.html')


if __name__ == "__main__":
    gui.init()