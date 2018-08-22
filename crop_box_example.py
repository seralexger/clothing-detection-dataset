# -*- coding: utf-8 -*-

#########################################################
#
# Alejandro German
# 
# https://github.com/seralexger/clothing-detection-dataset
#
#########################################################



from PIL import Image
import json
import glob
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


files_list = glob.glob('data/*.json')
img_data = json.loads(open(files_list[random.randint(0, len(files_list)-1)]).read())
normal_img = Image.open('dataset/' + img_data['file_name'])

fig=plt.figure(figsize=(8, 8))
columns = 4
if len(img_data['arr_boxes']) > columns:
	rows = int(len(img_data['arr_boxes'])-columns)
else:
	rows = 1
for index,item in enumerate(img_data['arr_boxes']):
	img2 = normal_img.crop((item['x'], item['y'],  item['x']+item['width'],  item['y']+item['height']))
	ax = fig.add_subplot(rows, columns, index+1)
	ax.set_title(item['class'])
	ax.axis('off')
	plt.imshow(img2)
	plt.subplots_adjust(hspace=0.4)
plt.legend()
plt.show()