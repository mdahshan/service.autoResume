'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import xbmc
import xbmcaddon
import xbmcgui
from time import sleep
from natsort import natural_sort

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
FOLDER = ADDON.getSetting('autoresume.save.folder').encode('utf-8', 'ignore')
FREQUENCY = int(ADDON.getSetting('autoresume.frequency'))
DELETESTOP = ADDON.getSetting('autoresume.deletestop') == 'true' or False
PATH = os.path.join(FOLDER, 'autoresume.txt')
SEEKWAIT = 5

def resume():
    if os.path.exists(FOLDER):
      if os.path.exists(PATH):
          
        # Read from autoresume.txt.
        f = open(PATH, 'r')
        mediafile = f.readline().strip()
        position = float(f.readline().strip())
        f.close()
        
        # Read directory to create a playlist
        filename = os.path.basename(mediafile)
        dirname = os.path.dirname(mediafile)
        dirlist = natural_sort(os.listdir(dirname))
        
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        i = 0
        
        # Get the media file offset in the playlist
        for f in dirlist:
            pl.add('{}/{}'.format(dirname, f), index = i)

            if f == filename:
                playoffset = i
            i += 1

        #xbmc.executebuiltin('XBMC.Notification(Playing {} at {} ...)'.format(filename, position))

        mp = xbmc.Player()
        mp.play(pl, xbmcgui.ListItem(), startpos = playoffset)
        sleep(SEEKWAIT)
        mp.seekTime(position)


def recordPosition():
  mp = xbmc.Player()
    
  if mp.isPlaying():
    mediafile = mp.getPlayingFile()
    position = mp.getTime()

    # Write info to file
    f = open(PATH, 'w')
    f.write(mediafile + '\n' + repr(position))
    f.close()
  else:
    if os.path.exists(PATH) and DELETESTOP:
      os.remove(PATH)

def log(msg):
  xbmc.log("%s: %s" % (ADDON_ID, msg), xbmc.LOGDEBUG)

if __name__ == "__main__":
    resume()
    while (not xbmc.abortRequested):
        recordPosition()
        sleep(FREQUENCY)

