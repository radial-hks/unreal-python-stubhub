## RigVMFunction_MathColorLerp Objects

```python
class RigVMFunction_MathColorLerp(RigVMFunction_MathColorBase)
```

Linearly interpolates between A and B using the ratio T

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathColor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (LinearColor):  [Read-Write]
- ``b`` (LinearColor):  [Read-Write]
- ``result`` (LinearColor):  [Read-Write]
- ``t`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorLerp.__init__"></a>

#### __init__

```python
def __init__(
        a: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        b: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        t: float = 0.000000,
        result: LinearColor = [0.000000, 0.000000, 0.000000,
                               0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathColorLerp.a"></a>

#### a

```python
@property
def a() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorLerp.a"></a>

#### a

```python
@a.setter
def a(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_MathColorLerp.b"></a>

#### b

```python
@property
def b() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorLerp.b"></a>

#### b

```python
@b.setter
def b(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_MathColorLerp.t"></a>

#### t

```python
@property
def t() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorLerp.t"></a>

#### t

```python
@t.setter
def t(value: float) -> None
```

<a id="unreal.RigVMFunction_MathColorLerp.result"></a>

#### result

```python
@property
def result() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigUnit_MathColorLerp"></a>