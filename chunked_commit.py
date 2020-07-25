import os
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
dpath = os.path.dirname(os.path.realpath(__file__))
paths = [f'images/train/{p}' for p in os.listdir(f'{dpath}/images/train')] + [f'images/test/{p}' for p in os.listdir(f'{dpath}/images/test')]
cs = [x for x in chunks(paths, 500)]
for i, c in enumerate(cs):
    com = ' '.join([f"'{x}'" for x in c])
    print(f'{i + 1} / {len(cs)}')
    os.system(f'git add {com}')
    print('added')
    os.system(f"git commit -m 'temporary commit'")
    print('committed')
    os.system('git push origin master')
    print('pushed')
