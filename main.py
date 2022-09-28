from flask import Flask, request, send_file
import generator
import os

app = Flask(__name__)


@app.route('/generator', methods=['GET'])
def generate_qr():
    args = request.args
    try:
        filename = generator.generate(args['URL'])
        return send_file(filename, mimetype='image/png')

    except:
        return "Sorry, something went wrong..."
    finally:
        try:
            os.remove(filename)
        except:
            print("Erro ao excluir arquivo")


if __name__ == '__main__':
    app.run(port=2000)
