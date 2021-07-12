import pathlib


for p in pathlib.Path.cwd().glob('*.txt'):
    new_p = p.parent.joinpath('archive', p.name)
    p.replace(new_p)
