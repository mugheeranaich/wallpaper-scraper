import os

os.system("wget 'wallpaperswide.com'")

c = list(filter(lambda x: x != 'webscrapping.py' and x != '.git', os.listdir()))

for i in c:
        with open (i,"r") as f:
            content = f.readlines()

            for i in content:
                line = i.strip()
                if line.startswith("<a href=") and line.endswith('smartphone">'):
                    lin = line.split('"/')
                    link = lin[1].split('"')
                    if link[2] .startswith('View'):
                        c =link[2]
                    else:
                        img = link[0].split('.html')
                        png = img[0].split('-wallpapers')
                        # print(png[0])
                        os.system(f"wget 'https://wallpaperswide.com/download/{png[0]}-wallpaper-1920x1080.jpg'")
