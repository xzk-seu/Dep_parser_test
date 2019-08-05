from stanfordcorenlp import StanfordCoreNLP

sentence = '张三的爸爸是谁？'

# nlp = StanfordCoreNLP('http://localhost', port=9000)
# StanfordCoreNLP(r'D:\Program Files\stanford-corenlp-full-2018-10-05', lang='zh')

with StanfordCoreNLP('http://localhost', port=9000, lang='zh') as nlp:
    print(nlp.word_tokenize(sentence))
    print(nlp.pos_tag(sentence))
    print(nlp.ner(sentence))
    print(nlp.parse(sentence))
    print(nlp.dependency_parse(sentence))

    dp = nlp.parse(sentence)
    print(type(dp))

    dp = nlp.dependency_parse(sentence)
    print(type(dp))

