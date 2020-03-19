# Junk File Organizer


import os, shutil
file_extensions={
       'Audio':('.mp3','.wav','.flac', '.m4a', '.aac'),
       'Video':('.mp4','.mkv','.MKV','.flv','.mpeg'),
       'Images':('.jpeg', '.jpg', '.tiff', '.gif', '.png'),
       'Docs':('.doc','.pdf','.txt','.docx','.xls', '.xlsx', '.ppt', '.pptx', '.xps'),
       'Archives':('.zip', '.7z', '.rar'),
       'Others':('.exe', '.apk', '.bat', '.bin'),
       'Programming':('.py', '.htm', '.html', '.html5', '.css', '.php', '.js')
}
parent_folder={
    "Organized":('Audio','Video','Images','Docs','Archives','Others','Programming')
}

# My Demo Path = C:\Users\pijus\Desktop\DemoDesktop

folderpath = input('Enter Your Folder Path To Sort The Files: ')

def file_finder(folderpath,file_extensions):
    files=[]
    for file in os.listdir(folderpath):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    # files=os.listdir(os.getcwd())
    # files.sort(os.stat(file).st_size,reverse=True)
    return files 

# print(file_finder(folderpath,audio_extensions))
for extensions_type,extension_tuple in file_extensions.items():
    # print('calling file finder')
    # print(file_finder(folderpath,extension_tuple))
    folder_name=extensions_type.split('_')[0]
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in (file_finder(folderpath,extension_tuple)):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)

for extensions_type,extension_tuple in parent_folder.items():
    # print('calling file finder')
    # print(file_finder(folderpath,extension_tuple))
    folder_name=extensions_type.split('_')[0]
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in (file_finder(folderpath,extension_tuple)):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)