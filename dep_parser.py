import stanfordnlp
from stanfordnlp.utils.resources import DEFAULT_MODEL_DIR

print(DEFAULT_MODEL_DIR)
nlp = stanfordnlp.Pipeline(lang='zh')

s = "张三的父亲是谁？"

# doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc = nlp(s)
print(len(doc.sentences))
doc.sentences[0].print_dependencies()
t = doc.sentences[0].dependencies
print(t)
for i in t:
    print(i)
    print(type(i))
    for j in i:
        print(type(j))
        break
