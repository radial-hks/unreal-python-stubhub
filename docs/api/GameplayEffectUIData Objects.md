## GameplayEffectUIData Objects

```python
class GameplayEffectUIData(GameplayEffectComponent)
```

UGameplayEffectUIData
Base class to provide game-specific data about how to describe a Gameplay Effect in the UI. Subclass with data to use in your game.
In Unreal Engine 5.3, this now derives from UGameplayEffectComponent so you can use it directly as a GameplayEffectComponent.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectUIData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_friendly_name`` (str):  [Read-Only] Friendly name for displaying in the Editor's Gameplay Effect Component Index (
  see: UGameplayEffect::GEComponents). We set EditCondition False here so it doesn't show up otherwise.

<a id="unreal.GameplayEffectUIData_TextOnly"></a>