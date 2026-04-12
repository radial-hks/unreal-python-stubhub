## SmartObjectSlotDefinition Objects

```python
class SmartObjectSlotDefinition(StructBase)
```

Persistent and sharable definition of a smart object slot.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activity_tags`` (GameplayTagContainer):  [Read-Write] Tags identifying this slot's use case. Can be used while looking for slots supporting given activity.
  Depending on the tag filtering policy these tags can override the parent object's tags
  or be combined with them while applying filters from requests.
- ``behavior_definitions`` (Array[SmartObjectBehaviorDefinition]):  [Read-Write] All available definitions associated to this slot.
  This allows multiple frameworks to provide their specific behavior definition to the slot.
  Note that there should be only one definition of each type since the first one will be selected.
- ``debug_draw_color`` (Color):  [Read-Write]
- ``debug_draw_shape`` (SmartObjectSlotShape):  [Read-Write]
- ``debug_draw_size`` (float):  [Read-Write]
- ``definition_data`` (Array[SmartObjectDefinitionDataProxy]):  [Read-Write] Custom definition data items (struct inheriting from SmartObjecDefinitionData) that can be added to the slot definition and accessed through a FSmartObjectSlotView
- ``enabled`` (bool):  [Read-Write] Whether the slot is enable initially.
- ``id`` (Guid):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``offset`` (Vector3f):  [Read-Write] Offset relative to the parent object where the slot is located.
- ``rotation`` (Rotator3f):  [Read-Write] Rotation relative to the parent object.
- ``runtime_tags`` (GameplayTagContainer):  [Read-Write] Initial runtime tags.
- ``selection_preconditions`` (WorldConditionQueryDefinition):  [Read-Write] Preconditions that must pass for the slot to be selected.
- ``user_tag_filter`` (GameplayTagQuery):  [Read-Write] This slot is available only for users matching this query.

<a id="unreal.SmartObjectSlotDefinition.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        offset: Vector3f = [0.000000, 0.000000, 0.000000],
        rotation: Rotator3f = [0.000000, 0.000000, 0.000000],
        enabled: bool = False,
        user_tag_filter: GameplayTagQuery = [],
        activity_tags: GameplayTagContainer = [[]],
        runtime_tags: GameplayTagContainer = [[]],
        behavior_definitions: Array[SmartObjectBehaviorDefinition] = []
) -> None
```

<a id="unreal.SmartObjectSlotDefinition.offset"></a>

#### offset

```python
@property
def offset() -> Vector3f
```

(Vector3f):  [Read-Only] Offset relative to the parent object where the slot is located.

<a id="unreal.SmartObjectSlotDefinition.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator3f
```

(Rotator3f):  [Read-Only] Rotation relative to the parent object.

<a id="unreal.SmartObjectSlotDefinition.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only] Whether the slot is enable initially.

<a id="unreal.SmartObjectSlotDefinition.user_tag_filter"></a>

#### user\_tag\_filter

```python
@property
def user_tag_filter() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Only] This slot is available only for users matching this query.

<a id="unreal.SmartObjectSlotDefinition.activity_tags"></a>

#### activity\_tags

```python
@property
def activity_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] Tags identifying this slot's use case. Can be used while looking for slots supporting given activity.
Depending on the tag filtering policy these tags can override the parent object's tags
or be combined with them while applying filters from requests.

<a id="unreal.SmartObjectSlotDefinition.runtime_tags"></a>

#### runtime\_tags

```python
@property
def runtime_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] Initial runtime tags.

<a id="unreal.SmartObjectSlotDefinition.behavior_definitions"></a>

#### behavior\_definitions

```python
@property
def behavior_definitions() -> Array[SmartObjectBehaviorDefinition]
```

(Array[SmartObjectBehaviorDefinition]):  [Read-Only] All available definitions associated to this slot.
This allows multiple frameworks to provide their specific behavior definition to the slot.
Note that there should be only one definition of each type since the first one will be selected.

<a id="unreal.SmartObjectSlot"></a>