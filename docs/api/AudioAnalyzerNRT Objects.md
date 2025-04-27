## AudioAnalyzerNRT Objects

```python
class AudioAnalyzerNRT(AudioAnalyzerAssetBase)
```

UAudioAnalyzerNRT

UAudioAnalyzerNRT applies an analyzer to a sound using specific settings, stores the
results and exposes them via blueprints.

Subclasses of UAudioAnalyzerNRT must implement GetAnalyzerNRTFactoryName() to associate
the UAudioAnalyzerNRT with an IAudioAnalyzerNRTFactory implementation.

To support blueprint access, subclasses can implement UFUNCTIONs to expose the data
returned by GetResult().

**C++ Source:**

- **Module**: AudioAnalyzer
- **File**: AudioAnalyzerNRT.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_in_seconds`` (float):  [Read-Write] The duration of the analyzed audio in seconds.
- ``sound`` (SoundWave):  [Read-Write] The USoundWave which is analyzed.

<a id="unreal.AudioAnalyzerNRT.sound"></a>

#### sound

```python
@property
def sound() -> SoundWave
```

(SoundWave):  [Read-Only] The USoundWave which is analyzed.

<a id="unreal.AudioAnalyzerNRT.duration_in_seconds"></a>

#### duration_in_seconds

```python
@property
def duration_in_seconds() -> float
```

(float):  [Read-Only] The duration of the analyzed audio in seconds.

<a id="unreal.AudioSynesthesiaSettings"></a>