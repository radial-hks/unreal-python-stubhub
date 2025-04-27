## RigVMFunction_MathFloatRemap Objects

```python
class RigVMFunction_MathFloatRemap(RigVMFunction_MathFloatBase)
```

Remaps the given value from a source range to a target range.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamp`` (bool):  [Read-Write] If set to true the result is clamped to the target range
- ``result`` (float):  [Read-Write]
- ``source_maximum`` (float):  [Read-Write]
- ``source_minimum`` (float):  [Read-Write]
- ``target_maximum`` (float):  [Read-Write]
- ``target_minimum`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatRemap.__init__"></a>

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

<a id="unreal.RigVMFunction_MathFloatRemap.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatRemap.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatRemap.source_minimum"></a>

#### source_minimum

```python
@property
def source_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatRemap.source_minimum"></a>

#### source_minimum

```python
@source_minimum.setter
def source_minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatRemap.source_maximum"></a>

#### source_maximum

```python
@property
def source_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatRemap.source_maximum"></a>

#### source_maximum

```python
@source_maximum.setter
def source_maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatRemap.target_minimum"></a>

#### target_minimum

```python
@property
def target_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatRemap.target_minimum"></a>

#### target_minimum

```python
@target_minimum.setter
def target_minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatRemap.target_maximum"></a>

#### target_maximum

```python
@property
def target_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatRemap.target_maximum"></a>

#### target_maximum

```python
@target_maximum.setter
def target_maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatRemap.clamp"></a>

#### clamp

```python
@property
def clamp() -> bool
```

(bool):  [Read-Write] If set to true the result is clamped to the target range

<a id="unreal.RigVMFunction_MathFloatRemap.clamp"></a>

#### clamp

```python
@clamp.setter
def clamp(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathFloatRemap.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathFloatRemap"></a>