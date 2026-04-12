## SmartObjectRequestFilter Objects

```python
class SmartObjectRequestFilter(StructBase)
```

Struct that can be used to filter results of a smart object request when trying to find or claim a smart object

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activity_requirements`` (GameplayTagQuery):  [Read-Write] Only return slots whose activity tags are matching this query.
- ``behavior_definition_classes`` (Array[type(Class)]):  [Read-Write] If set, will filter out any SmartObject that uses different BehaviorDefinition classes.
- ``claim_priority`` (SmartObjectClaimPriority):  [Read-Write] The user's claim priority. The search will contain already claimed slots at lower priority.
- ``should_evaluate_conditions`` (bool):  [Read-Write] If true, will evaluate the slot and object conditions, otherwise will skip them.
- ``should_include_claimed_slots`` (bool):  [Read-Write] If true, this search will contain claimed slots.
- ``should_include_disabled_slots`` (bool):  [Read-Write] If true, this search will contain disabled slots.
- ``user_tags`` (GameplayTagContainer):  [Read-Write] Gameplay tags of the Actor or Entity requesting the Smart Object slot.

<a id="unreal.SmartObjectRequestFilter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(user_tags: GameplayTagContainer = [[]],
             claim_priority: SmartObjectClaimPriority = 0,
             activity_requirements: GameplayTagQuery = [],
             behavior_definition_classes: Array[Class] = [],
             should_evaluate_conditions: bool = False,
             should_include_claimed_slots: bool = False,
             should_include_disabled_slots: bool = False) -> None
```

<a id="unreal.SmartObjectRequestFilter.user_tags"></a>

#### user\_tags

```python
@property
def user_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] Gameplay tags of the Actor or Entity requesting the Smart Object slot.

<a id="unreal.SmartObjectRequestFilter.user_tags"></a>

#### user\_tags

```python
@user_tags.setter
def user_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.SmartObjectRequestFilter.claim_priority"></a>

#### claim\_priority

```python
@property
def claim_priority() -> SmartObjectClaimPriority
```

(SmartObjectClaimPriority):  [Read-Write] The user's claim priority. The search will contain already claimed slots at lower priority.

<a id="unreal.SmartObjectRequestFilter.claim_priority"></a>

#### claim\_priority

```python
@claim_priority.setter
def claim_priority(value: SmartObjectClaimPriority) -> None
```

<a id="unreal.SmartObjectRequestFilter.activity_requirements"></a>

#### activity\_requirements

```python
@property
def activity_requirements() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write] Only return slots whose activity tags are matching this query.

<a id="unreal.SmartObjectRequestFilter.activity_requirements"></a>

#### activity\_requirements

```python
@activity_requirements.setter
def activity_requirements(value: GameplayTagQuery) -> None
```

<a id="unreal.SmartObjectRequestFilter.behavior_definition_classes"></a>

#### behavior\_definition\_classes

```python
@property
def behavior_definition_classes() -> Array[Class]
```

(Array[type(Class)]):  [Read-Write] If set, will filter out any SmartObject that uses different BehaviorDefinition classes.

<a id="unreal.SmartObjectRequestFilter.behavior_definition_classes"></a>

#### behavior\_definition\_classes

```python
@behavior_definition_classes.setter
def behavior_definition_classes(value: Array[Class]) -> None
```

<a id="unreal.SmartObjectRequestFilter.should_evaluate_conditions"></a>

#### should\_evaluate\_conditions

```python
@property
def should_evaluate_conditions() -> bool
```

(bool):  [Read-Write] If true, will evaluate the slot and object conditions, otherwise will skip them.

<a id="unreal.SmartObjectRequestFilter.should_evaluate_conditions"></a>

#### should\_evaluate\_conditions

```python
@should_evaluate_conditions.setter
def should_evaluate_conditions(value: bool) -> None
```

<a id="unreal.SmartObjectRequestFilter.should_include_claimed_slots"></a>

#### should\_include\_claimed\_slots

```python
@property
def should_include_claimed_slots() -> bool
```

(bool):  [Read-Write] If true, this search will contain claimed slots.

<a id="unreal.SmartObjectRequestFilter.should_include_claimed_slots"></a>

#### should\_include\_claimed\_slots

```python
@should_include_claimed_slots.setter
def should_include_claimed_slots(value: bool) -> None
```

<a id="unreal.SmartObjectRequestFilter.should_include_disabled_slots"></a>

#### should\_include\_disabled\_slots

```python
@property
def should_include_disabled_slots() -> bool
```

(bool):  [Read-Write] If true, this search will contain disabled slots.

<a id="unreal.SmartObjectRequestFilter.should_include_disabled_slots"></a>

#### should\_include\_disabled\_slots

```python
@should_include_disabled_slots.setter
def should_include_disabled_slots(value: bool) -> None
```

<a id="unreal.SmartObjectRequest"></a>