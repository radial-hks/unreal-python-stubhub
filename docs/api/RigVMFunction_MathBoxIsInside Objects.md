## RigVMFunction_MathBoxIsInside Objects

```python
class RigVMFunction_MathBoxIsInside(RigVMFunction_MathBoxBase)
```

Returns true if a point is inside a given box

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxIsInside.__init__"></a>

#### __init__

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             position: Vector = [0.000000, 0.000000, 0.000000],
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathBoxIsInside.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxIsInside.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxIsInside.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxIsInside.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxGetVolume"></a>