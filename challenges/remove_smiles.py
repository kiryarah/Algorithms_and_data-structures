'''
Удалить смайлики вида :-)))) и :-((
'''

from re import sub


def remove_smiles(string):
    return sub(r':-\)+|:-\(+', '', string)


string = '''
Я работаю в Гугле :-))))
Везет. А я тогда собос завалил:-((((
Лол:)
Aaaaaaaaa!!!!!!!! :-))(())
'''

print(remove_smiles(string))
