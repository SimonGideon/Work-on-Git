# Making things right
import winsound
import os
a = os.getcwd()
f = sorted(list(os.walk(a))[1:], reverse=True)
for fld in f:
    try:
        os.rmdir(fld[0])
        freq = 2500
        dur = 1000
        winsound.Beep(freq, dur)
    except OSError as error:
        print("\U0001F637: Share the prank with your Friend")
