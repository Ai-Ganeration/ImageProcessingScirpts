import random
from pathlib import Path

photo_paths = [x for x in Path('.').iterdir() if str(x).endswith('.png')]
photo_number = len(photo_paths)
random_list = random.sample(range(1000),301)

assert(photo_number == len(random_list))
for i in range(len(photo_paths)):
    photo_paths[i].rename(f'{str(random_list[i]).zfill(4)}.png')
