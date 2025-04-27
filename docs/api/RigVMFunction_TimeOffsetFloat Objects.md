## RigVMFunction_TimeOffsetFloat Objects

```python
class RigVMFunction_TimeOffsetFloat(RigVMFunction_SimBase)
```

Records a value over time and can access the value from the past

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_TimeOffset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_size`` (int32):  [Read-Only] The sampling precision of the buffer. The higher the more precise - the more memory usage.
- ``result`` (float):  [Read-Write]
- ``seconds_ago`` (float):  [Read-Write] Seconds of time in the past you want to query the value for
- ``time_range`` (float):  [Read-Only] The maximum time required for offsetting in seconds.
- ``value`` (float):  [Read-Write] The value to record

<a id="unreal.RigVMFunction_TimeOffsetFloat.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             seconds_ago: float = 0.000000,
             buffer_size: int = 0,
             time_range: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_TimeOffsetFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The value to record

<a id="unreal.RigVMFunction_TimeOffsetFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_TimeOffsetFloat.seconds_ago"></a>

#### seconds_ago

```python
@property
def seconds_ago() -> float
```

(float):  [Read-Write] Seconds of time in the past you want to query the value for

<a id="unreal.RigVMFunction_TimeOffsetFloat.seconds_ago"></a>

#### seconds_ago

```python
@seconds_ago.setter
def seconds_ago(value: float) -> None
```

<a id="unreal.RigVMFunction_TimeOffsetFloat.buffer_size"></a>

#### buffer_size

```python
@property
def buffer_size() -> int
```

(int32):  [Read-Only] The sampling precision of the buffer. The higher the more precise - the more memory usage.

<a id="unreal.RigVMFunction_TimeOffsetFloat.time_range"></a>

#### time_range

```python
@property
def time_range() -> float
```

(float):  [Read-Only] The maximum time required for offsetting in seconds.

<a id="unreal.RigVMFunction_TimeOffsetFloat.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_TimeOffsetFloat"></a>