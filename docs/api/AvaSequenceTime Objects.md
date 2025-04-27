## AvaSequenceTime Objects

```python
class AvaSequenceTime(StructBase)
```

Ava Sequence Time

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequenceShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame`` (int32):  [Read-Write]
- ``has_time_constraint`` (bool):  [Read-Write]
- ``mark_label`` (str):  [Read-Write]
- ``seconds`` (double):  [Read-Write]
- ``sub_frame`` (double):  [Read-Write]
- ``time_type`` (AvaSequenceTimeType):  [Read-Write]

<a id="unreal.AvaSequenceTime.__init__"></a>

#### __init__

```python
def __init__(time_type: AvaSequenceTimeType = 0,
             frame: int = 0,
             sub_frame: float = 0.000000,
             seconds: float = 0.000000,
             mark_label: str = "",
             has_time_constraint: bool = False) -> None
```

<a id="unreal.AvaSequenceTime.time_type"></a>

#### time_type

```python
@property
def time_type() -> AvaSequenceTimeType
```

(AvaSequenceTimeType):  [Read-Write]

<a id="unreal.AvaSequenceTime.time_type"></a>

#### time_type

```python
@time_type.setter
def time_type(value: AvaSequenceTimeType) -> None
```

<a id="unreal.AvaSequenceTime.frame"></a>

#### frame

```python
@property
def frame() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaSequenceTime.frame"></a>

#### frame

```python
@frame.setter
def frame(value: int) -> None
```

<a id="unreal.AvaSequenceTime.sub_frame"></a>

#### sub_frame

```python
@property
def sub_frame() -> float
```

(double):  [Read-Write]

<a id="unreal.AvaSequenceTime.sub_frame"></a>

#### sub_frame

```python
@sub_frame.setter
def sub_frame(value: float) -> None
```

<a id="unreal.AvaSequenceTime.seconds"></a>

#### seconds

```python
@property
def seconds() -> float
```

(double):  [Read-Write]

<a id="unreal.AvaSequenceTime.seconds"></a>

#### seconds

```python
@seconds.setter
def seconds(value: float) -> None
```

<a id="unreal.AvaSequenceTime.mark_label"></a>

#### mark_label

```python
@property
def mark_label() -> str
```

(str):  [Read-Write]

<a id="unreal.AvaSequenceTime.mark_label"></a>

#### mark_label

```python
@mark_label.setter
def mark_label(value: str) -> None
```

<a id="unreal.AvaSequenceTime.has_time_constraint"></a>

#### has_time_constraint

```python
@property
def has_time_constraint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaSequenceTime.has_time_constraint"></a>

#### has_time_constraint

```python
@has_time_constraint.setter
def has_time_constraint(value: bool) -> None
```

<a id="unreal.AvaSequencePlayAdvancedSettings"></a>