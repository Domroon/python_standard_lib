from pathlib import Path
from os import listdir

PATH = Path()
CURRENT= PATH.cwd()
HOME = PATH.home()
WORKSPACE = HOME / 'workspace'
HTML_FOLDER = CURRENT / 'calendar_html_output'
HTML_FILE = HTML_FOLDER / listdir(HTML_FOLDER)[0]

print(f'\n{CURRENT}')
print(f'\n{HTML_FOLDER}')
print(f'\n{HTML_FILE}')

print(f'\n{HTML_FOLDER.is_dir()}')
print(f'\n{HTML_FOLDER.is_file()}')
print(f'\n{HTML_FILE.is_file()}')

print(f'\nHTML FILE: \n{HTML_FILE.read_text()}')

for folder in CURRENT.iterdir():
    print(folder)

print(f'\n{HOME}')
print(f'\n{HTML_FILE.stat()}')
