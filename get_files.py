import glob, os


os.chdir("D:\lessons\pyt_n\\11 Web Scraping with Python\\")

for file in glob.glob("*.srt"):
    print(file)
    print()