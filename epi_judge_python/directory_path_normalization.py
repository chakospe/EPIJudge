from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError
    path_names = []
    if path[0] == '/':
        path_names.append('/')
    for token in path.split('/'):
        if token == '' or token == '.':
            continue
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append('..')
            else:
                if path_names[-1] == '/':
                    raise ValueError
                path_names.pop()
        else:
            path_names.append(token)
    result = '/'.join(path_names)
    return result[result.startswith('//'):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
