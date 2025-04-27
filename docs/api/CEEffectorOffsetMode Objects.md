## CEEffectorOffsetMode Objects

```python
class CEEffectorOffsetMode(CEEffectorModeBase)
```

CEEffector Offset Mode

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorOffsetMode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``offset`` (Vector):  [Read-Write] Offset applied on affected clones
- ``rotation`` (Rotator):  [Read-Write] Rotation applied on affected clones
- ``scale`` (Vector):  [Read-Write] Scale applied on affected clones

<a id="unreal.CEEffectorOffsetMode.set_scale"></a>

#### set_scale

```python
def set_scale(scale: Vector) -> None
```

x.set_scale(scale) -> None
Set Scale

Args:
    scale (Vector):

<a id="unreal.CEEffectorOffsetMode.set_rotation"></a>

#### set_rotation

```python
def set_rotation(rotation: Rotator) -> None
```

x.set_rotation(rotation) -> None
Set Rotation

Args:
    rotation (Rotator):

<a id="unreal.CEEffectorOffsetMode.set_offset"></a>

#### set_offset

```python
def set_offset(offset: Vector) -> None
```

x.set_offset(offset) -> None
Set Offset

Args:
    offset (Vector):

<a id="unreal.CEEffectorOffsetMode.get_scale"></a>

#### get_scale

```python
def get_scale() -> Vector
```

x.get_scale() -> Vector
Get Scale

Returns:
    Vector:

<a id="unreal.CEEffectorOffsetMode.get_rotation"></a>

#### get_rotation

```python
def get_rotation() -> Rotator
```

x.get_rotation() -> Rotator
Get Rotation

Returns:
    Rotator:

<a id="unreal.CEEffectorOffsetMode.get_offset"></a>

#### get_offset

```python
def get_offset() -> Vector
```

x.get_offset() -> Vector
Get Offset

Returns:
    Vector:

<a id="unreal.CEEffectorPlaneType"></a>