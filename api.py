from eve import Eve
from settings import HOST

app = Eve()

if __name__ == '__main__':
    app.run(host=HOST)