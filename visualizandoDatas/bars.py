import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .2

# Criando os dados
korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

# Colocando os dados no grafico
kor = plt.bar(index, korea_scores, bar_width, alpha=.4, label='Korea')
can = plt.bar(index + 0.2 + bar_width, canada_scores, bar_width, alpha=.4, label='Canada')
ch = plt.bar(index + 0.2, china_scores, bar_width, alpha=.3, label='China')
fra = plt.bar(index + 0.6, france_scores, bar_width, alpha=.4, label='France')


def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2., height*1.05,
                 '%d' % int(height),
                 ha='center',
                 va='bottom')

CreateLabels(kor)
CreateLabels(can)
CreateLabels(ch)
CreateLabels(fra)

plt.ylabel('Mean Score in PISA 2012')
plt.xlabel('Subjects')
plt.title('Test Scores by Country')
plt.xticks(index + .3 / 2, ('Mathemaics', 'Reading', 'Science'))
plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2)
plt.grid(True)

plt.show()