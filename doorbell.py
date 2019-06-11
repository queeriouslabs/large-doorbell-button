import evdev
import simpleaudio

print('Starting doorbell...')

def within_valid_timerange(last_event_timestamp, event):
  return not last_event_timestamp or \
             last_event_timestamp + 5 <= event.timestamp()

def is_enter_keydown(event):
  evcat = evdev.categorize(event)
  
  return event.type == evdev.ecodes.EV_KEY and \
         'KEY_YEN' == evcat.keycode and \
         1 == evcat.event.value

def should_ring(last_event_timestamp, event):
  return within_valid_timerange(last_event_timestamp, event) and \
         is_enter_keydown(event)

kb = evdev.InputDevice('/dev/input/event3')
last_event_timestamp = None
for event in kb.read_loop():
  if should_ring(last_event_timestamp, event):
    last_event_timestamp = event.timestamp()
    wave_obj = simpleaudio.WaveObject.from_wave_file("tng_chime.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
