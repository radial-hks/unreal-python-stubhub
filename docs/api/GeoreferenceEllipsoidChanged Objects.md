## GeoreferenceEllipsoidChanged Objects

```python
class GeoreferenceEllipsoidChanged(MulticastDelegateBase)
```

The event that triggers when a georeference's ellipsoid is changed.
This should be used for performing any necessary coordinate changes.
The parameters are (OldEllipsoid, NewEllipsoid).

Args:
    old_ellipsoid (CesiumEllipsoid): 
    new_ellipsoid (CesiumEllipsoid):

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumGeoreference.h

<a id="unreal.GeoreferenceEllipsoidChanged.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.GeoreferenceUpdated"></a>