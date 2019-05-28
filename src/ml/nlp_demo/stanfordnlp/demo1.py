from stanfordcorenlp import StanfordCoreNLP

model = r"F:\NLP_learnings\standnlp\stanford-corenlp-full-2018-10-05"
nlp_zh = StanfordCoreNLP(model, lang='zh')  #
nlp_en = StanfordCoreNLP(model, lang='zh')

sentence = '代继涛是我的好朋友，广东外国语大学位于广东'
print('Tokenize:', nlp_en.word_tokenize(sentence))
print('Part of Speech:', nlp_en.pos_tag(sentence))
print('Named Entities:', nlp_en.ner(sentence))
print('Constituency Parsing:', nlp_en.parse(sentence))  # 语法树
print('Dependency Parsing:', nlp_en.dependency_parse(sentence))  # 依存句法


def demo():
    nlp = nlp_zh
    fin = open(r'F:\pycharm_workspce\myML_DM_Test\src\ml\nlp_demo\stanfordnlp\data\news.txt', 'r', encoding='utf8')
    fner = open(r'F:\pycharm_workspce\myML_DM_Test\src\ml\nlp_demo\stanfordnlp\data\ner.txt', 'w', encoding='utf8')
    ftag = open(r'F:\pycharm_workspce\myML_DM_Test\src\ml\nlp_demo\stanfordnlp\data\pos_tag.txt', 'w', encoding='utf8')
    for line in fin:
        line = line.strip()
        if len(line) < 1:
            continue

        fner.write(" ".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
        ftag.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")
    fner.close()
    ftag.close()


demo()
nlp_en.close()  # Do not forget to close! The backend server will consume a lot memery
nlp_zh.close()  #
