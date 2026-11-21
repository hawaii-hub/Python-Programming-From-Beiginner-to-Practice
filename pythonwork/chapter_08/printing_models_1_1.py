from printing_functions import print_models,show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#禁止函数修改列表，可以创建副本
#print_models(unprinted_designs[:], completed_models)