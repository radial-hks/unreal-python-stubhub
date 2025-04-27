## CEClonerRangeExtension Objects

```python
class CEClonerRangeExtension(CEClonerExtensionBase)
```

Extension dealing with range options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerRangeExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``range_enabled`` (bool):  [Read-Write] Use random range transforms for each clones
- ``range_mirrored`` (bool):  [Read-Write] Mirrors offset and rotation values
- ``range_offset_max`` (Vector):  [Read-Write]
- ``range_offset_min`` (Vector):  [Read-Write]
- ``range_rotation_max`` (Rotator):  [Read-Write]
- ``range_rotation_min`` (Rotator):  [Read-Write]
- ``range_scale_max`` (Vector):  [Read-Write]
- ``range_scale_min`` (Vector):  [Read-Write]
- ``range_scale_uniform`` (bool):  [Read-Write]
- ``range_scale_uniform_max`` (float):  [Read-Write]
- ``range_scale_uniform_min`` (float):  [Read-Write]

<a id="unreal.CEClonerRangeExtension.set_range_scale_uniform_min"></a>

#### set_range_scale_uniform_min

```python
def set_range_scale_uniform_min(range_scale_uniform_min: float) -> None
```

x.set_range_scale_uniform_min(range_scale_uniform_min) -> None
Set Range Scale Uniform Min

Args:
    range_scale_uniform_min (float):

<a id="unreal.CEClonerRangeExtension.set_range_scale_uniform_max"></a>

#### set_range_scale_uniform_max

```python
def set_range_scale_uniform_max(range_scale_uniform_max: float) -> None
```

x.set_range_scale_uniform_max(range_scale_uniform_max) -> None
Set Range Scale Uniform Max

Args:
    range_scale_uniform_max (float):

<a id="unreal.CEClonerRangeExtension.set_range_scale_uniform"></a>

#### set_range_scale_uniform

```python
def set_range_scale_uniform(range_scale_uniform: bool) -> None
```

x.set_range_scale_uniform(range_scale_uniform) -> None
Set Range Scale Uniform

Args:
    range_scale_uniform (bool):

<a id="unreal.CEClonerRangeExtension.set_range_scale_min"></a>

#### set_range_scale_min

```python
def set_range_scale_min(range_scale_min: Vector) -> None
```

x.set_range_scale_min(range_scale_min) -> None
Set Range Scale Min

Args:
    range_scale_min (Vector):

<a id="unreal.CEClonerRangeExtension.set_range_scale_max"></a>

#### set_range_scale_max

```python
def set_range_scale_max(range_scale_max: Vector) -> None
```

x.set_range_scale_max(range_scale_max) -> None
Set Range Scale Max

Args:
    range_scale_max (Vector):

<a id="unreal.CEClonerRangeExtension.set_range_rotation_min"></a>

#### set_range_rotation_min

```python
def set_range_rotation_min(range_rotation_min: Rotator) -> None
```

x.set_range_rotation_min(range_rotation_min) -> None
Set Range Rotation Min

Args:
    range_rotation_min (Rotator):

<a id="unreal.CEClonerRangeExtension.set_range_rotation_max"></a>

#### set_range_rotation_max

```python
def set_range_rotation_max(range_rotation_max: Rotator) -> None
```

x.set_range_rotation_max(range_rotation_max) -> None
Set Range Rotation Max

Args:
    range_rotation_max (Rotator):

<a id="unreal.CEClonerRangeExtension.set_range_offset_min"></a>

#### set_range_offset_min

```python
def set_range_offset_min(range_offset_min: Vector) -> None
```

x.set_range_offset_min(range_offset_min) -> None
Set Range Offset Min

Args:
    range_offset_min (Vector):

<a id="unreal.CEClonerRangeExtension.set_range_offset_max"></a>

#### set_range_offset_max

```python
def set_range_offset_max(range_offset_max: Vector) -> None
```

x.set_range_offset_max(range_offset_max) -> None
Set Range Offset Max

Args:
    range_offset_max (Vector):

<a id="unreal.CEClonerRangeExtension.set_range_mirrored"></a>

#### set_range_mirrored

```python
def set_range_mirrored(mirrored: bool) -> None
```

x.set_range_mirrored(mirrored) -> None
Set Range Mirrored

Args:
    mirrored (bool):

<a id="unreal.CEClonerRangeExtension.set_range_enabled"></a>

#### set_range_enabled

```python
def set_range_enabled(range_enabled: bool) -> None
```

x.set_range_enabled(range_enabled) -> None
Set Range Enabled

Args:
    range_enabled (bool):

<a id="unreal.CEClonerRangeExtension.get_range_scale_uniform_min"></a>

#### get_range_scale_uniform_min

```python
def get_range_scale_uniform_min() -> float
```

x.get_range_scale_uniform_min() -> float
Get Range Scale Uniform Min

Returns:
    float:

<a id="unreal.CEClonerRangeExtension.get_range_scale_uniform_max"></a>

#### get_range_scale_uniform_max

```python
def get_range_scale_uniform_max() -> float
```

x.get_range_scale_uniform_max() -> float
Get Range Scale Uniform Max

Returns:
    float:

<a id="unreal.CEClonerRangeExtension.get_range_scale_uniform"></a>

#### get_range_scale_uniform

```python
def get_range_scale_uniform() -> bool
```

x.get_range_scale_uniform() -> bool
Get Range Scale Uniform

Returns:
    bool:

<a id="unreal.CEClonerRangeExtension.get_range_scale_min"></a>

#### get_range_scale_min

```python
def get_range_scale_min() -> Vector
```

x.get_range_scale_min() -> Vector
Get Range Scale Min

Returns:
    Vector:

<a id="unreal.CEClonerRangeExtension.get_range_scale_max"></a>

#### get_range_scale_max

```python
def get_range_scale_max() -> Vector
```

x.get_range_scale_max() -> Vector
Get Range Scale Max

Returns:
    Vector:

<a id="unreal.CEClonerRangeExtension.get_range_rotation_min"></a>

#### get_range_rotation_min

```python
def get_range_rotation_min() -> Rotator
```

x.get_range_rotation_min() -> Rotator
Get Range Rotation Min

Returns:
    Rotator:

<a id="unreal.CEClonerRangeExtension.get_range_rotation_max"></a>

#### get_range_rotation_max

```python
def get_range_rotation_max() -> Rotator
```

x.get_range_rotation_max() -> Rotator
Get Range Rotation Max

Returns:
    Rotator:

<a id="unreal.CEClonerRangeExtension.get_range_offset_min"></a>

#### get_range_offset_min

```python
def get_range_offset_min() -> Vector
```

x.get_range_offset_min() -> Vector
Get Range Offset Min

Returns:
    Vector:

<a id="unreal.CEClonerRangeExtension.get_range_offset_max"></a>

#### get_range_offset_max

```python
def get_range_offset_max() -> Vector
```

x.get_range_offset_max() -> Vector
Get Range Offset Max

Returns:
    Vector:

<a id="unreal.CEClonerRangeExtension.get_range_mirrored"></a>

#### get_range_mirrored

```python
def get_range_mirrored() -> bool
```

x.get_range_mirrored() -> bool
Get Range Mirrored

Returns:
    bool:

<a id="unreal.CEClonerRangeExtension.get_range_enabled"></a>

#### get_range_enabled

```python
def get_range_enabled() -> bool
```

x.get_range_enabled() -> bool
Get Range Enabled

Returns:
    bool:

<a id="unreal.CEClonerSphereRandomLayout"></a>