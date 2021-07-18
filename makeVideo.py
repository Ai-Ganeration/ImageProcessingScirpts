import imageio
import time
import numpy as np
from pathlib import Path
from PIL import Image
from tqdm import tqdm

def make_project_progress_mp4():
    current_folder = Path('.')
    current_folder_list = list(Path('').iterdir())
    movieName = Path(current_folder, 'out_movie_{0}.mp4'.format(int(time.time())))

    result_size = 512

    with imageio.get_writer(movieName, mode='I') as writer:
         for img_num in tqdm(range(len(current_folder_list))):
             all_image_paths = [x for x in current_folder_list if x.name.endswith('png') and '{0:04d}'.format(img_num) in x.name]
             for image_path in all_image_paths:
                canvas = Image.new('RGB', (result_size, result_size))
                canvas.paste(Image.fromarray(imageio.imread(image_path)).resize((result_size, result_size)), (0, 0))
                writer.append_data(np.array(canvas))
  
make_project_progress_mp4()
