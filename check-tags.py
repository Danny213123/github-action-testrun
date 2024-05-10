# read .md file and print contents
import pathlib
import markdown
import csv

def check_tags(file):
    data = pathlib.Path(file).read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta'])
    md.convert(data)

    tags_path = '.taglist.csv'
    approved_tags = []
    with open(tags_path, 'r') as f:
        approved_tags = csv.DictReader(f)
        approved_tags = [row['tags'] for row in approved_tags]
        approved_tags = approved_tags[0]

    # print(approved_tags)

    if ('tags' in md.Meta):
        md_tags = md.Meta['tags'][0].split(', ')
        for tag in md_tags:
            if tag not in approved_tags:
                print(f'{file} has an unapproved tag: {tag}. Please check the spelling or check the taglist.')
                exit (1)
            else:
                # print(f'{file} has an approved tag: {tag}.')
                pass

def main():
    file = input()
    check_tags(f'{file}')

main()
