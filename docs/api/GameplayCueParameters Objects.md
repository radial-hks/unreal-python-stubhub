## GameplayCueParameters Objects

```python
class GameplayCueParameters(StructBase)
```

Metadata about a gameplay cue execution

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ability_level`` (int32):  [Read-Write] If originating from an ability, this will be the level of that ability
- ``aggregated_source_tags`` (GameplayTagContainer):  [Read-Write] The aggregated source tags taken from the effect spec
- ``aggregated_target_tags`` (GameplayTagContainer):  [Read-Write] The aggregated target tags taken from the effect spec
- ``effect_causer`` (Actor):  [Read-Write] The physical actor that actually did the damage, can be a weapon or projectile
- ``effect_context`` (GameplayEffectContextHandle):  [Read-Write] Effect context, contains information about hit result, etc
- ``gameplay_effect_level`` (int32):  [Read-Write] If originating from a GameplayEffect, the level of that GameplayEffect
- ``instigator`` (Actor):  [Read-Write] Instigator actor, the actor that owns the ability system component
- ``location`` (Vector_NetQuantize10):  [Read-Write] Location cue took place at
- ``matched_tag_name`` (GameplayTag):  [Read-Write] The tag name that matched this specific gameplay cue handler
- ``normal`` (Vector_NetQuantizeNormal):  [Read-Write] Normal of impact that caused cue
- ``normalized_magnitude`` (float):  [Read-Write] Magnitude of source gameplay effect, normalzed from 0-1. Use this for "how strong is the gameplay effect" (0=min, 1=,max)
- ``original_tag`` (GameplayTag):  [Read-Write] The original tag of the gameplay cue
- ``physical_material`` (PhysicalMaterial):  [Read-Write] PhysMat of the hit, if there was a hit.
- ``raw_magnitude`` (float):  [Read-Write] Raw final magnitude of source gameplay effect. Use this is you need to display numbers or for other informational purposes.
- ``replicate_location_when_using_minimal_rep_proxy`` (bool):  [Read-Write] If we're using a minimal replication proxy, should we replicate location for this cue
- ``source_object`` (Object):  [Read-Write] Object this effect was created from, can be an actor or static object. Useful to bind an effect to a gameplay object
- ``target_attach_component`` (SceneComponent):  [Read-Write] Could be used to say "attach FX to this component always"

<a id="unreal.GameplayCueParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        normalized_magnitude: float = 0.000000,
        raw_magnitude: float = 0.000000,
        effect_context: GameplayEffectContextHandle = [],
        matched_tag_name: GameplayTag = ["None"],
        original_tag: GameplayTag = ["None"],
        aggregated_source_tags: GameplayTagContainer = [[]],
        aggregated_target_tags: GameplayTagContainer = [[]],
        location: Vector = [0.000000, 0.000000, 0.000000],
        normal: Vector = [0.000000, 0.000000, 0.000000],
        instigator: Actor = None,
        effect_causer: Actor = None,
        source_object: Object = None,
        physical_material: PhysicalMaterial = None,
        gameplay_effect_level: int = 1,
        ability_level: int = 1,
        target_attach_component: SceneComponent = None,
        replicate_location_when_using_minimal_rep_proxy: bool = False) -> None
```

<a id="unreal.GameplayCueParameters.normalized_magnitude"></a>

#### normalized\_magnitude

```python
@property
def normalized_magnitude() -> float
```

(float):  [Read-Write] Magnitude of source gameplay effect, normalzed from 0-1. Use this for "how strong is the gameplay effect" (0=min, 1=,max)

<a id="unreal.GameplayCueParameters.normalized_magnitude"></a>

#### normalized\_magnitude

```python
@normalized_magnitude.setter
def normalized_magnitude(value: float) -> None
```

<a id="unreal.GameplayCueParameters.raw_magnitude"></a>

#### raw\_magnitude

```python
@property
def raw_magnitude() -> float
```

(float):  [Read-Write] Raw final magnitude of source gameplay effect. Use this is you need to display numbers or for other informational purposes.

<a id="unreal.GameplayCueParameters.raw_magnitude"></a>

#### raw\_magnitude

```python
@raw_magnitude.setter
def raw_magnitude(value: float) -> None
```

<a id="unreal.GameplayCueParameters.effect_context"></a>

#### effect\_context

```python
@property
def effect_context() -> GameplayEffectContextHandle
```

(GameplayEffectContextHandle):  [Read-Write] Effect context, contains information about hit result, etc

<a id="unreal.GameplayCueParameters.effect_context"></a>

#### effect\_context

```python
@effect_context.setter
def effect_context(value: GameplayEffectContextHandle) -> None
```

<a id="unreal.GameplayCueParameters.matched_tag_name"></a>

#### matched\_tag\_name

```python
@property
def matched_tag_name() -> GameplayTag
```

(GameplayTag):  [Read-Write] The tag name that matched this specific gameplay cue handler

<a id="unreal.GameplayCueParameters.matched_tag_name"></a>

#### matched\_tag\_name

```python
@matched_tag_name.setter
def matched_tag_name(value: GameplayTag) -> None
```

<a id="unreal.GameplayCueParameters.original_tag"></a>

#### original\_tag

```python
@property
def original_tag() -> GameplayTag
```

(GameplayTag):  [Read-Write] The original tag of the gameplay cue

<a id="unreal.GameplayCueParameters.original_tag"></a>

#### original\_tag

```python
@original_tag.setter
def original_tag(value: GameplayTag) -> None
```

<a id="unreal.GameplayCueParameters.aggregated_source_tags"></a>

#### aggregated\_source\_tags

```python
@property
def aggregated_source_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] The aggregated source tags taken from the effect spec

