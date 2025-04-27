## RigVMFunction_MathBoxGetCenter Objects

```python
class RigVMFunction_MathBoxGetCenter(RigVMFunction_MathBoxBase)
```

Returns the center of a bounding box

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``center`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetCenter.__init__"></a>

#### __init__

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             center: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetCenter.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetCenter.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetCenter.center"></a>

#### center

```python
@property
def center() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxGetSize"></a>