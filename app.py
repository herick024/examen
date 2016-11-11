import web
import data

render = web.template.render('views/')
dat = data.Data()


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
        return render.about()
class data:
    def GET(self):
        return render.data(info)
    

if __name__ == '__main__':
    app = web.application(urls,globals())
    web.config.debug = True
    app.run()
