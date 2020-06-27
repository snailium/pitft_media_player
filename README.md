# pitft_media_player

## Dependencies:

1. RPi.GPIO
2. python-uinput (GitHub)[https://github.com/tuomasjjrasanen/python-uinput] (doc)[http://tjjr.fi/sw/python-uinput/]
3. dialog (site)[https://invisible-island.net/dialog/dialog.html]

## Troubleshoot and Tips

### No image on screen if monitor powered later than pi.

Try to force HDMI mode in ```/boot/config.txt```. For example, to force 1080p mode

```
hdmi_force_hotplug=1
hdmi_group=1
hdmi_mode=16
```

For additional information about ```hdmi_mode```, refer to [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/configuration/config-txt/video.md).
