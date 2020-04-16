import pickle
from ctf_homework import poem
from ctf_homework import pages
from ctf_homework import answers
from flask import Flask, request, render_template_string, url_for


app = Flask(__name__)
ans_dict = answers.Answers()

with open("data/questions.pickle", "rb") as f:
    questions = pickle.load(f)


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
        import os
        return render_template_string(template, os=os)
    else:
        return "Not available now."
