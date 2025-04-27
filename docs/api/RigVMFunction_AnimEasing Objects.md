## RigVMFunction_AnimEasing Objects

```python
class RigVMFunction_AnimEasing(RigVMFunction_AnimBase)
```

Returns the eased version of the input value

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_AnimEasing.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (float):  [Read-Write]
- ``source_maximum`` (float):  [Read-Write]
- ``source_minimum`` (float):  [Read-Write]
- ``target_maximum`` (float):  [Read-Write]
- ``target_minimum`` (float):  [Read-Write]
- ``type`` (RigVMAnimEasingType):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
             source_minimum: float = 0.000000,
             source_maximum: float = 0.000000,
             target_minimum: float = 0.000000,
             target_maximum: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.type"></a>

#### type

```python
@property
def type() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.type"></a>

#### type

```python
@type.setter
def type(value: RigVMAnimEasingType) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.source_minimum"></a>

#### source_minimum

```python
@property
def source_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.source_minimum"></a>

#### source_minimum

```python
@source_minimum.setter
def source_minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.source_maximum"></a>

#### source_maximum

```python
@property
def source_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.source_maximum"></a>

#### source_maximum

```python
@source_maximum.setter
def source_maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.target_minimum"></a>

#### target_minimum

```python
@property
def target_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.target_minimum"></a>

#### target_minimum

```python
@target_minimum.setter
def target_minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.target_maximum"></a>

#### target_maximum

```python
@property
def target_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AnimEasing.target_maximum"></a>

#### target_maximum

```python
@target_maximum.setter
def target_maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_AnimEasing.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_AnimEasing"></a>