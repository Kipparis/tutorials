## Restart  
`alsactl kill rescan` or `alsactl nrestore`
## High quality resampling
Setup __libspeex-rerived__ resampler instead of linear interpolation.  
## List of loaded modules
`cat /proc/asound/modules`
## Devices and modules list 
`lsmod | grep snd`
## List of cards and devices
`aplay -l`
## Get valid ALSA card names
`aplay -l | awk -F \: '/,/{print $2}' | awk '{print $1}' | uniq`
## The more you know
The 'pcm' options affect which card and device will be used for audio playback while the 'ctl' option affects which card is used by control utilities like alsamixer .  
__Test__ `aplay -D default:PCH your_favourite_sound.wav`
## Equalizers
[https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture](Using
mbeq)
## list of audio-devices and drivers
`lspci -knn|grep -iA2 audio`
