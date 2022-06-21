lista =  ['text  \n\n  more text (1)  \n\n  even more text  \n\n']
aux = lista[0].split('\n\n')
list_final = [e.strip() for e in aux]
list_final.remove('')
print(list_final)