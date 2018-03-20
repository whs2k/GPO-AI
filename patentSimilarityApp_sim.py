'''

    Simulate real script.

'''


def init():
    pass


def get_similar_patents(input_text, title='Document Title 1'):

    results = [
        ('Document Number 1', title),
        ('Document Number 2', 'Document Title 2'),
        ('Document Number 3', 'Document Title 3'),
        ('Document Number 4', 'Document Title 4'),
        ('Document Number 5', 'Document Title 5'),
    ]

    return results


if __name__ == '__main__':
    import sys
    from pprint import pprint

    print('results:\n')
    pprint(get_similar_patents(sys.argv[1], title=sys.argv[2]))

