service.autoResume
==================

XBMC service add-on that remembers what was playing and where it left off when power is abruptly cut off. Resumes playing it when power is restored.

The intent of autoResume is for XBMC running in a car.  If using a Raspberry Pi, it's recommended that the "Save Folder" setting point to a folder that is not on your SD card that the RPi boots from to minimize the risk of XBMC doing any writes to the SD card at the time power is cut off.  If using an external USB drive for media, set the "Save Folder" setting to save there.

This is a forked version based on the service.autoResume addon developed by gatorfreak. The main change is supporting resuming the next media file in the directory, using natural sorting for directory listing.

## References

* [https://kodi.wiki/view/List_of_built-in_functions](https://kodi.wiki/view/List_of_built-in_functions)
* [https://forum.kodi.tv/showthread.php?tid=310745](https://forum.kodi.tv/showthread.php?tid=310745)
* [https://kodi.wiki/view/Add-on_settings](https://kodi.wiki/view/Add-on_settings)

