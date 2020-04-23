import subprocess
import os
import datetime
#start_cut = '00:00:00'
#end_cut = '00:00:20'
#i=1001
#file_name = 'event_'+str(i)+'.mp4'
#x = 'ffmpeg -i /home/clab/Desktop/a1.mp4 -ss'+ start_cut  + ' -to' + end_cut '-c:v copy -c:a copy /home/clab/Desktop/az_00_20.mp4'

#x = "ffmpeg -i /home/clab/Desktop/a1.mp4 -ss {0}  -to {1} -c:v copy -c:a copy {2}".format(start_cut,end_cut,file_name);
#x = ['ffmpeg', '-i', '/home/clab/Desktop/a1.mp4', '-ss' ,start_cut, '-to', end_cut , '-c:v copy -c:a copy' , '/home/clab/Desktop/bhasad00_20.mp4']
#p = subprocess.call(x,shell=True)


# Create Empty list to store seconds
timestamps_seconds = [];
timestamp_hh_mm_ss = []
offset = 10
value = 0
for i in range(480):
    if(i < 480):
        timestamps_seconds.append(value);
        timestamp_hh_mm_ss.append(str(datetime.timedelta(seconds=value)))
        value= value + offset;
var_loop = len(timestamps_seconds) - 2
var_pos = 0
while var_loop > 0:
    i = timestamps_seconds[var_pos]
    j = i+20;
    start_cut = timestamp_hh_mm_ss[var_pos];
    end_cut = timestamp_hh_mm_ss[var_pos + 2]
    file_name = 'event_'+str(i)+'_'+str(j)+'.mp4'
    x = "ffmpeg -i /home/clab/Desktop/a1.mp4 -ss {0}  -to {1} -c:v copy -c:a copy {2}".format(start_cut,end_cut,file_name);
    p = subprocess.call(x,shell=True)
    print("================================================================\n")
    print("================================================================\n")
    print("================================================================\n")
    print(start_cut,"  ",end_cut," ",file_name)
    print("================================================================\n")
    print("================================================================\n")
    print("================================================================\n")
    var_pos = var_pos + 1;
    var_loop = var_loop - 1;


    


