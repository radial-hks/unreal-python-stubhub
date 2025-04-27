## AvaMask2DWriteModifier Objects

```python
class AvaMask2DWriteModifier(AvaMask2DBaseModifier)
```

Uses scene actors to create a mask texture and applies it to attached actors

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMask
- **File**: AvaMask2DWriteModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

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
- ``write_operation`` (GeometryMaskCompositeOperation):  [Read-Write] How to write to the chosen mask channel

<a id="unreal.AvaMask2DWriteModifier.write_operation"></a>

#### write_operation

```python
@property
def write_operation() -> GeometryMaskCompositeOperation
```

(GeometryMaskCompositeOperation):  [Read-Write] How to write to the chosen mask channel

<a id="unreal.AvaMask2DWriteModifier.write_operation"></a>

#### write_operation

```python
@write_operation.setter
def write_operation(value: GeometryMaskCompositeOperation) -> None
```

<a id="unreal.AvaMaskSettings"></a>