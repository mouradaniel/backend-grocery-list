from flask import Flask
from routes.items import itemsRoute

app = Flask(__name__)

@app.route('/')
def health_check():
  return 'Application is running!'

app.register_blueprint(itemsRoute)

if __name__ == '__main__':
  app.run()