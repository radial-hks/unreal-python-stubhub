## OnQueueSubtitles Objects

```python
class OnQueueSubtitles(DelegateBase)
```

Called when subtitles are sent to the SubtitleManager.  Set this delegate if you want to hijack the subtitles for other purposes

Args:
    subtitles (Array[SubtitleCue]): 
    cue_duration (float):

**C++ Source:**

- **Module**: Engine
- **File**: AudioComponent.h

<a id="unreal.OnQueueSubtitles.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnSubmixEnvelope"></a>