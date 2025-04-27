## CEEffectorPushMode Objects

```python
class CEEffectorPushMode(CEEffectorModeBase)
```

CEEffector Push Mode

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorPushMode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``push_direction`` (CEClonerEffectorPushDirection):  [Read-Write] Relative direction computed for the push effect on each clone
- ``push_strength`` (Vector):  [Read-Write] Strength of the push effect

<a id="unreal.CEEffectorPushMode.set_push_strength"></a>

#### set_push_strength

```python
def set_push_strength(strength: Vector) -> None
```

x.set_push_strength(strength) -> None
Set Push Strength

Args:
    strength (Vector):

<a id="unreal.CEEffectorPushMode.set_push_direction"></a>

#### set_push_direction

```python
def set_push_direction(direction: CEClonerEffectorPushDirection) -> None
```

x.set_push_direction(direction) -> None
Set Push Direction

Args:
    direction (CEClonerEffectorPushDirection):

<a id="unreal.CEEffectorPushMode.get_push_strength"></a>

#### get_push_strength

```python
def get_push_strength() -> Vector
```

x.get_push_strength() -> Vector
Get Push Strength

Returns:
    Vector:

<a id="unreal.CEEffectorPushMode.get_push_direction"></a>

#### get_push_direction

```python
def get_push_direction() -> CEClonerEffectorPushDirection
```

x.get_push_direction() -> CEClonerEffectorPushDirection
Get Push Direction

Returns:
    CEClonerEffectorPushDirection:

<a id="unreal.CEEffectorRadialType"></a>