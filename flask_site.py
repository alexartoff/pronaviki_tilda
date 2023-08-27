from flask import Flask, render_template, Response
from flask import request, flash, redirect, url_for
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime


# import add
load_dotenv(find_dotenv())
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME')
SITE_URL = 'https://psy-coach.org'
SITE_TITLE = 'Психологический коучинг'
# FORM_ID = '#rec624966349'


@app.route('/', methods=('GET', 'POST'))
async def main():
    context = {
        'title': SITE_TITLE,
        'h1_tag': 'ПОМОГАЮ ЛЮДЯМ </br>НАВЕСТИ ПОРЯДОК В ГОЛОВЕ И В ЖИЗНИ',
        'h1_descr': 'on-line консультации по всему миру',
        'meta_description': 'Психологический коучинг от Екатерины Таракановой - on-line консультации по всему миру',
        'meta_keywords': 'психологический коучинг, консультации, безнес-разбор, эмоциональный интеллект, мягкие навыки, гибкие навыки, soft skills, наставничество, работа с убеждениями, реабилитация после бизнес-интенсивов, Екатерина Тараканова',
        'meta_url': SITE_URL,
        'footer_link': 'main',
    }
    if request.method == 'POST':
        return redirect(url_for('main'))
        # user_name = request.form['user_name']
        # user_request = request.form['user_request']
        # user_contact = request.form['user_contact']

        # if not user_name or not user_request or not user_contact:
        #     flash('Пожалуйста, заполните все поля формы', category='danger')
        #     return redirect(url_for('main') + FORM_ID)
        # else:
        #     add.write_to_file(user_name, user_contact, user_request)
        #     flash(f'<strong>{user_name}!</strong></br>Ваш запрос успешно отправлен', category='success')
        #     return redirect(url_for('main'))

    if request.method == 'GET':
        return render_template('index.html', context=context)


@app.route('/pronaviki', methods=('GET', 'POST'))
async def study():
    date = datetime.now()
    context = {
        'title': SITE_TITLE + ' - курс PRO НАВЫКИ',
        'h1_tag': 'PRO НАВЫКИ',
        'h1_descr': 'Уникальный курс Екатерины Таракановой для подростков 14+',
        'meta_description': 'Курс на развитие гибких навыков и эмоционального интеллекта для подростков от 14 лет от коуча-психолога Екатерины Таракановой',
        'meta_keywords': 'курс, адаптивность, принципы, ценности, восприятие критики, постановка целей, выбор профессии, выученная беспомощность, тайм-менеджмент, колесо баланса, развитие психики, эффективная коммуникация, эмоции, эмоциональный интеллект, мягкие навыки, soft skills',
        'meta_url': SITE_URL,
        'footer_link': 'study',
    }
    if request.method == 'POST':
        return redirect(url_for('study'))
        # user_name = request.form['user_name']
        # user_request = request.form['user_request']
        # user_contact = request.form['user_contact']

        # if not user_name or not user_request or not user_contact:
        #     flash('Пожалуйста, заполните все поля формы', category='danger')
        #     return redirect(url_for('study')+"#rec624966349")
        # else:
        #     add.write_to_file(user_name, user_contact, user_request)
        #     flash(f'<strong>{user_name}!</strong></br>Ваш запрос успешно отправлен', category='success')
        #     return redirect(url_for('study'))

    if request.method == 'GET':
        return render_template('study.html', date=date, context=context)


@app.route("/robots.txt")
async def robots_dot_txt():
    return "User-agent: *\nAllow: /"


@app.route('/sitemap.xml')
async def sitemap_dot_xml():
    sitemap_context = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://psy-coach.org</loc>
      <lastmod>2023-08-27</lastmod>
      <priority>0.9</priority>
   </url>
   <url>
      <loc>https://psy-coach.org/pronaviki</loc>
      <lastmod>2023-08-27</lastmod>
      <priority>0.8</priority>
   </url>
</urlset>'''
    return Response(sitemap_context, mimetype='text/xml')


@app.errorhandler(404)
async def page_not_found(e):
    context = {
        'title': SITE_TITLE,
        'h1_tag': 'ПОМОГАЮ ЛЮДЯМ </br>НАВЕСТИ ПОРЯДОК В ГОЛОВЕ И В ЖИЗНИ',
        'h1_descr': 'on-line консультации по всему миру',
        'meta_description': 'Психологический коучинг от Екатерины Таракановой - on-line консультации по всему миру',
        'meta_keywords': 'психологический коучинг, консультации, безнес-разбор, эмоциональный интеллект, мягкие навыки, гибкие навыки, soft skills, наставничество, работа с убеждениями, реабилитация после бизнес-интенсивов, Екатерина Тараканова',
        'meta_url': SITE_URL,
        'footer_link': 'code404',
    }
    print(f"page_not_found - [{e}]")
    return render_template('404.html', context=context), 404
