#!/usr/bin/env python3
import argparse
import copy
import json


class Book(object):
    def __init__(self):
        self.title = None
        self.isbn = None
        self.pages = {}
        self.stories = []

    def load_data(self, data):
        if 'title' in data:
            self.title = data['title']
        if 'isbn' in data:
            self.isbn = data['isbn']
        if 'pages' in data:
            for page in data['pages']:
                page_no = page[0]
                next_pages = page[1]
                if page_no not in self.pages:
                    self.pages[page_no] = next_pages

    def load_json(self, fname):
        with open(fname, 'r') as fp:
            data = json.load(fp)
            self.load_data(data)

    def find_stories(self):
        pending_stories = []
        first_page = [k for k in self.pages.keys() if k == min(self.pages.keys())][0]
        story = Story()
        story.pages.append(first_page)
        pending_stories.append(story)
        while len(pending_stories):
            story = pending_stories.pop()
            last_page = story.pages[-1]
            next_pages = self.pages[last_page]
            if next_pages is None:
                self.stories.append(story)
            else:
                for page in next_pages:
                    new_story = copy.deepcopy(story)
                    new_story.pages.append(page)
                    pending_stories.append(new_story)

    def print_stats(self):
        print('Libro: {} ({})'.format(self.title, self.isbn))
        print('Páginas: {}'.format(len(self.pages)))
        print('Finales: {}'.format(len([k for k, v in self.pages.items() if v is None])))
        print('Historias: {}'.format(len(self.stories)))
        for story in self.stories:
            pages = [str(x) for x in story.pages]
            print(' - {}'.format(', '.join(pages)))


class Story(object):
    def __init__(self):
        self.pages = []

    def __str__(self):
        return str(self.pages)


def main():
    parser = argparse.ArgumentParser(description='Analiza un libro de "Elige tu propia Aventura".')
    parser.add_argument('--file', dest='fname', action='store', required=True,
                        help='Nombre del archivo a procesar.')

    args = parser.parse_args()
    book = Book()
    book.load_json(args.fname)
    book.find_stories()
    book.print_stats()


if __name__ == '__main__':
    main()
