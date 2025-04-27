## RigVMFunction_MathBoxFromArray Objects

```python
class RigVMFunction_MathBoxFromArray(RigVMFunction_MathBoxBase)
```

Returns bounding box of the given array of positions

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``array`` (Array[Vector]):  [Read-Write]
- ``box`` (Box):  [Read-Write]
- ``center`` (Vector):  [Read-Write]
- ``maximum`` (Vector):  [Read-Write]
- ``minimum`` (Vector):  [Read-Write]
- ``size`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxFromArray.__init__"></a>

#### __init__

```python
def __init__(array: Array[Vector] = [],
             box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             minimum: Vector = [0.000000, 0.000000, 0.000000],
             maximum: Vector = [0.000000, 0.000000, 0.000000],
             center: Vector = [0.000000, 0.000000, 0.000000],
             size: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathBoxFromArray.array"></a>

#### array

```python
@property
def array() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxFromArray.array"></a>

#### array

```python
@array.setter
def array(value: Array[Vector]) -> None
```

<a id="unreal.RigVMFunction_MathBoxFromArray.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxFromArray.minimum"></a>

#### minimum

```python
@property
def minimum() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxFromArray.maximum"></a>

#### maximum

```python
@property
def maximum() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxFromArray.center"></a>

#### center

```python
@property
def center() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxFromArray.size"></a>

#### size

```python
@property
def size() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxIsValid"></a>