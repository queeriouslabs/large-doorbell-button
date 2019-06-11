import evdev
import simpleaudio

print('Starting doorbell...')

def should_ring(event):
  evcat = evdev.categorize(event)
  return event.type == evdev.ecodes.EV_KEY and \
         'KEY_YEN' == evcat.keycode and \
         1 == evcat.event.value

kb = evdev.InputDevice('/dev/input/event3')
for event in kb.read_loop():
  if should_ring(event):
    wave_obj = simpleaudio.WaveObject.from_wave_file("tng_chime.wav")
    play_obj = wave_obj.play()
    play.obj.wait_done()