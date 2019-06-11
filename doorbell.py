import evdev

print('Starting doorbell...')

kb = evdev.InputDevice('/dev/input/event3')
for event in kb.read_loop():
  evcat = evdev.categorize(event)
  if event.type == evdev.ecodes.EV_KEY and \
     'KEY_YEN' == evcat.keycode and \
     1 == evcat.event.value:
    print('ding dong!')
