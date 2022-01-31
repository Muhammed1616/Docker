import osfrom flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_youtube('/'):
    target = os.environ.get('TARGET','HELLO PASAM !!!')
    return 'Hello {}\n'.format(target)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)