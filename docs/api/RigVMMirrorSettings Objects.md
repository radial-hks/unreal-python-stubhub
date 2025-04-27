## RigVMMirrorSettings Objects

```python
class RigVMMirrorSettings(StructBase)
```

Rig VMMirror Settings

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMMathLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis_to_flip`` (AxisType):  [Read-Write] the axis to flip for rotations
- ``mirror_axis`` (AxisType):  [Read-Write] the axis to mirror against
- ``replace_string`` (str):  [Read-Write] the string to replace the search occurrences with
- ``search_string`` (str):  [Read-Write] the string to search for

<a id="unreal.RigVMMirrorSettings.__init__"></a>

#### __init__

```python
def __init__(mirror_axis: AxisType = AxisType.NONE,
             axis_to_flip: AxisType = AxisType.NONE,
             search_string: str = "",
             replace_string: str = "") -> None
```

<a id="unreal.RigVMMirrorSettings.mirror_axis"></a>

#### mirror_axis

```python
@property
def mirror_axis() -> AxisType
```

(AxisType):  [Read-Write] the axis to mirror against

<a id="unreal.RigVMMirrorSettings.mirror_axis"></a>

#### mirror_axis

```python
@mirror_axis.setter
def mirror_axis(value: AxisType) -> None
```

<a id="unreal.RigVMMirrorSettings.axis_to_flip"></a>

#### axis_to_flip

```python
@property
def axis_to_flip() -> AxisType
```

(AxisType):  [Read-Write] the axis to flip for rotations

<a id="unreal.RigVMMirrorSettings.axis_to_flip"></a>

#### axis_to_flip

```python
@axis_to_flip.setter
def axis_to_flip(value: AxisType) -> None
```

<a id="unreal.RigVMMirrorSettings.search_string"></a>

#### search_string

```python
@property
def search_string() -> str
```

(str):  [Read-Write] the string to search for

<a id="unreal.RigVMMirrorSettings.search_string"></a>

#### search_string

```python
@search_string.setter
def search_string(value: str) -> None
```

<a id="unreal.RigVMMirrorSettings.replace_string"></a>

#### replace_string

```python
@property
def replace_string() -> str
```

(str):  [Read-Write] the string to replace the search occurrences with

<a id="unreal.RigVMMirrorSettings.replace_string"></a>

#### replace_string

```python
@replace_string.setter
def replace_string(value: str) -> None
```

<a id="unreal.RigMirrorSettings"></a>