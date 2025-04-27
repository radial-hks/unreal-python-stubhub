## SoundWaveEnvelopeDataPerSound Objects

```python
class SoundWaveEnvelopeDataPerSound(StructBase)
```

Sound Wave Envelope Data Per Sound

**C++ Source:**

- **Module**: Engine
- **File**: SoundWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``envelope`` (float):  [Read-Write] The current envelope of the playing sound
- ``playback_time`` (float):  [Read-Write] The current playback time of this sound wave
- ``sound_wave`` (SoundWave):  [Read-Write] The sound wave this envelope data is associated with

<a id="unreal.SoundWaveEnvelopeDataPerSound.__init__"></a>

#### __init__

```python
def __init__(envelope: float = 0.000000,
             playback_time: float = 0.000000,
             sound_wave: SoundWave = None) -> None
```

<a id="unreal.SoundWaveEnvelopeDataPerSound.envelope"></a>

#### envelope

```python
@property
def envelope() -> float
```

(float):  [Read-Write] The current envelope of the playing sound

<a id="unreal.SoundWaveEnvelopeDataPerSound.envelope"></a>

#### envelope

```python
@envelope.setter
def envelope(value: float) -> None
```

<a id="unreal.SoundWaveEnvelopeDataPerSound.playback_time"></a>

#### playback_time

```python
@property
def playback_time() -> float
```

(float):  [Read-Write] The current playback time of this sound wave

<a id="unreal.SoundWaveEnvelopeDataPerSound.playback_time"></a>

#### playback_time

```python
@playback_time.setter
def playback_time(value: float) -> None
```

<a id="unreal.SoundWaveEnvelopeDataPerSound.sound_wave"></a>

#### sound_wave

```python
@property
def sound_wave() -> SoundWave
```

(SoundWave):  [Read-Write] The sound wave this envelope data is associated with

<a id="unreal.SoundWaveEnvelopeDataPerSound.sound_wave"></a>

#### sound_wave

```python
@sound_wave.setter
def sound_wave(value: SoundWave) -> None
```

<a id="unreal.SoundWaveCuePoint"></a>