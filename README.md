# Point_man
A toolbox for pointing in certain pictures
## 1. Quick start
    python Img_Label.py  --img_path         \path\to\images     \
                         --is_log                               \
                         --log_name        \name\of\logfile     \
                         --mask_name          \name\of\mask     \
                         --label_class       \name\of\class     \
logfile and mask pictures will be stored in data, as the structure followed  

    |---dir\to\project---data---classname_1---maskname----mask_001 
    |                      |         |            |-------mask_002  
    |                      |         |            |-------mask_003  
    |                      |         |            |-------...  
    |                      |         |  
    |                      |         |---------------------logfile1
    |                      |    
    |                      |-----classname_2---maskname----mask_001 
    |                      |         |            |--------mask_002  
    |                      |         |            |--------mask_003  
    |                      |         |            |-------...  
    |                      |         |  
    |                      |         |----------------------logfile2 
    |                      |-----...

## 2. video splite
our images are generated from a video, which means that we have to split the video into several frames 

    python src/split_video.py --video_path      \path\to\video      \
                              --number_frames   \number\of\frames   \
                         
these images generated will be saved as followed  
  
  
    |---dir\to\project------img---video_name1----pic_001  
    |                        |          |--------pic_002  
    |                        |          |--------pic_003  
    |                        |          |-------...  
    |                        |  
    |                        |----video_name2----pic_001  
    |                        |          |--------pic_002  
    |                        |          |--------pic_003  
    |                        |          |-------...  
    |                        |----...  
