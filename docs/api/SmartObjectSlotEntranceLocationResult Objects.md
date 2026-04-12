## SmartObjectSlotEntranceLocationResult Objects

```python
class SmartObjectSlotEntranceLocationResult(StructBase)
```

Validated result from FindEntranceLocationForSlot().

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entrance_handle`` (SmartObjectSlotEntranceHandle):  [Read-Only] Handle identifying the entrance that was found.
- ``is_valid`` (bool):  [Read-Only] True if the result has passed validation tests.
- ``location`` (Vector):  [Read-Only] The location to enter the slot.
- ``rotation`` (Rotator):  [Read-Only] The expected direction to enter the slot.
- ``tags`` (GameplayTagContainer):  [Read-Only] Gameplay tags associated with the entrance.

<a id="unreal.SmartObjectSlotEntranceLocationResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             tags: GameplayTagContainer = [[]],
             entrance_handle: SmartObjectSlotEntranceHandle = [[]],
             is_valid: bool = False) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationResult.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only] The location to enter the slot.

<a id="unreal.SmartObjectSlotEntranceLocationResult.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Only] The expected direction to enter the slot.

<a id="unreal.SmartObjectSlotEntranceLocationResult.tags"></a>

#### tags

```python
@property
def tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] Gameplay tags associated with the entrance.

<a id="unreal.SmartObjectSlotEntranceLocationResult.entrance_handle"></a>

#### entrance\_handle

```python
@property
def entrance_handle() -> SmartObjectSlotEntranceHandle
```

(SmartObjectSlotEntranceHandle):  [Read-Only] Handle identifying the entrance that was found.

<a id="unreal.SmartObjectSlotEntranceLocationResult.is_valid"></a>

#### is\_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Only] True if the result has passed validation tests.

<a id="unreal.SmartObjectSlotIndex"></a>