import sounddevice as sd
import numpy as np
import time

# Parameters
record_duration = 5  # seconds to record
loop_minutes = 1  # total loop time in minutes
interval_between_loops = 10  # seconds to wait between playbacks

fs = 44100  # sample rate

print("Recording started now, tell something...")
recording = sd.rec(int(record_duration * fs), samplerate=fs, channels=1, dtype='float32')
sd.wait()
print("Recording finished.")

# Loop playback with delay
end_time = time.time() + (loop_minutes * 60)
while time.time() < end_time:
    print("Playing recorded audio...")
    sd.play(recording, samplerate=fs)
    sd.wait()

    print(f"Waiting {interval_between_loops} seconds before replaying...")
    time.sleep(interval_between_loops)

print("Done looping.")
