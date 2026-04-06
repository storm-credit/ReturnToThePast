@echo off
git init
git add .
git commit -m "Initialize repository"
git branch -M main
git remote add origin https://github.com/storm-credit/ReturnToThePast.git
git push -u origin main
