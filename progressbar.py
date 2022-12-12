from time import sleep

from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(1000)):
        print('.', end='')
        sleep(0.1)
