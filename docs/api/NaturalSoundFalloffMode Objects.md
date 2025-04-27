## NaturalSoundFalloffMode Objects

```python
class NaturalSoundFalloffMode(EnumBase)
```

ENatural Sound Falloff Mode

**C++ Source:**

- **Module**: Engine
- **File**: Attenuation.h

<a id="unreal.NaturalSoundFalloffMode.CONTINUES"></a>

#### CONTINUES

0: (Default) Continues attenuating pass falloff max using volume value
specified at the max falloff distance's bounds

<a id="unreal.NaturalSoundFalloffMode.SILENT"></a>

#### SILENT

1: Sound goes silent upon leaving the shape

<a id="unreal.NaturalSoundFalloffMode.HOLD"></a>

#### HOLD

2: Holds the volume value specified at the shapes falloff bounds

<a id="unreal.AudioBusChannels"></a>