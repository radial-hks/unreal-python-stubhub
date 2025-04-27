## AITestSpawnSet Objects

```python
class AITestSpawnSet(AITestSpawnSetBase)
```

FAITestSpawnSet

Generic AI Test Spawn Set that is used in regular AFunctionalAITest tests.

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalAITest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``fallback_spawn_location`` (Actor):  [Read-Write] location used for spawning if spawn info doesn't define one
- ``name`` (Name):  [Read-Write] give the set a name to help identify it if need be
- ``spawn_info_container`` (Array[AITestSpawnInfo]):  [Read-Write] what to spawn

<a id="unreal.AITestSpawnSet.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             enabled: bool = False,
             fallback_spawn_location: Actor = None,
             spawn_info_container: Array[AITestSpawnInfo] = []) -> None
```

<a id="unreal.AITestSpawnSet.spawn_info_container"></a>

#### spawn_info_container

```python
@property
def spawn_info_container() -> Array[AITestSpawnInfo]
```

(Array[AITestSpawnInfo]):  [Read-Write] what to spawn

<a id="unreal.AITestSpawnSet.spawn_info_container"></a>

#### spawn_info_container

```python
@spawn_info_container.setter
def spawn_info_container(value: Array[AITestSpawnInfo]) -> None
```

<a id="unreal.TraceChannelTestBatchOptions"></a>