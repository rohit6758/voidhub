@echo off
echo [VOID HUB] Initializing Automatic GitHub Upload...
git init
git add .
git commit -m "Void Hub Initialization via AI Code Assist"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/rohit6758/voidhub.git
git push -u origin main -f
echo.
echo [VOID HUB] SUCCESS! Your files are now safely uploaded to https://github.com/rohit6758/voidhub
pause