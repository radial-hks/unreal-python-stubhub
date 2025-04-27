## RigVMFunction_MathBoxGetVolume Objects

```python
class RigVMFunction_MathBoxGetVolume(RigVMFunction_MathBoxBase)
```

Returns the volume of a given box

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``volume`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetVolume.__init__"></a>

#### __init__

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             volume: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetVolume.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetVolume.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetVolume.volume"></a>

#### volume

```python
@property
def volume() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathColorBase"></a>