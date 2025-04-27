## AITestSpawnInfoBase Objects

```python
class AITestSpawnInfoBase(StructBase)
```

FAITestSpawnInfoBase

Base struct defining where & when to spawn. Used within a FAITestSpawnSetBase class.

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalAITest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``number_to_spawn`` (int32):  [Read-Write]
- ``pre_spawn_delay`` (float):  [Read-Write] delay before attempting first spawn
- ``spawn_delay`` (float):  [Read-Write] delay between consecutive spawn attempts
- ``spawn_location`` (Actor):  [Read-Write] Where should AI be spawned

<a id="unreal.AITestSpawnInfoBase.__init__"></a>

#### __init__

```python
def __init__(spawn_location: Actor = None,
             number_to_spawn: int = 0,
             spawn_delay: float = 0.000000,
             pre_spawn_delay: float = 0.000000) -> None
```

<a id="unreal.AITestSpawnInfoBase.spawn_location"></a>

#### spawn_location

```python
@property
def spawn_location() -> Actor
```

(Actor):  [Read-Write] Where should AI be spawned

<a id="unreal.AITestSpawnInfoBase.spawn_location"></a>

#### spawn_location

```python
@spawn_location.setter
def spawn_location(value: Actor) -> None
```

<a id="unreal.AITestSpawnInfoBase.number_to_spawn"></a>

#### number_to_spawn

```python
@property
def number_to_spawn() -> int
```

(int32):  [Read-Write]

<a id="unreal.AITestSpawnInfoBase.number_to_spawn"></a>

#### number_to_spawn

```python
@number_to_spawn.setter
def number_to_spawn(value: int) -> None
```

<a id="unreal.AITestSpawnInfoBase.spawn_delay"></a>

#### spawn_delay

```python
@property
def spawn_delay() -> float
```

(float):  [Read-Write] delay between consecutive spawn attempts

<a id="unreal.AITestSpawnInfoBase.spawn_delay"></a>

#### spawn_delay

```python
@spawn_delay.setter
def spawn_delay(value: float) -> None
```

<a id="unreal.AITestSpawnInfoBase.pre_spawn_delay"></a>

#### pre_spawn_delay

```python
@property
def pre_spawn_delay() -> float
```

(float):  [Read-Write] delay before attempting first spawn

<a id="unreal.AITestSpawnInfoBase.pre_spawn_delay"></a>

#### pre_spawn_delay

```python
@pre_spawn_delay.setter
def pre_spawn_delay(value: float) -> None
```

<a id="unreal.AITestSpawnInfo"></a>