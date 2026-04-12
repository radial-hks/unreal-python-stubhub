## GameplayEventData Objects

```python
class GameplayEventData(StructBase)
```

Metadata for a tag-based Gameplay Event, that can activate other abilities or run ability-specific logic

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context_handle`` (GameplayEffectContextHandle):  [Read-Write] Polymorphic context information
- ``event_magnitude`` (float):  [Read-Write] The magnitude of the triggering event
- ``event_tag`` (GameplayTag):  [Read-Write] Tag of the event that triggered this
- ``instigator`` (Actor):  [Read-Write] The instigator of the event
- ``instigator_tags`` (GameplayTagContainer):  [Read-Write] Tags that the instigator has
- ``optional_object`` (Object):  [Read-Write] An optional ability-specific object to be passed though the event
- ``optional_object2`` (Object):  [Read-Write] A second optional ability-specific object to be passed though the event
- ``target`` (Actor):  [Read-Write] The target of the event
- ``target_data`` (GameplayAbilityTargetDataHandle):  [Read-Write] The polymorphic target information for the event
- ``target_tags`` (GameplayTagContainer):  [Read-Write] Tags that the target has

<a id="unreal.GameplayEventData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(event_tag: GameplayTag = ["None"],
             instigator: Actor = None,
             target: Actor = None,
             optional_object: Object = None,
             optional_object2: Object = None,
             context_handle: GameplayEffectContextHandle = [],
             instigator_tags: GameplayTagContainer = [[]],
             target_tags: GameplayTagContainer = [[]],
             event_magnitude: float = 0.000000,
             target_data: GameplayAbilityTargetDataHandle = []) -> None
```

<a id="unreal.GameplayEventData.event_tag"></a>

#### event\_tag

```python
@property
def event_tag() -> GameplayTag
```

(GameplayTag):  [Read-Write] Tag of the event that triggered this

<a id="unreal.GameplayEventData.event_tag"></a>

#### event\_tag

```python
@event_tag.setter
def event_tag(value: GameplayTag) -> None
```

<a id="unreal.GameplayEventData.instigator"></a>

#### instigator

```python
@property
def instigator() -> Actor
```

(Actor):  [Read-Write] The instigator of the event

<a id="unreal.GameplayEventData.instigator"></a>

#### instigator

```python
@instigator.setter
def instigator(value: Actor) -> None
```

<a id="unreal.GameplayEventData.target"></a>

#### target

```python
@property
def target() -> Actor
```

(Actor):  [Read-Write] The target of the event

<a id="unreal.GameplayEventData.target"></a>

#### target

```python
@target.setter
def target(value: Actor) -> None
```

<a id="unreal.GameplayEventData.optional_object"></a>

#### optional\_object

```python
@property
def optional_object() -> Object
```

(Object):  [Read-Write] An optional ability-specific object to be passed though the event

<a id="unreal.GameplayEventData.optional_object"></a>

#### optional\_object

```python
@optional_object.setter
def optional_object(value: Object) -> None
```

<a id="unreal.GameplayEventData.optional_object2"></a>

#### optional\_object2

```python
@property
def optional_object2() -> Object
```

(Object):  [Read-Write] A second optional ability-specific object to be passed though the event

<a id="unreal.GameplayEventData.optional_object2"></a>

#### optional\_object2

```python
@optional_object2.setter
def optional_object2(value: Object) -> None
```

<a id="unreal.GameplayEventData.context_handle"></a>

#### context\_handle

```python
@property
def context_handle() -> GameplayEffectContextHandle
```

(GameplayEffectContextHandle):  [Read-Write] Polymorphic context information

<a id="unreal.GameplayEventData.context_handle"></a>

#### context\_handle

```python
@context_handle.setter
def context_handle(value: GameplayEffectContextHandle) -> None
```

<a id="unreal.GameplayEventData.instigator_tags"></a>

#### instigator\_tags

```python
@property
def instigator_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] Tags that the instigator has

<a id="unreal.GameplayEventData.instigator_tags"></a>

#### instigator\_tags

```python
@instigator_tags.setter
def instigator_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.GameplayEventData.target_tags"></a>

#### target\_tags

```python
@property
def target_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] Tags that the target has

<a id="unreal.GameplayEventData.target_tags"></a>

#### target\_tags

```python
@target_tags.setter
def target_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.GameplayEventData.event_magnitude"></a>

#### event\_magnitude

```python
@property
def event_magnitude() -> float
```

(float):  [Read-Write] The magnitude of the triggering event

<a id="unreal.GameplayEventData.event_magnitude"></a>

#### event\_magnitude

```python
@event_magnitude.setter
def event_magnitude(value: float) -> None
```

<a id="unreal.GameplayEventData.target_data"></a>

#### target\_data

```python
@property
def target_data() -> GameplayAbilityTargetDataHandle
```

(GameplayAbilityTargetDataHandle):  [Read-Write] The polymorphic target information for the event

<a id="unreal.GameplayEventData.target_data"></a>

#### target\_data

```python
@target_data.setter
def target_data(value: GameplayAbilityTargetDataHandle) -> None
```

<a id="unreal.GameplayAbilityTargetDataHandle"></a>