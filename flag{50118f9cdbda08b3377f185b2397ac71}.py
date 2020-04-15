import json
from ctf_homework import poem
from ctf_homework import pages
from ctf_homework import answers
from flask import Flask, request, render_template_string


app = Flask(__name__)
ans_dict = answers.Answers()

with open("data/questions.json", "r") as f:
    questions = json.loads(f.read())


@app.route('/', methods=['GET', 'POST'])
def index():
    if pages.check_time():
        template = pages.goldentime()
        return render_template_string(template)
    else:
        answer = request.form['answer'] if request.method == 'POST' else ""
        page = request.args.get('page') if request.args.get('page') else "The Question Game: index"
        template = pages.questions(questions, page, answer, ans_dict)
        return render_template_string(template, page=page, answer=answer)


@app.route('/rewards', methods=['GET', 'POST'])
def rewards():
    if ans_dict.all():
        template = pages.rewards()
        return render_template_string(template, poem=poem)
    else:
        return "Not available now."


@app.route('/thepoem', methods=['GET'])
def the_poems():
    if pages.check_time():
        template = pages.the_poem()
        return render_template_string(template, poem=poem)
    else:
        return "Not available now."


@app.route('/justanaudio', methods=['GET'])
def just_an_audio():
    if pages.check_time():
        template = pages.just_an_audio()
        return render_template_string(template)
    else:
        return "Not available now."


@app.route('/hint254', methods=['GET'])
def hint_254():
    if pages.check_time():
        template = pages.hint_254()
        return render_template_string(template)
    else:
        return "Not available now."


if __name__ == "__main__":
    try:
        app.run('0.0.0.0', 5000, debug=True)
    except KeyboardInterrupt:
        print("[*] Closing...")
    finally:
        ans_dict.close()
        print("[*] Server has been closed.")
