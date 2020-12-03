# CHATBOT <br>

## Tabel of Content<br>

### 1. Introduction<br>

### 2. Demo<br>

### 3. Setup<br>

### 4. Data Preprocessing<br>

### 5. Modeling<br>

### 6. Deployment<br>

### Introduction<br>
ellis is chatbot based on multinomial navai byes algorithm. <br>

### demo<br>

### setup<br>
#### a. linux:<br>
some linux dependency<br>
  sudo apt-get install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev<br>
  sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0<br>
<!---
pip install gobject PyGObject<br>
pip install PyAudio<br>
pip install -r requirements.txt<br>
-->

#### b. windows:<br>
you can download your apropriate vertion of pyaudio from here if you get any error<br>
[pyaudio windows](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)<br>

### data preprocessing<br>
I tried count vectorizer and if-idf vectorizer for word to vec process I found that tf-idf works more efficient in this case. because of many words occur to many times but they are not much usefull to understand the context of sentence like (what, are, is, etc) and we can not directly remove this words as stop words because we will loose some information. while we talking sentences are usually small so we can't loose any relevant information. so tf-idf vectorizer is best way to prevent that for light weight models.
<br>
### modeling<br>
I used multinomial naive byes for this dataset becouse naive byes aproch work well for text data becouse it work on probability.<br>
I messured one interesting thing here when we are incresing number of output classes we have to decrese value of alpha to increase accuracy and at one mininum point accuracy will remain same.<br>
for example:<br>
when my output classes are 120 I need set value of alpha is 0.1 for geting maximum accuracy but when I increase my output classes by 150 i need to set value of alpha is 0.04 to get maximum accuracy.
<br>
### deployment<br>
for deployment part I uesd tkinter lib to build UI. <br>
in chatbot program I used queue data structure for building short term memory. by using it chatbot can identify repetitive occurrence of sentences and reply according to that.
<br>  
#### run app.py





