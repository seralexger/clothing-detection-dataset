# Clothing detection dataset

I have created a dataset with wild images where garments are detected, I have gotten all the images from instagram. The are two files, the "dataset.zip", where you can find all the images and the "data.zip", where there are the jsons with the metadata of the images. 

## Getting Started

All the necesary libraries for run the project are in the requirements.txt.

### Example

In draw_box_example.py there is an example code to draw the boxes, and in crop_example.py there is an example code to crop the clothes of the image.


#### Draw box example

![alt text](https://raw.githubusercontent.com/seralexger/clothing-detection-dataset/master/readme_images/img_draw_example.png)


### Data JSON scheme example

```
{
    "arr_boxes": [
        {
            "x": 221.32390916347504,
            "y": 624.6319770812988,
            "width": 78.0220752954483,
            "height": 43.4633731842041,
            "genre": "mujer",
            "class": "gafas de sol"
        },
        {
            "x": 345.8838129043579,
            "y": 650.0715896487236,
            "width": 80.0260877609253,
            "height": 46.52789086103439,
            "genre": "mujer",
            "class": "gafas de sol"
        },
        {
            "x": 462.4635708332062,
            "y": 643.2647868990898,
            "width": 80.10356068611145,
            "height": 51.223500072956085,
            "genre": "mujer",
            "class": "gafas de sol"
        },
        {
            "x": 248.01238238811493,
            "y": 1268.1888163089752,
            "width": 122.82929956912994,
            "height": 67.63978600502014,
            "genre": "mujer",
            "class": "zapatos"
        },
        {
            "x": 498.22065711021423,
            "y": 1232.948613166809,
            "width": 101.950603723526,
            "height": 85.60903072357178,
            "genre": "mujer",
            "class": "zapatos"
        },
        {
            "x": 296.8093013763428,
            "y": 697.8735029697418,
            "width": 186.79794073104858,
            "height": 238.04175853729248,
            "genre": "mujer",
            "class": "camisas"
        },
        {
            "x": 172.84747123718262,
            "y": 697.6209998130798,
            "width": 186.8482804298401,
            "height": 239.25325870513916,
            "genre": "mujer",
            "class": "chaquetas"
        },
        {
            "x": 301.18216037750244,
            "y": 921.2495595216751,
            "width": 160.36638021469116,
            "height": 308.5134744644165,
            "genre": "mujer",
            "class": "pantalones"
        },
        {
            "x": 484.19432401657104,
            "y": 920.1821744441986,
            "width": 218.4789276123047,
            "height": 296.2758421897888,
            "genre": "mujer",
            "class": "falda"
        },
        {
            "x": 448.34460496902466,
            "y": 699.9615222215652,
            "width": 213.53031635284424,
            "height": 305.36177158355713,
            "genre": "mujer",
            "class": "chaquetas"
        }
    ],
    "file_name": "df5wx01jni2eac5fk8039f1zf0xzxe2vdehgoo9ai1dh1pgl80iy55xs2uwn59w9.jpg"
}
```