## 1. Intro
This is a project in memory of a Chinese peot, 顾城(Gu Cheng), which is named after his most known peom:

>***黑夜给了我黑色的眼睛***
>***我却用它寻找光明***
>***(Dark night endowed me with eyes for darkness,***
>***yet with them I seek light)***

## 2. Mapping
In 1991-1993, Gu Cheng wrote an unfinished set of 52 poems, 城(the City), to recall the place in Beijing where he grow up with deep attachment and memory.

Through the power of his strong imagination, Gu Cheng is able to walk around Beijing even though he was living on another continent, to see things and places which did not exist anymore; he is able to “refurbish” or “rebuild” the gates pulled down, the bricks, the walls, the trees, in a moment, like a god with the power of his poetry and of his enchanting words. 

42 poems in this poem set is named after place in Beijing, for example, 故宫（the Palace Museum), so I use Gaode Map Web API to geocode them and locate them into a map in QGIS to visualize and find patterns of his memory.

This is the geocode map in Chinese.
![geocode](geocoding_poem_place.png)

This is the geocode map in English.
*The official English names of these places are mostly 拼音(Pinyin), the romanization of a phonetic notation for Chinese characters, but my translation is based on its location type and meaning to facilitate understanding. For example, the 柳荫街(Liu Yin Jie) is translated as "Willow-shade Street".*
![geocode_english](assets/geocoding_poem_place.png)

## 3. Findings
Here are patterns I found according to the map:

1. EVEN: Places in his poems have a relatively even distribution inside Beijing Second Ring Road, with is known as the "old city part". 

2. TWO-SIDES: Place in poems written in 1991 and 1992 mainly distributed in the west and east sides of Beijing respectively.

3. SHRINKING: Place range shrinked regularly from 1991 to 1993, and four place mentioned in 1993 are all in the "old city part".

4. BRIDGE: Bridge is the most mentioned place type, for example, 白石桥(Baishi Bridge).

Additionally, as I used the Mean Coordinates tool in QGIS to explore the places, I realize the point with mean coords of all places is pretty near the hospital he was born, which is an geographical coincide or metaphor that makes me cry... 

The reversed geocoding shows this point is 中国儿童中心(China National Children's Center), and considering his hazy and sometimes child-like writing style, this is something even more profound.

![geo_coincidence](assets/mean_coords.png)

## 4. Mourning 

On Oct 7th, the day before Gu Cheng's death anniversary, I decide to mourn him by going to several important places to him, and planned my route using Gaode Map JS API.




## 4. TODO

- take screenshot of route planning using Gaode JS API
- share photos of my ill-fated jounery(haha I'll explain why!)

## Note

I declare NO interest to his love affarir, relationship, and homicide! It is his poems, and poems only that make me nostalgic and mourn him in this way.

## Reference

[One Generation's translation](https://leonarddurso.com/2016/02/08/one-generation-by-gu-cheng/)

MARGARITO, A. S. (2012). Reflections of the West in Gu Cheng’s Life and Poems. Asian Studies, -16(2), 3–19. https://doi.org/10.4312/as.2012.-16.2.3-19

[顾城之城(Archive of Gu Cheng)](http://www.gucheng.net/index.htm)
