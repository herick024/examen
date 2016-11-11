import web

render = web.template.render('views/')

urls = (
     '/','index',
    '/about','about', 
    '/data', 'data'
)

class index:
     def GET(self):
         return render.index()
class about:
    def GET(self):
        return about
class data:
    def GET(self)
        return.render.data()
    

if __name__ == '__main__':
    app = web.application(urls,globals())
    web.config.debug = True
    app.run()
