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

Upload a folder

```
~ » scp -r /Users/xhl/Desktop/render_train helinxu@218.94.122.142:/home/helinxu/renderTrain
.gitignore                                                             100%   13     0.3KB/s   00:00    
README.md                                                              100%  336     7.1KB/s   00:00    
.gitignore                                                             100% 2062    44.2KB/s   00:00    
render.py                                                              100% 6194   130.5KB/s   00:00    
rle.py                                                                 100%  359     7.6KB/s   00:00    
pose.py                                                                100% 2093    44.7KB/s   00:00    
main.py                                                                100% 4496    96.4KB/s   00:00
```
