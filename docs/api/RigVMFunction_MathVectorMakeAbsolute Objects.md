## RigVMFunction_MathVectorMakeAbsolute Objects

```python
class RigVMFunction_MathVectorMakeAbsolute(RigVMFunction_MathVectorBase)
```

Returns the absolute global vector within a parent's vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Vector):  [Read-Write]
- ``local`` (Vector):  [Read-Write]
- ``parent`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorMakeAbsolute.__init__"></a>

#### __init__

```python
def __init__(local: Vector = [0.000000, 0.000000, 0.000000],
             parent: Vector = [0.000000, 0.000000, 0.000000],
             global_: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorMakeAbsolute.local"></a>

#### local

```python
@property
def local() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorMakeAbsolute.local"></a>

#### local

```python
@local.setter
def local(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorMakeAbsolute.parent"></a>

#### parent

```python
@property
def parent() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorMakeAbsolute.parent"></a>

#### parent

```python
@parent.setter
def parent(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorMakeAbsolute.global_"></a>

#### global_

```python
@property
def global_() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorMakeAbsolute"></a>