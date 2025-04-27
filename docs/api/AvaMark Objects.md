## AvaMark Objects

```python
class AvaMark(StructBase)
```

Ava Mark

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaMark.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (AvaMarkDirection):  [Read-Write]
- ``is_local_mark`` (bool):  [Read-Write] Whether Executing this Mark should affect the Local Sequence
  Set to True to only Execute Roles in the Owning Sequence
  Set to False to Affect Child Sequences of the Owning Sequence
- ``jump_label`` (str):  [Read-Write]
- ``label`` (str):  [Read-Only]
- ``limit_play_count`` (int32):  [Read-Write]
- ``limit_play_count_enabled`` (bool):  [Read-Write]
- ``pause_time`` (float):  [Read-Write]
- ``role`` (AvaMarkRole):  [Read-Write]
- ``search_direction`` (AvaMarkSearchDirection):  [Read-Write]

<a id="unreal.AvaMark.__init__"></a>

#### __init__

```python
def __init__(
    label: str = "",
    direction: AvaMarkDirection = AvaMarkDirection.BOTH,
    role: AvaMarkRole = AvaMarkRole.NONE,
    is_local_mark: bool = False,
    limit_play_count_enabled: bool = False,
    limit_play_count: int = 0,
    pause_time: float = 0.000000,
    jump_label: str = "",
    search_direction: AvaMarkSearchDirection = AvaMarkSearchDirection.ALL
) -> None
```

<a id="unreal.AvaMark.label"></a>

#### label

```python
@property
def label() -> str
```

(str):  [Read-Only]

<a id="unreal.AvaMark.direction"></a>

#### direction

```python
@property
def direction() -> AvaMarkDirection
```

(AvaMarkDirection):  [Read-Write]

<a id="unreal.AvaMark.direction"></a>

#### direction

```python
@direction.setter
def direction(value: AvaMarkDirection) -> None
```

<a id="unreal.AvaMark.role"></a>

#### role

```python
@property
def role() -> AvaMarkRole
```

(AvaMarkRole):  [Read-Write]

<a id="unreal.AvaMark.role"></a>

#### role

```python
@role.setter
def role(value: AvaMarkRole) -> None
```

<a id="unreal.AvaMark.is_local_mark"></a>

#### is_local_mark

```python
@property
def is_local_mark() -> bool
```

(bool):  [Read-Write] Whether Executing this Mark should affect the Local Sequence
Set to True to only Execute Roles in the Owning Sequence
Set to False to Affect Child Sequences of the Owning Sequence

<a id="unreal.AvaMark.is_local_mark"></a>

#### is_local_mark

```python
@is_local_mark.setter
def is_local_mark(value: bool) -> None
```

<a id="unreal.AvaMark.limit_play_count_enabled"></a>

#### limit_play_count_enabled

```python
@property
def limit_play_count_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaMark.limit_play_count_enabled"></a>

#### limit_play_count_enabled

```python
@limit_play_count_enabled.setter
def limit_play_count_enabled(value: bool) -> None
```

<a id="unreal.AvaMark.limit_play_count"></a>

#### limit_play_count

```python
@property
def limit_play_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaMark.limit_play_count"></a>

#### limit_play_count

```python
@limit_play_count.setter
def limit_play_count(value: int) -> None
```

<a id="unreal.AvaMark.pause_time"></a>

#### pause_time

```python
@property
def pause_time() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaMark.pause_time"></a>

#### pause_time

```python
@pause_time.setter
def pause_time(value: float) -> None
```

<a id="unreal.AvaMark.jump_label"></a>

#### jump_label

```python
@property
def jump_label() -> str
```

(str):  [Read-Write]

<a id="unreal.AvaMark.jump_label"></a>

#### jump_label

```python
@jump_label.setter
def jump_label(value: str) -> None
```

<a id="unreal.AvaMark.search_direction"></a>

#### search_direction

```python
@property
def search_direction() -> AvaMarkSearchDirection
```

(AvaMarkSearchDirection):  [Read-Write]

<a id="unreal.AvaMark.search_direction"></a>

#### search_direction

```python
@search_direction.setter
def search_direction(value: AvaMarkSearchDirection) -> None
```

<a id="unreal.AvaSequenceName"></a>