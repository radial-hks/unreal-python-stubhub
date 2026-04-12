## CachedAnimRelevancyData Objects

```python
class CachedAnimRelevancyData(StructBase)
```

Cached Anim Relevancy Data

**C++ Source:**

- **Module**: Engine
- **File**: CachedAnimData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``state_machine_name`` (Name):  [Read-Write] Name of StateMachine State is in
- ``state_name`` (Name):  [Read-Write] Name of State to Cache

<a id="unreal.CachedAnimRelevancyData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(state_machine_name: Name = "None",
             state_name: Name = "None") -> None
```

<a id="unreal.CachedAnimRelevancyData.state_machine_name"></a>

#### state\_machine\_name

```python
@property
def state_machine_name() -> Name
```

(Name):  [Read-Only] Name of StateMachine State is in

<a id="unreal.CachedAnimRelevancyData.state_name"></a>

#### state\_name

```python
@property
def state_name() -> Name
```

(Name):  [Read-Only] Name of State to Cache

<a id="unreal.CachedAnimTransitionData"></a>