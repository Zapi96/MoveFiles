
import os
import shutil
from send2trash import send2trash


folder =  "D:\\Imágenes\\Google Fotos"

source_dir = "D:\\Imágenes\\Origin"
target_dir_fotos = "D:\\Imágenes\\Fotos"
target_dir_videos = "D:\\Imágenes\\Videos"

try:
    os.makedirs(target_dir_fotos)
    os.makedirs(target_dir_videos)
except Exception:
    pass

def move_files(source_dir,target_dir_fotos,target_dir_videos):

    for dir in os.listdir(source_dir):
        if '.mp3' in dir.lower() or '.db' in dir.lower() or '.3gp' in dir.lower():
            print('File not valid. Deleting...')
            send2trash(os.path.join(source_dir, dir))

        elif not('.jpg' in dir.lower() or '.jpeg' in dir.lower() or '.png' in dir.lower() \
                            or '.raw' in dir.lower() or '.gif' in dir.lower() or '.mp4' in dir.lower() or '.avi' in dir.lower()
                            or '.mov' in dir.lower() or '.m4v' in dir.lower() or '.mpeg' in dir.lower() or '.mkv' in dir.lower()
                            or '.flv' in dir.lower() or '.wmv' in dir.lower()):
            if dir.lower().endswith('json'):
                send2trash(os.path.join(source_dir,dir))
                print('Deleting json')
                continue
            print(dir)
            file_names = os.listdir(os.path.join(source_dir,dir))



            for file_name in file_names:
                if not '.' in file_name:
                    move_files(os.path.join(source_dir,dir,file_name), target_dir_fotos, target_dir_videos)
                else:
                    if file_name.lower().endswith('json'):
                        send2trash(os.path.join(source_dir, dir,file_name))
                        print('Deleting json')
                        continue
                    if not os.path.exists(os.path.join(target_dir_videos,file_name))  and not os.path.exists(os.path.join(target_dir_fotos,file_name)):
                        print('File ', file_name, ' not in destination folder. Moving...')
                        if '.jpg' in dir.lower() or '.jpeg' in dir.lower() or '.png' in dir.lower() \
                            or '.raw' in dir.lower() or '.gif' in dir.lower() or '.mp4' in dir.lower() or '.avi' in dir.lower() \
                            or '.mpeg' in dir.lower():
                            shutil.move(os.path.join(source_dir, dir,file_name), target_dir_fotos)
                        else:
                            shutil.move(os.path.join(source_dir, dir, file_name),target_dir_videos)
                    else:
                        print('File ',file_name,' already in destination folder. Deleting...')
                        if os.path.exists(os.path.join(target_dir_videos, file_name)):
                            send2trash(os.path.join(target_dir_videos, file_name))
                        elif os.path.exists(os.path.join(target_dir_fotos, file_name)):
                            send2trash(os.path.join(target_dir_fotos, file_name))
            if not os.listdir(os.path.join(source_dir,dir)):
                print('Folder ', dir, ' empty. Deleting...')
                send2trash(os.path.join(source_dir, dir))

        else:
            if dir.lower().endswith('json'):
                send2trash(os.path.join(source_dir, dir))
                print('Deleting json')
                continue
            print(dir)
            if not os.path.exists(os.path.join(target_dir_videos, dir)) and not os.path.exists(
                    os.path.join(target_dir_fotos, dir)):
                print('File ', dir, ' not in destination folder. Moving...')

                if '.jpg' in dir.lower() or '.jpeg' in dir.lower() or '.png' in dir.lower() \
                            or '.raw' in dir.lower() or '.gif' in dir.lower() or '.mp4' in dir.lower() or '.avi' in dir.lower() \
                            or '.mpeg' in dir.lower():
                    shutil.move(os.path.join(source_dir, dir), target_dir_fotos)
                else:
                    shutil.move(os.path.join(source_dir, dir),target_dir_videos)
            else:
                print('File ', dir, ' already in destination folder. Deleting...')
                if os.path.exists(os.path.join(target_dir_videos, dir)):
                    send2trash(os.path.join(target_dir_videos, dir))
                elif os.path.exists(os.path.join(target_dir_fotos, dir)):
                    send2trash(os.path.join(target_dir_fotos, dir))

    if not os.listdir(source_dir):
        print('Folder ', os.path.basename(source_dir), ' empty. Deleting...')
        send2trash(source_dir)



move_files(source_dir,target_dir_fotos,target_dir_videos)
