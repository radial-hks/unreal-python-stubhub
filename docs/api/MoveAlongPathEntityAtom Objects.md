## MoveAlongPathEntityAtom Objects

```python
class MoveAlongPathEntityAtom(EntityAtomBase)
```

Move Along Path Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: MoveAlongPathEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``loop`` (bool):  [Read-Write]
- ``moving_eid`` (int64):  [Read-Write]
- ``offset`` (MoveAlongOffset_Atom):  [Read-Write]
- ``path_eid`` (int64):  [Read-Write]
- ``path_update_points`` (Array[Vector]):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``state`` (str):  [Read-Write]
- ``time`` (float):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.moving_eid"></a>

#### moving\_eid

```python
@property
def moving_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.moving_eid"></a>

#### moving\_eid

```python
@moving_eid.setter
def moving_eid(value: int) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.path_eid"></a>

#### path\_eid

```python
@property
def path_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.path_eid"></a>

#### path\_eid

```python
@path_eid.setter
def path_eid(value: int) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.time"></a>

#### time

```python
@time.setter
def time(value: float) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.offset"></a>

#### offset

```python
@property
def offset() -> MoveAlongOffset_Atom
```

(MoveAlongOffset_Atom):  [Read-Only]

<a id="unreal.MoveAlongPathEntityAtom.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.MoveAlongPathEntityAtom.state"></a>

#### state

```python
@property
def state() -> str
```

(str):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.state"></a>

#### state

```python
@state.setter
def state(value: str) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.path_update_points"></a>

#### path\_update\_points

```python
@property
def path_update_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.MoveAlongPathEntityAtom.path_update_points"></a>

#### path\_update\_points

```python
@path_update_points.setter
def path_update_points(value: Array[Vector]) -> None
```

<a id="unreal.MoveAlongPathEntityAtom.set_time"></a>

#### set\_time

```python
def set_time(time: float) -> bool
```

x.set_time(time) -> bool
Set Time

Args:
    time (float): 

Returns:
    bool:

<a id="unreal.MoveAlongPathEntityAtom.set_path_eid"></a>

#### set\_path\_eid

```python
def set_path_eid(new_path_eid: int) -> bool
```

x.set_path_eid(new_path_eid) -> bool
Set Path Eid

Args:
    new_path_eid (int64): 

Returns:
    bool:

<a id="unreal.MoveAlongPathEntityAtom.set_moving_eid"></a>

#### set\_moving\_eid

```python
def set_moving_eid(new_moving_eid: int) -> bool
```

x.set_moving_eid(new_moving_eid) -> bool
Set Moving Eid

Args:
    new_moving_eid (int64): 

Returns:
    bool:

<a id="unreal.MoveAlongPathEntityAtom.setb_reverse"></a>

#### setb\_reverse

```python
def setb_reverse(inb_reverse: bool) -> bool
```

x.setb_reverse(inb_reverse) -> bool
Setb Reverse

Args:
    inb_reverse (bool): 

Returns:
    bool:

<a id="unreal.MoveAlongPathEntityAtom.setb_loop"></a>

#### setb\_loop

```python
def setb_loop(inb_loop: bool) -> bool
```

x.setb_loop(inb_loop) -> bool
Setb Loop

Args:
    inb_loop (bool): 

Returns:
    bool:

<a id="unreal.ParabolaEntityAtom"></a>