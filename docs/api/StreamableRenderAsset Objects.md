## StreamableRenderAsset Objects

```python
class StreamableRenderAsset(Object)
```

Streamable Render Asset

**C++ Source:**

- **Module**: Engine
- **File**: StreamableRenderAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``never_stream`` (bool):  [Read-Write]
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.

<a id="unreal.StreamableRenderAsset.num_cinematic_mip_levels"></a>

#### num_cinematic_mip_levels

```python
@property
def num_cinematic_mip_levels() -> int
```

(int32):  [Read-Write] Number of mip-levels to use for cinematic quality.

<a id="unreal.StreamableRenderAsset.num_cinematic_mip_levels"></a>

#### num_cinematic_mip_levels

```python
@num_cinematic_mip_levels.setter
def num_cinematic_mip_levels(value: int) -> None
```

<a id="unreal.StreamableRenderAsset.never_stream"></a>

#### never_stream

```python
@property
def never_stream() -> bool
```

(bool):  [Read-Write]

<a id="unreal.StreamableRenderAsset.never_stream"></a>

#### never_stream

```python
@never_stream.setter
def never_stream(value: bool) -> None
```

<a id="unreal.StreamableRenderAsset.global_force_mip_levels_to_be_resident"></a>

#### global_force_mip_levels_to_be_resident

```python
@property
def global_force_mip_levels_to_be_resident() -> bool
```

(bool):  [Read-Only] Global and serialized version of ForceMiplevelsToBeResident.

<a id="unreal.StreamableRenderAsset.set_force_mip_levels_to_be_resident"></a>

#### set_force_mip_levels_to_be_resident

```python
def set_force_mip_levels_to_be_resident(seconds: float,
                                        cinematic_lod_group_mask: int = 0
                                        ) -> None
```

x.set_force_mip_levels_to_be_resident(seconds, cinematic_lod_group_mask=0) -> None
Tells the streaming system that it should force all mip-levels to be resident for a number of seconds.

Args:
    seconds (float): Duration in seconds
    cinematic_lod_group_mask (int32):

<a id="unreal.Texture"></a>