from mmwave.dataloader import DCA1000
import time
from datetime import datetime
import sys
import numpy as np

dca = DCA1000()
if len(sys.argv) > 2:
    num_frames = sys.argv[1]
    user = sys.argv[2]
start_time = time.time()
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
user=user.split("/")[-1]
print(user)
adc_data = dca.read(num_frames=int(num_frames))
end_time = time.time()
total_time = end_time-start_time
print("Total time: ", total_time)
print("FPS:", int(num_frames)/total_time) 
print(adc_data.shape)
filename = f"adc_data_{current_time}_{user}.npy"
np.save(filename, adc_data)
