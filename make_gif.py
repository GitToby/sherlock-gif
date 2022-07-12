from pathlib import Path

import imageio.v3 as iio
from pygifsicle import optimize

ROOT_DIR = Path(__file__).parent
filenames = (ROOT_DIR / "imgs").glob("*")

images = []
for filename in filenames:
    print(filename.resolve())
    imread = iio.imread(filename)
    images.append(imread)

gif_out = ROOT_DIR / 'movie.gif'
print(f'writing to {gif_out}')
iio.imwrite(gif_out, images)
print('done')

# dl this from ports and use cli
# http://www.lcdf.org/gifsicle/
# optimize(gif_out)
# gifsicle.exe -O3 ".\movie.gif" -o ".\movie_2.gif" --scale 0.2
