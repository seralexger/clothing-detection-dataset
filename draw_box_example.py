from PIL import Image
import json
import glob
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


files_list = glob.glob('data/*.json')
img_data = json.loads(open(files_list[random.randint(0, len(files_list)-1)]).read())
normal_img = Image.open('dataset/' + img_data['file_name'])
fig,ax = plt.subplots(1)
for index,item in enumerate(img_data['arr_boxes']):
	box = patches.Rectangle((item['x'], item['y']),  item['width'],  item['height'],linewidth=2,edgecolor=(random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0)) ,facecolor='none', label = item['class'])
	ax = fig.add_subplot(111)
	ax.add_patch(box)
	ax.axis('off')
plt.legend()
plt.imshow(normal_img)
plt.show()