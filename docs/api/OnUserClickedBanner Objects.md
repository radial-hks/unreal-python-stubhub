## OnUserClickedBanner Objects

```python
class OnUserClickedBanner(DelegateBase)
```

Delegate called when user clicks on an banner ad. Base class already handles pausing,
so a delegate is only needed if you need extra handling. If you set it to a PC or other actor
function, make sure to set it back when switching levels.

**C++ Source:**

- **Module**: Engine
- **File**: InGameAdManager.h

<a id="unreal.OnUserClickedBanner.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnUserClosedAdvertisement"></a>