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

value = 2760
val = 0
while val < 280:
    i = val + value
    j = i+30;
    #start_cut = timestamp_hh_mm_ss[var_pos];
    start_cut = str(datetime.timedelta(seconds=val))
    #end_cut = timestamp_hh_mm_ss[var_pos + 2]
    end_cut = str(datetime.timedelta(seconds=(val+30)))
    file_name = 'event_till_i_collapse2_'+str(i)+'_'+str(j)+'.mp4'
    x = "ffmpeg -i ~/VMerge/VMERGE_OVERLAP/VMERGE/overlap/Eminem_Seoul/till_i_collapse__cindrella/E2.mp4 -ss {0}  -to {1} -c:v copy -c:a copy {2}".format(start_cut,end_cut,file_name)
    p = subprocess.call(x,shell=True)
    print("================================================================\n")
    print("================================================================\n")
    print("================================================================\n")
    print(start_cut,"  ",end_cut," ",file_name)
    print("================================================================\n")
    print("================================================================\n")
    print("================================================================\n")
    val = val + 10
    


    


