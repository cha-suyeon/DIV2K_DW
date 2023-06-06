# Download DIV2K dataset

This lame script downloads DIVerse 2k (div2k) resolution hight quality images dataset as used for the challenges NTIRE (CVPR 2017 and CVPR 2018) and PIRM (ECCV 2018). More details at [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/).

## 1. Wget

```
wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip
wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_HR.zip
```

## 2. 

First, make sure you installed requirements.


```pip install -r requirements.txt```

Second, set the desired download path to <OUTPUT_DIR>.

```python main.py <OUTPUT_DIR>```