## AvaTaperModifier Objects

```python
class AvaTaperModifier(AvaGeometryBaseModifier)
```

Ava Taper Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaTaperModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amount`` (float):  [Read-Write]
- ``extent`` (AvaTaperExtent):  [Read-Write]
- ``interpolation_type`` (AvaTaperInterpolationType):  [Read-Write]
- ``lower_extent`` (float):  [Read-Write] 100%: shape bottom.
  0%: shape top.
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``offset`` (Vector2D):  [Read-Write]
- ``reference_frame`` (AvaTaperReferenceFrame):  [Read-Write]
- ``resolution`` (int32):  [Read-Write] The number of vertical control points used to apply the taper. If the modifier is in a stack with Subdivide modifiers, taper will use the max value between Resolution and the total subdivision cuts.
- ``upper_extent`` (float):  [Read-Write] 100%: shape top.
  0%: shape bottom.

<a id="unreal.AvaTaperModifier.set_upper_extent"></a>

#### set_upper_extent

```python
def set_upper_extent(upper_extent: float) -> None
```

x.set_upper_extent(upper_extent) -> None
Set Upper Extent

Args:
    upper_extent (float):

<a id="unreal.AvaTaperModifier.set_resolution"></a>

#### set_resolution

```python
def set_resolution(resolution: int) -> None
```

x.set_resolution(resolution) -> None
Set Resolution

Args:
    resolution (int32):

<a id="unreal.AvaTaperModifier.set_reference_frame"></a>

#### set_reference_frame

```python
def set_reference_frame(reference_frame: AvaTaperReferenceFrame) -> None
```

x.set_reference_frame(reference_frame) -> None
Set Reference Frame

Args:
    reference_frame (AvaTaperReferenceFrame):

<a id="unreal.AvaTaperModifier.set_offset"></a>

#### set_offset

```python
def set_offset(offset: Vector2D) -> None
```

x.set_offset(offset) -> None
Set Offset

Args:
    offset (Vector2D):

<a id="unreal.AvaTaperModifier.set_lower_extent"></a>

#### set_lower_extent

```python
def set_lower_extent(lower_extent: float) -> None
```

x.set_lower_extent(lower_extent) -> None
Set Lower Extent

Args:
    lower_extent (float):

<a id="unreal.AvaTaperModifier.set_interpolation_type"></a>

#### set_interpolation_type

```python
def set_interpolation_type(
        interpolation_type: AvaTaperInterpolationType) -> None
```

x.set_interpolation_type(interpolation_type) -> None
Set Interpolation Type

Args:
    interpolation_type (AvaTaperInterpolationType):

<a id="unreal.AvaTaperModifier.set_extent"></a>

#### set_extent

```python
def set_extent(extent: AvaTaperExtent) -> None
```

x.set_extent(extent) -> None
Set Extent

Args:
    extent (AvaTaperExtent):

<a id="unreal.AvaTaperModifier.set_amount"></a>

#### set_amount

```python
def set_amount(amount: float) -> None
```

x.set_amount(amount) -> None
Set Amount

Args:
    amount (float):

<a id="unreal.AvaTaperModifier.get_upper_extent"></a>

#### get_upper_extent

```python
def get_upper_extent() -> float
```

x.get_upper_extent() -> float
Get Upper Extent

Returns:
    float:

<a id="unreal.AvaTaperModifier.get_resolution"></a>

#### get_resolution

```python
def get_resolution() -> int
```

x.get_resolution() -> int32
Get Resolution

Returns:
    int32:

<a id="unreal.AvaTaperModifier.get_reference_frame"></a>

#### get_reference_frame

```python
def get_reference_frame() -> AvaTaperReferenceFrame
```

x.get_reference_frame() -> AvaTaperReferenceFrame
Get Reference Frame

Returns:
    AvaTaperReferenceFrame:

<a id="unreal.AvaTaperModifier.get_offset"></a>

#### get_offset

```python
def get_offset() -> Vector2D
```

x.get_offset() -> Vector2D
Get Offset

Returns:
    Vector2D:

<a id="unreal.AvaTaperModifier.get_lower_extent"></a>

#### get_lower_extent

```python
def get_lower_extent() -> float
```

x.get_lower_extent() -> float
Get Lower Extent

Returns:
    float:

<a id="unreal.AvaTaperModifier.get_interpolation_type"></a>

#### get_interpolation_type

```python
def get_interpolation_type() -> AvaTaperInterpolationType
```

x.get_interpolation_type() -> AvaTaperInterpolationType
Get Interpolation Type

Returns:
    AvaTaperInterpolationType:

<a id="unreal.AvaTaperModifier.get_extent"></a>

#### get_extent

```python
def get_extent() -> AvaTaperExtent
```

x.get_extent() -> AvaTaperExtent
Get Extent

Returns:
    AvaTaperExtent:

<a id="unreal.AvaTaperModifier.get_amount"></a>

#### get_amount

```python
def get_amount() -> float
```

x.get_amount() -> float
Get Amount

Returns:
    float:

<a id="unreal.AvaTranslucentPriorityModifier"></a>