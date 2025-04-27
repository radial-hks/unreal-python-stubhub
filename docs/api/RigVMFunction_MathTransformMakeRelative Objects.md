## RigVMFunction_MathTransformMakeRelative Objects

```python
class RigVMFunction_MathTransformMakeRelative(RigVMFunction_MathTransformBase)
```

Returns the relative local transform within a parent's transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Transform):  [Read-Write]
- ``local`` (Transform):  [Read-Write]
- ``parent`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMakeRelative.__init__"></a>

#### __init__

```python
def __init__(
    global_: Transform = [[0.000000, 0.000000, 0.000000],
                          [-0.000000, 0.000000, 0.000000],
                          [1.000000, 1.000000, 1.000000]],
    parent: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]],
    local: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformMakeRelative.global_"></a>

#### global_

```python
@property
def global_() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMakeRelative.global_"></a>

#### global_

```python
@global_.setter
def global_(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformMakeRelative.parent"></a>

#### parent

```python
@property
def parent() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMakeRelative.parent"></a>

#### parent

```python
@parent.setter
def parent(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformMakeRelative.local"></a>

#### local

```python
@property
def local() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformMakeRelative"></a>