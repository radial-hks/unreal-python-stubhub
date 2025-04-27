## AudioAnalyzer Objects

```python
class AudioAnalyzer(Object)
```

UAudioAnalyzer

UAudioAnalyzer performs analysis on an audio bus using specific settings and exposes the results via blueprints.

Subclasses of UAudioAnalyzer must implement GetAnalyzerFactoryName() to associate
the UAudioAnalyzer asset with an IAudioAnalyzerFactory implementation.

To support blueprint access, subclasses can implement UFUNCTIONs to expose the data
returned by GetResult().

**C++ Source:**

- **Module**: AudioAnalyzer
- **File**: AudioAnalyzer.h

<a id="unreal.AudioAnalyzer.stop_analyzing"></a>

#### stop_analyzing

```python
def stop_analyzing(world_context_object: Object = None) -> None
```

x.stop_analyzing(world_context_object=None) -> None
Stops analyzing audio.

Args:
    world_context_object (Object):

<a id="unreal.AudioAnalyzer.start_analyzing"></a>

#### start_analyzing

```python
def start_analyzing(world_context_object: Object,
                    audio_bus_to_analyze: AudioBus) -> None
```

x.start_analyzing(world_context_object, audio_bus_to_analyze) -> None
Starts analyzing audio from the given audio bus. Optionally override the audio bus desired to analyze.

Args:
    world_context_object (Object): 
    audio_bus_to_analyze (AudioBus):

<a id="unreal.AudioAnalyzerNRTSettings"></a>