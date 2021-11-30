import os
import shutil
pic_names = os.listdir('./train/')
# label_names = os.listdir('./labels/')
count = 0
for i, name in enumerate(pic_names):
    i = i+818
    os.rename('./train/'+name, './train/fire_smoke_'+str(i)+'.txt')
    # os.rename('./labels/'+label_names[i], './labels/fire_smoke_'+str(i)+'.txt')