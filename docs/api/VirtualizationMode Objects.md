## VirtualizationMode Objects

```python
class VirtualizationMode(EnumBase)
```

Method of virtualization when a sound is stopped due to playback constraints
(i.e. by concurrency, priority, and/or MaxChannelCount)
for a given sound.

**C++ Source:**

- **Module**: Engine
- **File**: SoundBase.h

<a id="unreal.VirtualizationMode.DISABLED"></a>

#### DISABLED

0: Virtualization is disabled

<a id="unreal.VirtualizationMode.PLAY_WHEN_SILENT"></a>

#### PLAY_WHEN_SILENT

1: Sound continues to play when silent and not virtualize, continuing to use a voice. If
sound is looping and stopped due to concurrency or channel limit/priority, sound will
restart on realization. If any SoundWave referenced in a SoundCue's waveplayer is set
to 'PlayWhenSilent', entire SoundCue will be overridden to 'PlayWhenSilent' (to maintain
timing over all wave players).

<a id="unreal.VirtualizationMode.RESTART"></a>

#### RESTART

2: If sound is looping, sound restarts from beginning upon realization from being virtual

<a id="unreal.ModulationRouting"></a>