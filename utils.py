import os
import shutil
import zipfile

def unzip_folder(zip_path, output_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)
        
def zip_folder(folder_path, output_zip):
    shutil.make_archive(output_zip, 'zip', folder_path)
        
def push_folder_to_github(local_dir, repo_url='https://github.com/Khoawawa/Art-Detective', commit_message="Updated folder",email='atom08072004@gmail.com',name='Khoawawa'):
    """
    Pushes a specific folder to GitHub from Google Colab.

    Parameters:
    - local_dir (str): The folder to push.
    - repo_url (str): The GitHub repository URL (HTTPS format).
    - commit_message (str): The commit message.
    """
    
    # Extract repo name from URL
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = f"/content/{repo_name}"

    # Clone the repository if it doesn't exist
    if not os.path.exists(repo_path):
        os.system(f"git clone {repo_url}")

    # Move the folder to the cloned repository
    os.system(f"cp -r {local_dir} {repo_path}/")

    # Navigate to the repo
    os.chdir(repo_path)

    # Configure Git (Replace with your GitHub email & username)
    os.system(f"git config --global user.email '{email}'")
    os.system(f"git config --global user.name '{name}'")

    # Add, commit, and push the folder
    os.system(f"git add {local_dir}")
    os.system(f"git commit -m '{commit_message}'")
    os.system("git push origin main")  # Change "main" to the correct branch if needed

    print(f"Folder '{local_dir}' pushed to GitHub successfully!")
