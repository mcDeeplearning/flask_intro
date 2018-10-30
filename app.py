from flask import Flask, render_template
import random

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
    
    
    
    