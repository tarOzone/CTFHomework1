from ctf_homework import poem
from ctf_homework import timeutils
from datetime import datetime, time


def check_time():
    now = datetime.now().time()
    return not timeutils.in_between(now, time(4), time(5))


def _body_index():
    return f"""
    <body>
        <h1><font size="7">Welcome to the Question Game</font></h1>
        <p>
            <font size="4">This web site designed for..... Anyway, I hope you ENJOY THE GAME.</font>
        </p>
        <p>
            <font size="4"><a href="./?page=1">Go to the questions! ></a></font><br>
        </p>
    </body>
    """


def _body_question(questions, page, _answer, answer_dict):
    page = max(1, min(4, page))
    prev_page = "./" if page == 1 else f"./?page={page - 1}"
    next_page = f"./?page={ page + 1 }" if page < 4 else "./rewards"
    question = questions["normal"][page - 1]["question"]
    answer = questions["normal"][page - 1]["answers"]

    answer_dict.update(page, _answer == answer)

    return f"""
    <body>
        <h1><font size="7">Question #{ page }</font></h1>
        <p>
            <font size="4">{ question }</font>
            {{% if { answer_dict.ans[str(page)] } %}}
                <h1><font size="4">[ANSWER]: Corrected!</font></h1>
            {{% else %}}
                <form method="POST">
                    <input name="answer", placeholder="your answer here">
                    <input type="submit">
                </form>
            {{% endif %}}
        </p>
        <p>
            <font size="4"><a href="{ prev_page }">&lt; Back</a></font>&nbsp;&nbsp;&nbsp;&nbsp;
            <font size="4"><a href="{ next_page }">Next &gt;</a></font>
        </p>
    </body>
    """


def questions(_questions, page, answer, ans_dict):
    try:
        page = int(page)
        _body = _body_question(_questions, page, answer, ans_dict)
    except ValueError:
        _body = _body_index()
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{ page }</title>
            <meta http-equiv="Location" content="/">
            <style type="text/css">
                a:link {{ color: #3333CC; text-decoration: none}}
                a:visited {{ color: #3333CC; text-decoration: none}}
                a:active {{ color: #0099FF; text-decoration: none}}
                a:hover {{ color: #0099FF; text-decoration: none}}
                textarea {{ resize: none; }}
            </style>
        </head>
        { _body }
        </html>
    """


def _head_golden_time():
    return f"""
    <head>
        <title>The Question Game: Golden Time! %nbsp%nbsp%nbsp%nbsp flag{{40cef608897fbd5358da9a6659b899e3}}</title>
        <meta http-equiv="Location" content="/">
        <style type="text/css">
            a:link {{ color: #3333CC; text-decoration: none}}
            a:visited {{ color: #3333CC; text-decoration: none}}
            a:active {{ color: #0099FF; text-decoration: none}}
            a:hover {{ color: #0099FF; text-decoration: none}}
            textarea {{ resize: none; }}
        </style>
    </head>
    """


def _body_index_golden_time():
    return f"""
    <body>
        <h1><font size="7">Welcome to the Question Game special: Golden Time!</font></h1>
        <h6><font size="5">In this special moment, we have 3 extra questions for you.</font></h6>
        <p>
            <font size="4">All you have to do is do whatever you can to get flags.</font>
            <font size="4">Without any further ado, let's get start!.</font>
        </p>
        <p>
            <font size="4"><a href="./thepoem">The Poem ></a></font><br>
            <font size="4"><a href="./justanaudio">Just an audio ></a></font><br>
            <font size="4"><a href="./hint254">Hint: 254 ></a></font><br>
        </p>
    </body>
    """


def the_poem():
    a = poem.rotate_ans()
    a = f'\"{a}\"'
    return """
    <!DOCTYPE html>
    <html>
    <title>The Question Game: Golden Time - The Poem ... why don't you refresh it again and then ecrypt?</title>
    <h1><div align="center">{{ poem.title }}</div></h1>
    {% for i in poem.body %}
        <div align="center">{{ i | replace(
    """ + a + """
    , "▢") }}</div>
    {% endfor %}
    </html>
    """


def just_an_audio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>The Question Game: Golden Time - Just an audio</title>
    </head>
    <h1><div align="center">f.wav</div></h1>
    <audio controls>
        <source src="static/f.wav" type="audio/wav">
    </audio>
    </html>
    """


def hint_254():
    return """   
    <!DOCTYPE html>
    <html>
    <title>The Question Game: Golden Time - Hint: 254</title>
    <head>
        <title>Index</title>
    </head>
    <body>
        <img src="./static/254.png" alt="User Image">
    </body>
    </html>
    """


def goldentime():
    return f"""
        <!DOCTYPE html>
        <html>
        {_head_golden_time()}
        {_body_index_golden_time()}
        </html>
    """
