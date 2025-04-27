## AITestSpawnSetBase Objects

```python
class AITestSpawnSetBase(StructBase)
```

FAITestSpawnSetBase

Base struct defining an AI Test Spawn Set that are used in AFunctionalAITestBase tests.

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalAITest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``fallback_spawn_location`` (Actor):  [Read-Write] location used for spawning if spawn info doesn't define one
- ``name`` (Name):  [Read-Write] give the set a name to help identify it if need be

<a id="unreal.AITestSpawnSetBase.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             enabled: bool = False,
             fallback_spawn_location: Actor = None) -> None
```

<a id="unreal.AITestSpawnSetBase.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] give the set a name to help identify it if need be

<a id="unreal.AITestSpawnSetBase.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AITestSpawnSetBase.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AITestSpawnSetBase.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.AITestSpawnSetBase.fallback_spawn_location"></a>

#### fallback_spawn_location

```python
@property
def fallback_spawn_location() -> Actor
```

(Actor):  [Read-Write] location used for spawning if spawn info doesn't define one

<a id="unreal.AITestSpawnSetBase.fallback_spawn_location"></a>

#### fallback_spawn_location

```python
@fallback_spawn_location.setter
def fallback_spawn_location(value: Actor) -> None
```

<a id="unreal.AITestSpawnSet"></a>