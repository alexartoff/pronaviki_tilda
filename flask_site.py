from flask import Flask, render_template
from flask import request, flash, redirect, url_for
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime


import add
load_dotenv(find_dotenv())
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME')
SITE_URL = 'https://pronaviki.ru'
SITE_TITLE = 'PRO НАВЫКИ'
FORM_ID = '#rec624966349'


@app.route('/', methods=('GET', 'POST'))
async def main():
    context = {
        'title': SITE_TITLE,
        'h1_tag': 'ПОМОГАЮ ЛЮДЯМ </br>НАВЕСТИ ПОРЯДОК В ГОЛОВЕ И В ЖИЗНИ',
        'h1_descr': 'Школа развития эмоционального интеллекта и осознанного родительства',
        'meta_description': 'Школа развития эмоционального интеллекта и осознанного родительства',
        'meta_keywords': 'онлайн школа, эмоциональный интеллект, мягкие навыки, soft skills, авторский курс, Екатерина Тараканова, коучинг, наставничество, работа с убеждениями, реабилитация после бизнес-интенсивов',
        'meta_url': SITE_URL,
    }
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_request = request.form['user_request']
        user_contact = request.form['user_contact']

        if not user_name or not user_request or not user_contact:
            flash('Пожалуйста, заполните все поля формы', category='danger')
            return redirect(url_for('main') + FORM_ID)
        else:
            add.write_to_file(user_name, user_contact, user_request)
            flash(f'<strong>{user_name}!</strong></br>Ваш запрос успешно отправлен', category='success')
            return redirect(url_for('main'))

    if request.method == 'GET':
        return render_template('index.html', context=context)


@app.route('/study', methods=('GET', 'POST'))
async def study():
    date = datetime.now()
    context = {
        'title': SITE_TITLE + ' - КУРС',
        'h1_tag': SITE_TITLE,
        'h1_descr': 'Уникальный курс Екатерины Таракановой для подростков 14+',
        'meta_description': 'Курс обучение гибким навыкам для подростков',
        'meta_keywords': 'адаптивность, принципы, ценности, восприятие критики, постановка целей, выбор профессии, выученная беспомощность, тайм-менеджмент, колесо баланса, развитие психики, эффективная коммуникация, эмоции, эмоциональный интеллект, мягкие навыки, soft skills',
        'meta_url': SITE_URL,
    }
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_request = request.form['user_request']
        user_contact = request.form['user_contact']

        if not user_name or not user_request or not user_contact:
            flash('Пожалуйста, заполните все поля формы', category='danger')
            return redirect(url_for('study')+"#rec624966349")
        else:
            add.write_to_file(user_name, user_contact, user_request)
            flash(f'<strong>{user_name}!</strong></br>Ваш запрос успешно отправлен', category='success')
            return redirect(url_for('study'))

    if request.method == 'GET':
        return render_template('study.html', date=date, context=context)


@app.errorhandler(404)
def page_not_found(e):
    context = {
        'title': SITE_TITLE,
        'h1_tag': 'ПОМОГАЮ ЛЮДЯМ </br>НАВЕСТИ ПОРЯДОК В ГОЛОВЕ И В ЖИЗНИ',
        'h1_descr': 'Школа развития эмоционального интеллекта и осознанного родительства',
        'meta_description': 'Школа развития эмоционального интеллекта и осознанного родительства',
        'meta_keywords': 'онлайн школа, эмоциональный интеллект, мягкие навыки, soft skills, авторский курс, Екатерина Тараканова, коучинг, наставничество, работа с убеждениями, реабилитация после бизнес-интенсивов',
        'meta_url': SITE_URL,
    }
    return render_template('404.html', context=context), 404
