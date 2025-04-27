## RigVMFunction_MathBoxExpand Objects

```python
class RigVMFunction_MathBoxExpand(RigVMFunction_MathBoxBase)
```

Expands the size of the box by a given amount

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amount`` (Vector):  [Read-Write] the amount to grow / shrink the box by
- ``box`` (Box):  [Read-Write]
- ``result`` (Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxExpand.__init__"></a>

#### __init__

```python
def __init__(
    box: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
                False],
    amount: Vector = [0.000000, 0.000000, 0.000000],
    result: Box = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.RigVMFunction_MathBoxExpand.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxExpand.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxExpand.amount"></a>

#### amount

```python
@property
def amount() -> Vector
```

(Vector):  [Read-Write] the amount to grow / shrink the box by

<a id="unreal.RigVMFunction_MathBoxExpand.amount"></a>

#### amount

```python
@amount.setter
def amount(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathBoxExpand.result"></a>

#### result

```python
@property
def result() -> Box
```

(Box):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxTransform"></a>