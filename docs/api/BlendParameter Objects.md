## BlendParameter Objects

```python
class BlendParameter(StructBase)
```

Blend Parameter

**C++ Source:**

- **Module**: Engine
- **File**: BlendSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (str):  [Read-Write]
- ``grid_num`` (int32):  [Read-Write] The number of grid divisions along this axis.
- ``max`` (float):  [Read-Write] Maximum value for this axis range.
- ``min`` (float):  [Read-Write] Minimum value for this axis range.
- ``snap_to_grid`` (bool):  [Read-Write] If true then samples will always be snapped to the grid on this axis when added, moved, or the axes are changed.
- ``wrap_input`` (bool):  [Read-Write] If true then the input can go outside the min/max range and the blend space is treated as being cyclic on this axis. If false then input parameters are clamped to the min/max values on this axis.

<a id="unreal.BlendParameter.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ExternalDataLayerUID"></a>