import YoMoPie
import time

yomo = YoMoPie.YoMoPie()
##yomo.init_yomopie()

yomo.set_lines(1)

print yomo.do_n_measurements(5, 1)
        
yomo.close()    