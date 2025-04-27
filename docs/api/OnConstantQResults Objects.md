## OnConstantQResults Objects

```python
class OnConstantQResults(MulticastDelegateBase)
```

Delegate to receive all ConstantQ results per channel (time-stamped in an array) since last delegate call. If bDownmixToMono setting is true, results will be in channel index 0.

Args:
    channel_index (int32): 
    constant_q_results (Array[ConstantQResults]):

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQ.h

<a id="unreal.OnConstantQResults.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnLatestConstantQResults"></a>