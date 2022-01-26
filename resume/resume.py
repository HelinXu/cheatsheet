import os
import time

ret = 99
resume_count = 0
while ret == 99 and resume_count < 10:
    resume_count += 1
    ret = os.system('bash run.sh')
    time.sleep(1)
    ret = ret // 256
    print(f'resume: {resume_count}')
    
print('Finished')