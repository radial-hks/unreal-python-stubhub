## AvaMask2DReadModifier Objects

```python
class AvaMask2DReadModifier(AvaMask2DBaseModifier)
```

Uses scene actors to create a mask texture and applies it to attached actors

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMask
- **File**: AvaMask2DReadModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_opacity`` (float):  [Read-Write] Base opacity/alpha to use in Read mode
- ``blur_strength`` (float):  [Read-Write]
- ``canvas_weak`` (GeometryMaskCanvas):  [Read-Write] Reference to the Canvas used
- ``channel`` (Name):  [Read-Write] Channel to read to or write from
- ``inner_feather_radius`` (int32):  [Read-Write]
- ``inverted`` (bool):  [Read-Write] Whether to apply the mask as inverted (visible becomes invisible and vice versa)
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``outer_feather_radius`` (int32):  [Read-Write]
- ``parent_channel`` (Name):  [Read-Only] Channel found when GetChannelFromParent is true
- ``use_blur`` (bool):  [Read-Write]
- ``use_feathering`` (bool):  [Read-Write]
- ``use_parent_channel`` (bool):  [Read-Write] Whether to get the channel from the parent (first one that specifies a mask channel)

<a id="unreal.AvaMask2DReadModifier.base_opacity"></a>

#### base_opacity

```python
@property
def base_opacity() -> float
```

(float):  [Read-Write] Base opacity/alpha to use in Read mode

<a id="unreal.AvaMask2DReadModifier.base_opacity"></a>

#### base_opacity

```python
@base_opacity.setter
def base_opacity(value: float) -> None
```

<a id="unreal.AvaMask2DWriteModifier"></a>