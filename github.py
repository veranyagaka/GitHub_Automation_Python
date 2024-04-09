import subprocess
def git_push():
    try:
        repo_path = input("Enter the path to your local repository: ")
        #initialization
        subprocess.run(['git', 'init'], cwd=repo_path, check=True)
        print("Initialized empty Git repository.")

        #staging
        subprocess.run(['git','add', '.'], cwd=repo_path, check=True)
        print("Added all changes to staging area.")

        #commit
        commit_message = input("Enter the commit message: ")
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)
        print("Committed changes with message: ", commit_message)
        #remote origin
        remote_origin = input("Enter the URL of the remote origin: (e.g., 'git remote add origin https://github.com/veranyagaka/test.git'): ")
        
        # Add remote origin
        subprocess.run(['git', 'remote', 'add', 'origin', remote_origin], cwd=repo_path, check=True)
        print("Added remote origin:", remote_origin)
        # Renaming to 'main' i always forget this step but really GitHub whyyyy
        subprocess.run(['git', 'branch', '-M', 'main'], cwd=repo_path, check=True)
        print("Renamed the default branch to 'main'.")
        #Another branch maybe? 
        #branch_name = input("Enter the branch name (e.g., 'main'): ")

        #push
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=repo_path, check=True)
        print("Changes pushed successfully to 'main' branch.")
        print('Pushed changes successfully, Vera!')
    except subprocess.CalledProcessError as e:
        print("MAYDAY!:", e)
if __name__ == "__main__":
    git_push()