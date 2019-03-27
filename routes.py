from bottle import route, view

@route('/')
@view('home')
def render_home():
    return dict(dummy=1)
