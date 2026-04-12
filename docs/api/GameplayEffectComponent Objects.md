## GameplayEffectComponent Objects

```python
class GameplayEffectComponent(Object)
```

Gameplay Effect Component (aka GEComponent)

GEComponents are what define how a GameplayEffect behaves.  Introduced in UE 5.3, there are very few calls from UGameplayEffect to UGameplayEffectComponent by design.
Instead of providing a larger API for all desired functionality, the implementer of a GEComponent must read the GE flow carefully and register desired callbacks
to achieve the desired results.  This effectively limits the implementation of GEComponents to native code for the time being.

GEComponents live Within a GameplayEffect (which is typically a data-only blueprint asset).  Thus, like GEs, only one GEComponent exists for all applied instances.
One of the unintuitive caveats of this is that GEComponent should not contain any runtime manipulated/instanced data (e.g. stored state per execution).
One must take careful consideration about where to store any data (and thus when it can be evaluated).  The early implementations typically work around this by
storing small amounts of runtime data on the desired callbacks (e.g. by binding extra parameters on the delegate).  This may explain why some functionality is still
in UGameplayEffect rather than a UGameplayEffectComponent.  Future implementations may need extra data stored on the FGameplayEffectSpec (i.e. Gameplay Effect Spec Components).
see: GameplayEffect.h for further notes, especially on the terminology used (Added vs. Executed vs. Apply).

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_friendly_name`` (str):  [Read-Only] Friendly name for displaying in the Editor's Gameplay Effect Component Index (
  see: UGameplayEffect::GEComponents). We set EditCondition False here so it doesn't show up otherwise.

<a id="unreal.GameplayEffectUIData"></a>