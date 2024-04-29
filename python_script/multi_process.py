import os
from tqdm import tqdm
import json
import ffmpeg
from multiprocessing import Pool

src_dir = "/home/v-shuhuairen/mycontainer/data/yttemporal180m/raw_videos"
dst_dir = "/home/v-shuhuairen/mycontainer/data/yttemporal180m/videos"
if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

def convert_video(video_name):
    src_path = os.path.join(src_dir, video_name)
    dst_path = os.path.join(dst_dir, os.path.splitext(video_name)[0] + '.mp4')
    try:
        ffmpeg.input(src_path).filter('pad', 'ceil(iw/2)*2', 'ceil(ih/2)*2').output(dst_path, vcodec='libx264').run()
    except ffmpeg.Error as e:
        print('Error:', e)


videos = os.listdir(src_dir)

with Pool() as p:
    p.map(convert_video, videos)
