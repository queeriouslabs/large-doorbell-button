import evdev
import simpleaudio
import time


def within_valid_timerange(last_event_timestamp, event):
    return not last_event_timestamp or \
        last_event_timestamp + 2 <= event.timestamp()


def is_enter_keydown(event):
    evcat = evdev.categorize(event)

    return event.type == evdev.ecodes.EV_KEY and \
        'KEY_YEN' == evcat.keycode and \
        1 == evcat.event.value


def should_ring(last_event_timestamp, event):
    return within_valid_timerange(last_event_timestamp, event) and \
        is_enter_keydown(event)


while True:
    try:
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        button_path = None
        for device in devices:
            print(device.path, device.name, device.phys)
            if 'SIGMACHIP' in device.name:
                button_path = device.path

        if not button_path:
            print('No doorbell. :(')
            raise
        else:
            print('Found doorbell: ' + button_path)
            button = evdev.InputDevice(button_path)
            last_event_timestamp = None
            for event in button.read_loop():
                if should_ring(last_event_timestamp, event):
                    last_event_timestamp = event.timestamp()
                    wave_obj = simpleaudio.WaveObject.from_wave_file(
                        "voy_door_chime.wav")
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
    except:
        time.sleep(30)
