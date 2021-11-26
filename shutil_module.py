from pathlib import Path
import shutil
import time

PATH = Path()
CURRENT = PATH.cwd()
HOME = Path.home()
VIDEOS = HOME / 'Videos'
PLAYGROUND = CURRENT / 'shutil_playground'

# shutil.copytree(VIDEOS, PLAYGROUND)

# time.sleep(5)

# shutil.rmtree(PLAYGROUND) # PermissionError

print(shutil.disk_usage('C:/'))

print(f'\{shutil.get_archive_formats()}')

# discover how to archive a folder!

print(f'\n{shutil.get_terminal_size()}')



