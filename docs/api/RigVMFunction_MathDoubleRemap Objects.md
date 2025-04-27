## RigVMFunction_MathDoubleRemap Objects

```python
class RigVMFunction_MathDoubleRemap(RigVMFunction_MathDoubleBase)
```

Remaps the given value from a source range to a target range.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathDouble.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamp`` (bool):  [Read-Write] If set to true the result is clamped to the target range
- ``result`` (double):  [Read-Write]
- ``source_maximum`` (double):  [Read-Write]
- ``source_minimum`` (double):  [Read-Write]
- ``target_maximum`` (double):  [Read-Write]
- ``target_minimum`` (double):  [Read-Write]
- ``value`` (double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleRemap.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             source_minimum: float = 0.000000,
             source_maximum: float = 0.000000,
             target_minimum: float = 0.000000,
             target_maximum: float = 0.000000,
             clamp: bool = False,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.value"></a>

#### value

```python
@property
def value() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleRemap.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.source_minimum"></a>

#### source_minimum

```python
@property
def source_minimum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleRemap.source_minimum"></a>

#### source_minimum

```python
@source_minimum.setter
def source_minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.source_maximum"></a>

#### source_maximum

```python
@property
def source_maximum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleRemap.source_maximum"></a>

#### source_maximum

```python
@source_maximum.setter
def source_maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.target_minimum"></a>

#### target_minimum

```python
@property
def target_minimum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleRemap.target_minimum"></a>

#### target_minimum

```python
@target_minimum.setter
def target_minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.target_maximum"></a>

#### target_maximum

```python
@property
def target_maximum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleRemap.target_maximum"></a>

#### target_maximum

```python
@target_maximum.setter
def target_maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.clamp"></a>

#### clamp

```python
@property
def clamp() -> bool
```

(bool):  [Read-Write] If set to true the result is clamped to the target range

<a id="unreal.RigVMFunction_MathDoubleRemap.clamp"></a>

#### clamp

```python
@clamp.setter
def clamp(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathDoubleRemap.result"></a>

#### result

```python
@property
def result() -> float
```

(double):  [Read-Only]

<a id="unreal.RigUnit_MathDoubleRemap"></a>