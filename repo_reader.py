#!../env/bin/python

from github3.github import GitHub
from github3.exceptions import NotFoundError

from cred import USERNAME
from cred import PASSWORD


gh = GitHub(username=USERNAME, password=PASSWORD)


def read_files():
    repo_copy_1 = gh.repository('joeseggie', 'repo-copy-1')
    return repo_copy_1.file_contents('README.md').decoded


def commit_update(content: bytes):
    repo_copy_2 = gh.repository('joeseggie', 'repo-copy-2')

    try:
        repo_copy_2.directory_contents('/', return_as=list)
        repo_copy_2.file_contents('README.md').update('document_update', content, branch='gh-pages')
    except NotFoundError:
        repo_copy_2.create_file('README.md', 'Readme upload', content=content, branch='gh-pages')


def main():
    contents = read_files()
    commit_update(contents)


if __name__ == "__main__":
    main()
