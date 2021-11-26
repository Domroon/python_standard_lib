from pathlib import Path
import gzip


CURRENT = Path.cwd()
FOLDER = CURRENT / 'gzip_playground'


def create_compressed_file(filename:str):
    content = b"Lots of content here"
    with gzip.open(FOLDER / f'{filename}.gz', 'wb') as f:
        f.write(content)


def read_compressed_file(filename:str):
    with gzip.open(FOLDER / filename, 'rb') as f:
        file_content = f.read()

    return file_content


def main():
    # create_compressed_file('hello_there.txt')
    print(read_compressed_file('hello_there.txt.gz'))


if __name__ == '__main__':
    main()