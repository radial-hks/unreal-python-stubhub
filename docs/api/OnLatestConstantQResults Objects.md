## OnLatestConstantQResults Objects

```python
class OnLatestConstantQResults(MulticastDelegateBase)
```

Delegate to receive only the most recent overall ConstantQ result per channel. If bDownmixToMono setting is true, results will be in channel index 0.

Args:
    channel_index (int32): 
    latest_constant_q_results (ConstantQResults):

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQ.h

<a id="unreal.OnLatestConstantQResults.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnLatestOverallLoudnessResults"></a>