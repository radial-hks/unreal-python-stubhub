## CEClonerEmitterSpawnExtension Objects

```python
class CEClonerEmitterSpawnExtension(CEClonerExtensionBase)
```

Extension dealing with clones spawning options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerEmitterSpawnExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``spawn_behavior_mode`` (CEClonerSpawnBehaviorMode):  [Read-Write] How does spawn occurs
- ``spawn_loop_interval`` (float):  [Read-Write] Interval/Duration of spawn for clones
- ``spawn_loop_iterations`` (int32):  [Read-Write] Amount of spawn iterations for clones
- ``spawn_loop_mode`` (CEClonerSpawnLoopMode):  [Read-Write] How many times do we spawn clones
- ``spawn_rate`` (float):  [Read-Write] How many clones to spawn each seconds

<a id="unreal.CEClonerEmitterSpawnExtension.set_spawn_rate"></a>

#### set_spawn_rate

```python
def set_spawn_rate(rate: float) -> None
```

x.set_spawn_rate(rate) -> None
Set Spawn Rate

Args:
    rate (float):

<a id="unreal.CEClonerEmitterSpawnExtension.set_spawn_loop_mode"></a>

#### set_spawn_loop_mode

```python
def set_spawn_loop_mode(mode: CEClonerSpawnLoopMode) -> None
```

x.set_spawn_loop_mode(mode) -> None
Set Spawn Loop Mode

Args:
    mode (CEClonerSpawnLoopMode):

<a id="unreal.CEClonerEmitterSpawnExtension.set_spawn_loop_iterations"></a>

#### set_spawn_loop_iterations

```python
def set_spawn_loop_iterations(iterations: int) -> None
```

x.set_spawn_loop_iterations(iterations) -> None
Set Spawn Loop Iterations

Args:
    iterations (int32):

<a id="unreal.CEClonerEmitterSpawnExtension.set_spawn_loop_interval"></a>

#### set_spawn_loop_interval

```python
def set_spawn_loop_interval(interval: float) -> None
```

x.set_spawn_loop_interval(interval) -> None
Set Spawn Loop Interval

Args:
    interval (float):

<a id="unreal.CEClonerEmitterSpawnExtension.set_spawn_behavior_mode"></a>

#### set_spawn_behavior_mode

```python
def set_spawn_behavior_mode(mode: CEClonerSpawnBehaviorMode) -> None
```

x.set_spawn_behavior_mode(mode) -> None
Set Spawn Behavior Mode

Args:
    mode (CEClonerSpawnBehaviorMode):

<a id="unreal.CEClonerEmitterSpawnExtension.get_spawn_rate"></a>

#### get_spawn_rate

```python
def get_spawn_rate() -> float
```

x.get_spawn_rate() -> float
Get Spawn Rate

Returns:
    float:

<a id="unreal.CEClonerEmitterSpawnExtension.get_spawn_loop_mode"></a>

#### get_spawn_loop_mode

```python
def get_spawn_loop_mode() -> CEClonerSpawnLoopMode
```

x.get_spawn_loop_mode() -> CEClonerSpawnLoopMode
Get Spawn Loop Mode

Returns:
    CEClonerSpawnLoopMode:

<a id="unreal.CEClonerEmitterSpawnExtension.get_spawn_loop_iterations"></a>

#### get_spawn_loop_iterations

```python
def get_spawn_loop_iterations() -> int
```

x.get_spawn_loop_iterations() -> int32
Get Spawn Loop Iterations

Returns:
    int32:

<a id="unreal.CEClonerEmitterSpawnExtension.get_spawn_loop_interval"></a>

#### get_spawn_loop_interval

```python
def get_spawn_loop_interval() -> float
```

x.get_spawn_loop_interval() -> float
Get Spawn Loop Interval

Returns:
    float:

<a id="unreal.CEClonerEmitterSpawnExtension.get_spawn_behavior_mode"></a>

#### get_spawn_behavior_mode

```python
def get_spawn_behavior_mode() -> CEClonerSpawnBehaviorMode
```

x.get_spawn_behavior_mode() -> CEClonerSpawnBehaviorMode
Get Spawn Behavior Mode

Returns:
    CEClonerSpawnBehaviorMode:

<a id="unreal.CEClonerGridLayout"></a>