## ImmunityGameplayEffectComponent Objects

```python
class ImmunityGameplayEffectComponent(GameplayEffectComponent)
```

Immunity is blocking the application of _other_ GameplayEffectSpecs.
This registers a global handler on the ASC to block the application of other GameplayEffectSpecs.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: ImmunityGameplayEffectComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_friendly_name`` (str):  [Read-Only] Friendly name for displaying in the Editor's Gameplay Effect Component Index (
  see: UGameplayEffect::GEComponents). We set EditCondition False here so it doesn't show up otherwise.
- ``immunity_queries`` (Array[GameplayEffectQuery]):  [Read-Write] Grants immunity to GameplayEffects that match this query.

<a id="unreal.ImmunityGameplayEffectComponent.immunity_queries"></a>

#### immunity\_queries

```python
@property
def immunity_queries() -> Array[GameplayEffectQuery]
```

(Array[GameplayEffectQuery]):  [Read-Only] Grants immunity to GameplayEffects that match this query.

<a id="unreal.AbilityAsync_WaitAttributeChanged"></a>