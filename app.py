import json
from datetime import datetime, time
from ctf_homework import pages
from ctf_homework import answers
from ctf_homework import timeutils
from flask import Flask, request, render_template_string


app = Flask(__name__)
ans_dict = answers.Answers()

with open("data/questions.json", "r") as f:
    questions = json.loads(f.read())


@app.route('/', methods=['GET', 'POST'])
def index():
    now = datetime.now().time()
    if timeutils.in_between(now, time(4), time(5)):
        gt = """
        <title>The Question Game: Golden Time! %nbsp%nbsp%nbsp%nbsp%nbsp flag{40cef608897fbd5358da9a6659b899e3}</title>
        <h2>The Question Game special: Golden Time!</h2>
        """
        return render_template_string(gt)
    else:
        answer = request.form['answer'] if request.method == 'POST' else ""
        page = request.args.get('page') if request.args.get('page') else "The Question Game: index"
        template = pages.questions(questions, page, answer, ans_dict)
        return render_template_string(template, page=page, answer=answer)


@app.route('/rewards', methods=['GET', 'POST'])
def rewards():
    return "flag{h4rghndsjpogjre80gyrg9e4ugpj}" if ans_dict.all() else "Not yet!"


if __name__ == "__main__":
    try:
        app.run('0.0.0.0', 5000, debug=True)
    except KeyboardInterrupt:
        print("[*] Closing...")
    finally:
        ans_dict.close()
        print("[*] Server has been closed.")
