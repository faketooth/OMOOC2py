# -*- coding: utf-8 -*-

import os
from bottle import Bottle, route, run, debug, template, request
import sae

app_root = os.path.dirname(__file__) 

app = Bottle()

@app.route('/')
def index():
	return template(os.path.join(app_root, 'template', 'index.tpl'))
	
@app.route('/browse')
@app.route('/history')
@app.route('/reading')
def browse():
	diary = open(os.path.join(app_root,'diary', 'diary.txt'), 'r')
	lines = diary.readlines()
	diary.close()
	return template(os.path.join(app_root, 'template', 'reading.tpl'), content=lines)
	
@app.route('/writing')
@app.route('/new')
@app.route('/new_diary')
def new_diary():
	if request.GET.get('save','').strip():
		newline=request.GET.get('newline', '').strip()
		if newline == '':
			return template(os.path.join(app_root, 'template','new_diary.tpl'))
		
		diary = open(os.path.join(app_root,'diary', 'diary.txt'), 'a')
		diary.write(newline + '\n')
		diary.close()
	return template(os.path.join(app_root, 'template','new_diary.tpl'))
debug(True)	
application = sae.create_wsgi_app(app)
