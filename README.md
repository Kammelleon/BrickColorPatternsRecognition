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


In order to do this I converted all image dataset (about 4000 pictures) into histograms with bins from range 0-255. Here is a quick explanation what is "bin":

- "A histogram displays numerical data by grouping data into "bins" of equal width. Each bin is plotted as a bar whose height corresponds to how many data points are in that bin."
</br>

![example_histogram](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/preview_pictures/example_histogram.png)


So I decided to take these data points from vertical bars and put them in .csv file.
- Every column represents one bin
- Every cell in row represents one value from that bin
- Every row represents new image


So let's say we take first cell in this dataset:
</br>


![dataset](https://github.com/Kamelleon/DeepLearningBrickRecognition/blob/main/preview_pictures/data.png)


</br>
and this value tells us that in the first picture on bin with number 0 we have 31604 data points corresponding to that bin.

At this point we can feed our network and shuffle the data using "sample" method from pandas library.

# Results
Train accuracy: 92%

Test accuracy: 93%

