# read .md file and print contents
import pathlib
import markdown

def check_tags(file):
    data = pathlib.Path(file).read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta'])
    md.convert(data)
    print(md.Meta['tags'])

def main():
    files = input().split()
    for file in files:
        check_tags(f'{file}')

main()