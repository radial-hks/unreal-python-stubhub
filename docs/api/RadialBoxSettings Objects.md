## RadialBoxSettings Objects

```python
class RadialBoxSettings(StructBase)
```

Radial Box Settings

**C++ Source:**

- **Module**: UMG
- **File**: RadialBoxSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle_between_items`` (float):  [Read-Write] Amount of Euler degrees that separate each item. Only used when bDistributeItemsEvenly is false
- ``distribute_items_evenly`` (bool):  [Read-Write] Distribute Items evenly in the whole circle. Checking this option ignores AngleBetweenItems
- ``sector_central_angle`` (float):  [Read-Write] If we need a section of a radial (for example half-a-radial) we can define a central angle < 360 (180 in case of half-a-radial). Used when bDistributeItemsEvenly is enabled.
- ``starting_angle`` (float):  [Read-Write] At what angle will we place the first element of the wheel?

<a id="unreal.RadialBoxSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SlateChildSize"></a>