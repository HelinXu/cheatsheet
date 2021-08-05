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

[SCP](https://linux.die.net/man/1/scp) is a great resource for copying files from server to server. Unfortunately,
I use it infrequently enough that I never remember the syntax.

---

### Local to Remote

- Copy file from the local host to a remote host
`scp /path/to/myfile.txt username@remotehost:/some/remote/directory`

- Copy files from from the local host to your home directory on the remote host
`scp /path/to/myfile.txt /path/to/myotherfile.txt username@remotehost:~`

- Copy file from the local host to a remote host using port 2264
`scp -P 2264 /path/to/myfile.txt username@remotehost:/some/remote/directory`

- Copy directory from the local host to a remote host
`scp -r /some/local/directory/ username@remotehost:/some/remote/directory/`

---

### Remote to Local
- Copy file from a remote host to the local host
`scp username@remotehost:/path/to/myfile.txt /some/local/path/to/myfile.txt`

- Copy file from the remote host to your current directory on the local host
`scp username@remotehost:/path/to/myfile.txt .`

---

### Remote to Remote
- Copy file from one remote host to another
`scp username@remotehost:/some/remote/directory/myfile.txt username@otherremotehost:/some/remote/directory/`
