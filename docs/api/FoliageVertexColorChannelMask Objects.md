## FoliageVertexColorChannelMask Objects

```python
class FoliageVertexColorChannelMask(StructBase)
```

Foliage Vertex Color Channel Mask

**C++ Source:**

- **Module**: Foliage
- **File**: FoliageType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``invert_mask`` (bool):  [Read-Write] When unchecked, foliage instances will be placed only when the vertex color in the specified channel(s) is above the threshold amount.
  When checked, the vertex color must be less than the threshold amount
- ``mask_threshold`` (float):  [Read-Write] Specifies the threshold value above which the static mesh vertex color value must be, in order for foliage instances to be placed in a specific area
- ``use_mask`` (bool):  [Read-Write] When checked, foliage will be masked from this mesh using this color channel

<a id="unreal.FoliageVertexColorChannelMask.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.FoliageDensityFalloff"></a>