<a id="unreal.GameplayCueParameters.aggregated_source_tags"></a>

#### aggregated\_source\_tags

```python
@aggregated_source_tags.setter
def aggregated_source_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.GameplayCueParameters.aggregated_target_tags"></a>

#### aggregated\_target\_tags

```python
@property
def aggregated_target_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] The aggregated target tags taken from the effect spec

<a id="unreal.GameplayCueParameters.aggregated_target_tags"></a>

#### aggregated\_target\_tags

```python
@aggregated_target_tags.setter
def aggregated_target_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.GameplayCueParameters.location"></a>

#### location

```python
@property
def location() -> Vector_NetQuantize10
```

(Vector_NetQuantize10):  [Read-Write] Location cue took place at

<a id="unreal.GameplayCueParameters.location"></a>

#### location

```python
@location.setter
def location(value: Vector_NetQuantize10) -> None
```

<a id="unreal.GameplayCueParameters.normal"></a>

#### normal

```python
@property
def normal() -> Vector_NetQuantizeNormal
```

(Vector_NetQuantizeNormal):  [Read-Write] Normal of impact that caused cue

<a id="unreal.GameplayCueParameters.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Vector_NetQuantizeNormal) -> None
```

<a id="unreal.GameplayCueParameters.instigator"></a>

#### instigator

```python
@property
def instigator() -> Actor
```

(Actor):  [Read-Write] Instigator actor, the actor that owns the ability system component

<a id="unreal.GameplayCueParameters.instigator"></a>

#### instigator

```python
@instigator.setter
def instigator(value: Actor) -> None
```

<a id="unreal.GameplayCueParameters.effect_causer"></a>

#### effect\_causer

```python
@property
def effect_causer() -> Actor
```

(Actor):  [Read-Write] The physical actor that actually did the damage, can be a weapon or projectile

<a id="unreal.GameplayCueParameters.effect_causer"></a>

#### effect\_causer

```python
@effect_causer.setter
def effect_causer(value: Actor) -> None
```

<a id="unreal.GameplayCueParameters.source_object"></a>

#### source\_object

```python
@property
def source_object() -> Object
```

(Object):  [Read-Write] Object this effect was created from, can be an actor or static object. Useful to bind an effect to a gameplay object

<a id="unreal.GameplayCueParameters.source_object"></a>

#### source\_object

```python
@source_object.setter
def source_object(value: Object) -> None
```

<a id="unreal.GameplayCueParameters.physical_material"></a>

#### physical\_material

```python
@property
def physical_material() -> PhysicalMaterial
```

(PhysicalMaterial):  [Read-Write] PhysMat of the hit, if there was a hit.

<a id="unreal.GameplayCueParameters.physical_material"></a>

#### physical\_material

```python
@physical_material.setter
def physical_material(value: PhysicalMaterial) -> None
```

<a id="unreal.GameplayCueParameters.gameplay_effect_level"></a>

#### gameplay\_effect\_level

```python
@property
def gameplay_effect_level() -> int
```

(int32):  [Read-Write] If originating from a GameplayEffect, the level of that GameplayEffect

<a id="unreal.GameplayCueParameters.gameplay_effect_level"></a>

#### gameplay\_effect\_level

```python
@gameplay_effect_level.setter
def gameplay_effect_level(value: int) -> None
```

<a id="unreal.GameplayCueParameters.ability_level"></a>

#### ability\_level

```python
@property
def ability_level() -> int
```

(int32):  [Read-Write] If originating from an ability, this will be the level of that ability

<a id="unreal.GameplayCueParameters.ability_level"></a>

#### ability\_level

```python
@ability_level.setter
def ability_level(value: int) -> None
```

<a id="unreal.GameplayCueParameters.target_attach_component"></a>

#### target\_attach\_component

```python
@property
def target_attach_component() -> SceneComponent
```

(SceneComponent):  [Read-Write] Could be used to say "attach FX to this component always"

<a id="unreal.GameplayCueParameters.target_attach_component"></a>

#### target\_attach\_component

```python
@target_attach_component.setter
def target_attach_component(value: SceneComponent) -> None
```

<a id="unreal.GameplayCueParameters.replicate_location_when_using_minimal_rep_proxy"></a>

#### replicate\_location\_when\_using\_minimal\_rep\_proxy

```python
@property
def replicate_location_when_using_minimal_rep_proxy() -> bool
```

(bool):  [Read-Write] If we're using a minimal replication proxy, should we replicate location for this cue

<a id="unreal.GameplayCueParameters.replicate_location_when_using_minimal_rep_proxy"></a>

#### replicate\_location\_when\_using\_minimal\_rep\_proxy

```python
@replicate_location_when_using_minimal_rep_proxy.setter
def replicate_location_when_using_minimal_rep_proxy(value: bool) -> None
```

<a id="unreal.GameplayEffectRemovalInfo"></a>