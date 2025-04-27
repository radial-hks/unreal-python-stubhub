## RigVMFunction_MathBoxGetSize Objects

```python
class RigVMFunction_MathBoxGetSize(RigVMFunction_MathBoxBase)
```

Returns the size of a bounding box

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``extent`` (Vector):  [Read-Write] the half size of the box
- ``size`` (Vector):  [Read-Write] the overall size of the box

<a id="unreal.RigVMFunction_MathBoxGetSize.__init__"></a>

#### __init__

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             size: Vector = [0.000000, 0.000000, 0.000000],
             extent: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetSize.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetSize.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetSize.size"></a>

#### size

```python
@property
def size() -> Vector
```

(Vector):  [Read-Only] the overall size of the box

<a id="unreal.RigVMFunction_MathBoxGetSize.extent"></a>

#### extent

```python
@property
def extent() -> Vector
```

(Vector):  [Read-Only] the half size of the box

<a id="unreal.RigVMFunction_MathBoxShift"></a>