## MirrorOptions Objects

```python
class MirrorOptions(StructBase)
```

FMirrorOptions

**C++ Source:**

- **Plugin**: MeshModelingToolsetExp
- **Module**: SkeletalMeshModifiers
- **File**: SkeletonModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``left_string`` (str):  [Read-Write]
- ``mirror_axis`` (AxisType):  [Read-Write]
- ``mirror_children`` (bool):  [Read-Write]
- ``mirror_rotation`` (bool):  [Read-Write]
- ``right_string`` (str):  [Read-Write]

<a id="unreal.MirrorOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mirror_axis: AxisType = AxisType.NONE,
             mirror_rotation: bool = False,
             left_string: str = "",
             right_string: str = "",
             mirror_children: bool = False) -> None
```

<a id="unreal.MirrorOptions.mirror_axis"></a>

#### mirror\_axis

```python
@property
def mirror_axis() -> AxisType
```

(AxisType):  [Read-Write]

<a id="unreal.MirrorOptions.mirror_axis"></a>

#### mirror\_axis

```python
@mirror_axis.setter
def mirror_axis(value: AxisType) -> None
```

<a id="unreal.MirrorOptions.mirror_rotation"></a>

#### mirror\_rotation

```python
@property
def mirror_rotation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MirrorOptions.mirror_rotation"></a>

#### mirror\_rotation

```python
@mirror_rotation.setter
def mirror_rotation(value: bool) -> None
```

<a id="unreal.MirrorOptions.left_string"></a>

#### left\_string

```python
@property
def left_string() -> str
```

(str):  [Read-Write]

<a id="unreal.MirrorOptions.left_string"></a>

#### left\_string

```python
@left_string.setter
def left_string(value: str) -> None
```

<a id="unreal.MirrorOptions.right_string"></a>

#### right\_string

```python
@property
def right_string() -> str
```

(str):  [Read-Write]

<a id="unreal.MirrorOptions.right_string"></a>

#### right\_string

```python
@right_string.setter
def right_string(value: str) -> None
```

<a id="unreal.MirrorOptions.mirror_children"></a>

#### mirror\_children

```python
@property
def mirror_children() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MirrorOptions.mirror_children"></a>

#### mirror\_children

```python
@mirror_children.setter
def mirror_children(value: bool) -> None
```

<a id="unreal.OrientOptions"></a>