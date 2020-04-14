def _head(page):
    return f"""
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
    """


def _body_index():
    return f"""
    <body>
        <h1><font size="7">Welcome to the Question Game</font></h1>
        <p>
            <font size="4">This web site designed for..... Anyway, I hope you ENJOY THE GAME.</font>
        </p>
        <p>
            <font size="4"><a href="./?page=1">Go to the riddles! ></a></font><br>
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
        { _head(page) }
        { _body }
        </html>
    """
