## RigVMFunction_MathVectorRemap Objects

```python
class RigVMFunction_MathVectorRemap(RigVMFunction_MathVectorBase)
```

Remaps the given value from a source range to a target range for each component

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamp`` (bool):  [Read-Write] If set to true the result is clamped to the target range
- ``result`` (Vector):  [Read-Write]
- ``source_maximum`` (Vector):  [Read-Write]
- ``source_minimum`` (Vector):  [Read-Write]
- ``target_maximum`` (Vector):  [Read-Write]
- ``target_minimum`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorRemap.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             source_minimum: Vector = [0.000000, 0.000000, 0.000000],
             source_maximum: Vector = [0.000000, 0.000000, 0.000000],
             target_minimum: Vector = [0.000000, 0.000000, 0.000000],
             target_maximum: Vector = [0.000000, 0.000000, 0.000000],
             clamp: bool = False,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorRemap.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.source_minimum"></a>

#### source_minimum

```python
@property
def source_minimum() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorRemap.source_minimum"></a>

#### source_minimum

```python
@source_minimum.setter
def source_minimum(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.source_maximum"></a>

#### source_maximum

```python
@property
def source_maximum() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorRemap.source_maximum"></a>

#### source_maximum

```python
@source_maximum.setter
def source_maximum(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.target_minimum"></a>

#### target_minimum

```python
@property
def target_minimum() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorRemap.target_minimum"></a>

#### target_minimum

```python
@target_minimum.setter
def target_minimum(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.target_maximum"></a>

#### target_maximum

```python
@property
def target_maximum() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorRemap.target_maximum"></a>

#### target_maximum

```python
@target_maximum.setter
def target_maximum(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.clamp"></a>

#### clamp

```python
@property
def clamp() -> bool
```

(bool):  [Read-Write] If set to true the result is clamped to the target range

<a id="unreal.RigVMFunction_MathVectorRemap.clamp"></a>

#### clamp

```python
@clamp.setter
def clamp(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathVectorRemap.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorRemap"></a>