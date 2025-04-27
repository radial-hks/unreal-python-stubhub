## RigVMFunction_MathBoxIsValid Objects

```python
class RigVMFunction_MathBoxIsValid(RigVMFunction_MathBoxBase)
```

Returns true if the box has any content / is valid

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxIsValid.__init__"></a>

#### __init__

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             valid: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathBoxIsValid.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxIsValid.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxIsValid.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxGetCenter"></a>