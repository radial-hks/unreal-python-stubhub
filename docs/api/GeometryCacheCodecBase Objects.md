## GeometryCacheCodecBase Objects

```python
class GeometryCacheCodecBase(Object)
```

Interface for assets/objects that can own UserData *

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCache
- **File**: GeometryCacheCodecBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``topology_ranges`` (Array[int32]):  [Read-Only] Frames at which the topology of the decoded frames changes sorted in increasing order
  this allows fast topology queries between arbitrary frames.
  each codec has to fill this

<a id="unreal.DisplayClusterConfigurationScene"></a>