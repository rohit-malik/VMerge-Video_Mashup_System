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

value = 1893
val = 0
while val < 265:
    i = val + value
    j = i+20;
    #start_cut = timestamp_hh_mm_ss[var_pos];
    start_cut = str(datetime.timedelta(seconds=val))
    #end_cut = timestamp_hh_mm_ss[var_pos + 2]
    end_cut = str(datetime.timedelta(seconds=(val+20)))
    file_name = 'event_airplane_stan6_'+str(i)+'_'+str(j)+'.mp4'
    x = "ffmpeg -i ~/VMerge/VMERGE_OVERLAP/VMERGE/overlap/Eminem_Seoul/airplane_stan/E6.mp4 -ss {0}  -to {1} -c:v copy -c:a copy {2}".format(start_cut,end_cut,file_name)
    p = subprocess.call(x,shell=True)
    print("================================================================\n")
    print("================================================================\n")
    print("================================================================\n")
    print(start_cut,"  ",end_cut," ",file_name)
    print("================================================================\n")
    print("================================================================\n")
    print("================================================================\n")
    val = val + 15
    


    


