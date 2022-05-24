# DeepLearningBrickRecognition

A deep learning project based on TensorFlow that recognizes color patterns of brick.

# Problem definition

A model needs to learn recognizing following color patterns:
<br/><br/>
![barwy_jesieni](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/brick_patterns/barwy_jesieni.png)
![gothic](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/brick_patterns/gothic.png)
![light](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/brick_patterns/light.png)
![muszlowy](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/brick_patterns/muszlowy.png)
![york](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/brick_patterns/york.png)


In order to do this I converted all image dataset (about 4000 pictures) into histogram bins (from range 0-255). Here is a quick explanation what is "bin":

- "A histogram displays numerical data by grouping data into "bins" of equal width. Each bin is plotted as a bar whose height corresponds to how many data points are in that bin."
