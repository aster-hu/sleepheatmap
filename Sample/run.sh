cd /Users/aster/sleepheatmap # Change it to local file path
python3 sleepheatmap.py

# Push changes to git repo, if any
git diff
git config user.email "USEREMAIL"
git config user.name "USERNAME"
git add -A
git commit -m "Update sleep data" || exit 0
git push

