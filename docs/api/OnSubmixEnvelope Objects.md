## OnSubmixEnvelope Objects

```python
class OnSubmixEnvelope(MulticastDelegateBase)
```

Called when a new submix envelope value is generated on the given audio device id (different for multiple PIE). Array is an envelope value for each channel.

Args:
    envelope (Array[float]):

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmix.h

<a id="unreal.OnSubmixEnvelope.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnSubmixEnvelopeBP"></a>