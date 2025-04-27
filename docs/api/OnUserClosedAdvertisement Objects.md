## OnUserClosedAdvertisement Objects

```python
class OnUserClosedAdvertisement(DelegateBase)
```

Delegate called when user closes an ad (after clicking on banner). Base class already handles
pausing, so a delegate is only needed if you need extra handling.  If you set it to a PC or other actor
function, make sure to set it back when switching levels.

**C++ Source:**

- **Module**: Engine
- **File**: InGameAdManager.h

<a id="unreal.OnUserClosedAdvertisement.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnUserInputDeviceConnectionChange"></a>