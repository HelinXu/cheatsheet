# cheatsheet

## scp

### Remote to Local

Download multiple files

```
~ » scp helinxu@218.94.122.142:/data2/helin_test_data/data3/color_{0,1,2}.png /Users/xhl/Desktop/allkeyboards/
color_0.png                                                            100%   60KB 433.5KB/s
```

### Local to Remote

Upload single file

```
~ » scp /Users/xhl/Desktop/my_detectron2-main.zip helinxu@218.94.122.142:/home/helinxu/MyDetectron.zip
my_detectron2-main.zip                                                 100%   28MB   4.2MB/s   00:06
```
