## RigVMFunction_MathBoxMoveTo Objects

```python
class RigVMFunction_MathBoxMoveTo(RigVMFunction_MathBoxBase)
```

Moves the center of the box to a new location

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``center`` (Vector):  [Read-Write] the new center for the box
- ``result`` (Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxMoveTo.__init__"></a>

#### __init__

```python
def __init__(
    box: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
                False],
    center: Vector = [0.000000, 0.000000, 0.000000],
    result: Box = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.RigVMFunction_MathBoxMoveTo.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxMoveTo.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxMoveTo.center"></a>

#### center

```python
@property
def center() -> Vector
```

(Vector):  [Read-Write] the new center for the box

<a id="unreal.RigVMFunction_MathBoxMoveTo.center"></a>

#### center

```python
@center.setter
def center(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathBoxMoveTo.result"></a>

#### result

```python
@property
def result() -> Box
```

(Box):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxExpand"></a>