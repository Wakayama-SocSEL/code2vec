import os
import subprocess
from concurrent.futures import ProcessPoolExecutor
import pandas as pd


def work(page):
    if page.endswith('.c2v') and f'{page}.vectors' not in c2v_list:
        subprocess.run(f'python3 code2vec.py --load models/js_dataset_min5/saved_model_iter5 --test {c2v_dir}/{page} --export_code_vectors', shell=True)
        return page


c2v_dir = '/data/c2v'
c2v_list = os.listdir(c2v_dir)

# target_pages = []
# with open('/data/target_pages.txt', 'r') as f:
#     c2v_pages = [filename.split('.')[0] for filename in c2v_list if filename.endswith('.c2v')]
#     target_pages = [page_id + '.test.c2v' for page_id in f.read().split('\n') if page_id in c2v_pages]
#     target_pages.extend([str(page_id) + '.test.c2v' for page_id in pd.read_csv('/data/target_revision.csv', header=0, usecols=['page_id'])['page_id'].values.tolist()])
#     target_pages = list(set(target_pages))

c2v_pages = [filename for filename in c2v_list if filename.endswith('.c2v')]

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        futures = executor.map(work, c2v_pages)
        for future in futures:
            if future is not None:
                print(future)
