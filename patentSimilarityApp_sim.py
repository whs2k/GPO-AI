'''

    Simulate real script.

'''
from time import sleep


def init():
    sleep(1)
    print('init complete.')


def get_similar_docs(text, title='Document Title 1'):
    print('running get_similar_docs()')
    sleep(6)

    results = [     # Sponsors, Title, URL, summary
        (['S1', 'S2', 'S3'], title,         'http://bit.ly/DB', 'Summary'),
        (['S1', 'S2', 'S3'], 'Doc Title 2', 'http://bit.ly/DB', 'Summary'),
        (['S1', 'S2', 'S3'], 'Doc Title 3', 'http://bit.ly/DB', 'Summary'),
        (['S1', 'S2', 'S3'], 'Doc Title 4', 'http://bit.ly/DB', 'Summary'),
        (['S1', 'S2', 'S3'], 'Doc Title 5', 'http://bit.ly/DB', 'Summary'),
    ]
    return results


if __name__ == '__main__':
    import sys
    from pprint import pprint

    print('results:\n')
    pprint(get_similar_docs(sys.argv[1], title=sys.argv[2]))

