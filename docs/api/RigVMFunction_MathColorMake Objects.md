## RigVMFunction_MathColorMake Objects

```python
class RigVMFunction_MathColorMake(RigVMFunction_MathColorBase)
```

Makes a color from its components

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathColor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (float):  [Read-Write]
- ``b`` (float):  [Read-Write]
- ``g`` (float):  [Read-Write]
- ``r`` (float):  [Read-Write]
- ``result`` (LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorMake.__init__"></a>

#### __init__

```python
def __init__(
        r: float = 0.000000,
        g: float = 0.000000,
        b: float = 0.000000,
        a: float = 0.000000,
        result: LinearColor = [0.000000, 0.000000, 0.000000,
                               0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathColorMake.r"></a>

#### r

```python
@property
def r() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorMake.r"></a>

#### r

```python
@r.setter
def r(value: float) -> None
```

<a id="unreal.RigVMFunction_MathColorMake.g"></a>

#### g

```python
@property
def g() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorMake.g"></a>

#### g

```python
@g.setter
def g(value: float) -> None
```

<a id="unreal.RigVMFunction_MathColorMake.b"></a>

#### b

```python
@property
def b() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorMake.b"></a>

#### b

```python
@b.setter
def b(value: float) -> None
```

<a id="unreal.RigVMFunction_MathColorMake.a"></a>

#### a

```python
@property
def a() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorMake.a"></a>

#### a

```python
@a.setter
def a(value: float) -> None
```

<a id="unreal.RigVMFunction_MathColorMake.result"></a>

#### result

```python
@property
def result() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigUnit_MathColorMake"></a>