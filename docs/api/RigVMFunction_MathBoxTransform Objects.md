## RigVMFunction_MathBoxTransform Objects

```python
class RigVMFunction_MathBoxTransform(RigVMFunction_MathBoxBase)
```

Transforms the box by a given transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``result`` (Box):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxTransform.__init__"></a>

#### __init__

```python
def __init__(
    box: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
                False],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    result: Box = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.RigVMFunction_MathBoxTransform.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxTransform.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathBoxTransform.result"></a>

#### result

```python
@property
def result() -> Box
```

(Box):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxGetDistance"></a>