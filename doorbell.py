import evdev

devices = [evdev.InputDevice(path) for path in evdev.util.list_devices()]
for device in devices:
  print(device.path, device.name, device.phys)