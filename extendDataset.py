import os
import shutil

source = './data/'
target = './data2/'
for i in range(0,66517):
    temp = 133484 + i
    tempsdir = source + '{0:07d}'.format(i) + '_psf.png'
    temptdir = target + '{0:07d}'.format(temp) + '_psf.png'
    try:
        shutil.copy(tempsdir, temptdir)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())
