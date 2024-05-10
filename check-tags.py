# read .md file and print contents
import pathlib
import markdown

def check_tags(file):
    data = pathlib.Path(file).read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta'])
    md.convert(data)
    if ('tags' in md.Meta):
        print(md.Meta['tags'])
    else:
        print(file + " has no tags.")

def main():
    file = input()
    check_tags(f'{file}')

main()
