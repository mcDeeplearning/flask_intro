from flask import Flask, render_template, request
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/welcome")
def welcome():
    return "welcome flask!!!"
    
@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요!!!</h1>"
    
@app.route("/html_line")
def html_lint():
    return """
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("file.html")

@app.route("/hello_p/<string:name>")
def hello_p(name):
    return render_template("hello.html",people_name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    result = num**3 #num*num*num
    return render_template("cube.html",result=result, num=num)
    # 사용자가 입력한 숫자를 받아서
    # 세제곱 후 cube.html파일을 통해 응답
    
@app.route("/lunch")
def lunch():
    list = ["20층","짜장면","김밥","탕수육"]
    dict = {
        "20층":'https://scontent-dfw5-2.cdninstagram.com/vp/92d3ed9ada50b8a1ec3ac68a3cf40265/5C578CE8/t51.2885-15/e35/s480x480/20987024_1431422050287339_2004189507347283968_n.jpg',
        "짜장면":'http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg',
        "김밥":'http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg',
        "탕수육":'http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg'
    }
    pick = random.choice(list)
    url = dict[pick]
    return render_template("lunch.html",pick=pick, url=url)

@app.route("/lotto")
def lotto():
    num_list = list(range(1,46))
    lucky = random.sample(num_list,6)
    return render_template("lotto.html",lucky = sorted(lucky))
    
@app.route("/naver")
def naver():
    return render_template("naver.html")
    
@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/hell")
def hell():
    return render_template("hell.html")

@app.route("/hi")
def hi():
    user_name = request.args.get('name')
    return render_template("hi.html", user_name=user_name)
    

@app.route("/summoner")
def summoner():
    return render_template("summoner.html")

@app.route("/opgg")
def opgg():
    summoner = request.args.get('summoner')
    url = 'http://www.op.gg/summoner/userName='
    print(url+summoner)
    html = requests.get(url+summoner).text
    soup = BeautifulSoup(html, 'html.parser')
    
    win = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    lose = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text
    
    # print(type(win))
    # win의 타입이 bs4의 element여서 바로 리턴 불가
    
    return render_template("opgg.html",summoner=summoner,win=win,lose=lose)
    
    