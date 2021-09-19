from flask import Flask, request, abort
from gensim.models import word2vec

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    try:
        if request.method == 'GET':
            model = word2vec.Word2Vec.load("wiki.model")

            number = int(request.args.get('num', ''))
            positive = request.args.get('positive', '').split(',')

            words = []
            for word in model.wv.most_similar(positive=positive,topn=number):
                words.append(str(word).split("'")[1])

            return str(words)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
