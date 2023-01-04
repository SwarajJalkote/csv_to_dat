from git import Repo
import os
COMMITS_TO_PRINT = 5



def print_commit_data(commit):
    print('-----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))


def print_repository_info(repo):
    print('Repository description: {}'.format(repo.description))
    print('Repository active branch is {}'.format(repo.active_branch))

    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))

    print('Last commit for repository is {}.'.format(str(repo.head.commit.hexsha)))


if __name__ == "__main__":
    # Repo.clone_from("https://github.com/sayansaha91/python-file-read.git", "./clone")
    Repo.clone_from("https://github.com/SwarajJalkote/DrinkSomeWater.git", "./DrinkSomeWater", branch="main")
    repo_path = "./DrinkSomeWater" # os.getenv('REPO_PATH')
    # Repo object used to interact with Git repositories
    repo = Repo(repo_path)
    # print(repo_path)
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository_info(repo)

        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('main'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit_data(commit)
            pass

    else:
        print('Could not load repository at {} :'.format(repo_path))


    print("\n Printing list of branches")
    # for i in repo.heads:
    #     print("Branch: ", i.name)

    remote_branches = []
    for ref in repo.git.branch('-r').split('\n'):
        print("Branch: ",ref)
        remote_branches.append(ref)


    