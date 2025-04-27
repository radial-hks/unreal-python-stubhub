## BroadphaseSettings Objects

```python
class BroadphaseSettings(StructBase)
```

Settings pertaining to which PhysX broadphase to use, and settings for MBP if that is the chosen broadphase type

**C++ Source:**

- **Module**: Engine
- **File**: WorldSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mbp_bounds`` (Box):  [Read-Write] Total bounds for MBP, must cover the game world or collisions are disabled for out of bounds actors
- ``mbp_num_subdivs`` (uint32):  [Read-Write] Number of times to subdivide the MBP bounds, final number of regions is MBPNumSubdivs^2
- ``mbp_outer_bounds`` (Box):  [Read-Write] Total bounds for MBP, should cover absolute maximum bounds of the game world where physics is required
- ``use_mbp_on_client`` (bool):  [Read-Write] Whether to use MBP (Multi Broadphase Pruning
- ``use_mbp_on_server`` (bool):  [Read-Write]
- ``use_mbp_outer_bounds`` (bool):  [Read-Write] Whether to have MBP grid over concentrated inner bounds with loose outer bounds

<a id="unreal.BroadphaseSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.TimecodeCustomAttributeNameSettings"></a>