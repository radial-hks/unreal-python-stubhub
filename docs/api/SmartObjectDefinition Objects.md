## SmartObjectDefinition Objects

```python
class SmartObjectDefinition(DataAsset)
```

SmartObject definition asset. Contains sharable information that can be used by multiple SmartObject instances at runtime.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activity_tags`` (GameplayTagContainer):  [Read-Write] Tags identifying this Smart Object's use case. Can be used while looking for objects supporting given activity
- ``activity_tags_merging_policy`` (SmartObjectTagMergingPolicy):  [Read-Write] Indicates how Tags from slots and parent object are combined to be evaluated by a TagQuery from a find request.
- ``default_behavior_definitions`` (Array[SmartObjectBehaviorDefinition]):  [Read-Write] List of behavior definitions of different types provided to SO's user if the slot does not provide one.
- ``definition_data`` (Array[SmartObjectDefinitionDataProxy]):  [Read-Write] Custom definition data items (struct inheriting from SmartObjectDefinitionData) for the whole Smart Object.
- ``object_tag_filter`` (GameplayTagQuery):  [Read-Write]
  deprecated: Use FWorldCondition_SmartObjectActorTagQuery or FSmartObjectWorldConditionObjectTagQuery in Preconditions instead.
- ``parameters`` (InstancedPropertyBag):  [Read-Write] Parameters for the SmartObject definition
- ``preconditions`` (WorldConditionQueryDefinition):  [Read-Write] Preconditions that must pass for the object to be found/used.
- ``slots`` (Array[SmartObjectSlotDefinition]):  [Read-Write] Where SmartObject's user needs to stay to be able to activate it. These
  will be used by AI to approach the object. Locations are relative to object's location.
- ``user_tag_filter`` (GameplayTagQuery):  [Read-Write] This object is available if user tags match this query; always available if query is empty.
- ``user_tags_filtering_policy`` (SmartObjectTagFilteringPolicy):  [Read-Write] Indicates how TagQueries from slots and parent object will be processed against User Tags from a find request.
- ``world_condition_schema_class`` (type(Class)):  [Read-Write]

<a id="unreal.SmartObjectDefinition.object_tag_filter"></a>

#### object\_tag\_filter

```python
@property
def object_tag_filter() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write]
deprecated: Use FWorldCondition_SmartObjectActorTagQuery or FSmartObjectWorldConditionObjectTagQuery in Preconditions instead.

<a id="unreal.SmartObjectDefinition.object_tag_filter"></a>

#### object\_tag\_filter

```python
@object_tag_filter.setter
def object_tag_filter(value: GameplayTagQuery) -> None
```

<a id="unreal.SmartObjectDefinition.set_user_tag_filter"></a>

#### set\_user\_tag\_filter

```python
def set_user_tag_filter(user_tag_filter: GameplayTagQuery) -> None
```

x.set_user_tag_filter(user_tag_filter) -> None
Sets the tag query to run on the user tags provided by a request to accept this definition

Args:
    user_tag_filter (GameplayTagQuery):

<a id="unreal.SmartObjectDefinition.k2_get_slots"></a>

#### k2\_get\_slots

```python
def k2_get_slots() -> Array[SmartObjectSlotDefinition]
```

x.k2_get_slots() -> Array[SmartObjectSlotDefinition]
K2 Get Slots

Returns:
    Array[SmartObjectSlotDefinition]:

<a id="unreal.SmartObjectDefinition.is_valid_slot_index"></a>

#### is\_valid\_slot\_index

```python
def is_valid_slot_index(slot_index: int) -> bool
```

x.is_valid_slot_index(slot_index) -> bool


Args:
    slot_index (int32): 

Returns:
    bool: True if specified slot index is valid.

<a id="unreal.SmartObjectDefinition.get_user_tags_filtering_policy"></a>

#### get\_user\_tags\_filtering\_policy

```python
def get_user_tags_filtering_policy() -> SmartObjectTagFilteringPolicy
```

x.get_user_tags_filtering_policy() -> SmartObjectTagFilteringPolicy
Returns the tag filtering policy that should be applied on User tags by this definition

Returns:
    SmartObjectTagFilteringPolicy:

<a id="unreal.SmartObjectDefinition.get_user_tag_filter"></a>

#### get\_user\_tag\_filter

```python
def get_user_tag_filter() -> GameplayTagQuery
```

x.get_user_tag_filter() -> GameplayTagQuery
Returns the tag query to run on the user tags provided by a request to accept this definition

Returns:
    GameplayTagQuery:

<a id="unreal.SmartObjectDefinition.get_slot_world_transform"></a>

#### get\_slot\_world\_transform

```python
def get_slot_world_transform(slot_index: int,
                             owner_transform: Transform) -> Transform
```

x.get_slot_world_transform(slot_index, owner_transform) -> Transform
Returns the transform (in world space) of the given slot index.
note: Method will ensure on invalid slot index.

Args:
    slot_index (int32): Index within the list of slots.
    owner_transform (Transform): Transform (in world space) of the slot owner.

Returns:
    Transform: Transform (in world space) of the slot associated to SlotIndex, or OwnerTransform if index is invalid.

<a id="unreal.SmartObjectDefinition.get_slot_activity_tags_by_index"></a>

#### get\_slot\_activity\_tags\_by\_index

```python
def get_slot_activity_tags_by_index(slot_index: int) -> GameplayTagContainer
```

x.get_slot_activity_tags_by_index(slot_index) -> GameplayTagContainer
Fills the provided GameplayTagContainer with the activity tags associated to the slot according to the tag merging policy.

Args:
    slot_index (int32): Index of the slot for which the tags are requested

Returns:
    GameplayTagContainer: 

    out_activity_tags (GameplayTagContainer): Tag container to fill with the activity tags associated to the slot

<a id="unreal.SmartObjectDefinition.get_mutable_slot"></a>

#### get\_mutable\_slot

```python
def get_mutable_slot(index: int) -> SmartObjectSlotDefinition
```

x.get_mutable_slot(index) -> SmartObjectSlotDefinition


Args:
    index (int32): 

Returns:
    SmartObjectSlotDefinition: mutable slot definition stored at a given index

<a id="unreal.SmartObjectDefinition.get_bounds"></a>

#### get\_bounds

```python
def get_bounds() -> Box
```

x.get_bounds() -> Box
Return bounds encapsulating all slots

Returns:
    Box:

<a id="unreal.SmartObjectDefinition.get_activity_tags"></a>

#### get\_activity\_tags

```python
def get_activity_tags() -> GameplayTagContainer
```

x.get_activity_tags() -> GameplayTagContainer
Returns the list of tags describing the activity associated to this definition

Returns:
    GameplayTagContainer:

<a id="unreal.SmartObjectPersistentCollection"></a>