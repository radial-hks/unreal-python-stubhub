## MovementProperties Objects

```python
class MovementProperties(StructBase)
```

Movement capabilities, determining available movement options for Pawns and used by AI for reachability tests.

**C++ Source:**

- **Module**: Engine
- **File**: NavigationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_crouch`` (bool):  [Read-Write] If true, this Pawn is capable of crouching.
- ``can_fly`` (bool):  [Read-Write] If true, this Pawn is capable of flying.
- ``can_jump`` (bool):  [Read-Write] If true, this Pawn is capable of jumping.
- ``can_swim`` (bool):  [Read-Write] If true, this Pawn is capable of swimming or moving through fluid volumes.
- ``can_walk`` (bool):  [Read-Write] If true, this Pawn is capable of walking or moving on the ground.

<a id="unreal.MovementProperties.__init__"></a>

#### __init__

```python
def __init__(can_crouch: bool = False,
             can_jump: bool = False,
             can_walk: bool = False,
             can_swim: bool = False,
             can_fly: bool = False) -> None
```

<a id="unreal.MovementProperties.can_crouch"></a>

#### can_crouch

```python
@property
def can_crouch() -> bool
```

(bool):  [Read-Write] If true, this Pawn is capable of crouching.

<a id="unreal.MovementProperties.can_crouch"></a>

#### can_crouch

```python
@can_crouch.setter
def can_crouch(value: bool) -> None
```

<a id="unreal.MovementProperties.can_jump"></a>

#### can_jump

```python
@property
def can_jump() -> bool
```

(bool):  [Read-Write] If true, this Pawn is capable of jumping.

<a id="unreal.MovementProperties.can_jump"></a>

#### can_jump

```python
@can_jump.setter
def can_jump(value: bool) -> None
```

<a id="unreal.MovementProperties.can_walk"></a>

#### can_walk

```python
@property
def can_walk() -> bool
```

(bool):  [Read-Write] If true, this Pawn is capable of walking or moving on the ground.

<a id="unreal.MovementProperties.can_walk"></a>

#### can_walk

```python
@can_walk.setter
def can_walk(value: bool) -> None
```

<a id="unreal.MovementProperties.can_swim"></a>

#### can_swim

```python
@property
def can_swim() -> bool
```

(bool):  [Read-Write] If true, this Pawn is capable of swimming or moving through fluid volumes.

<a id="unreal.MovementProperties.can_swim"></a>

#### can_swim

```python
@can_swim.setter
def can_swim(value: bool) -> None
```

<a id="unreal.MovementProperties.can_fly"></a>

#### can_fly

```python
@property
def can_fly() -> bool
```

(bool):  [Read-Write] If true, this Pawn is capable of flying.

<a id="unreal.MovementProperties.can_fly"></a>

#### can_fly

```python
@can_fly.setter
def can_fly(value: bool) -> None
```

<a id="unreal.NavMovementProperties"></a>