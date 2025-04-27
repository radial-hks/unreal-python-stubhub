## CachedAnimAssetPlayerData Objects

```python
class CachedAnimAssetPlayerData(StructBase)
```

Cached Anim Asset Player Data

**C++ Source:**

- **Module**: Engine
- **File**: CachedAnimData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``state_machine_name`` (Name):  [Read-Write] Name of StateMachine State is in
- ``state_name`` (Name):  [Read-Write] Name of State to Cache

<a id="unreal.CachedAnimAssetPlayerData.__init__"></a>

#### __init__

```python
def __init__(state_machine_name: Name = "None",
             state_name: Name = "None") -> None
```

<a id="unreal.CachedAnimAssetPlayerData.state_machine_name"></a>

#### state_machine_name

```python
@property
def state_machine_name() -> Name
```

(Name):  [Read-Only] Name of StateMachine State is in

<a id="unreal.CachedAnimAssetPlayerData.state_name"></a>

#### state_name

```python
@property
def state_name() -> Name
```

(Name):  [Read-Only] Name of State to Cache

<a id="unreal.CachedAnimRelevancyData"></a>