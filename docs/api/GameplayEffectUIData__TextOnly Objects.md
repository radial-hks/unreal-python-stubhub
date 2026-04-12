## GameplayEffectUIData\_TextOnly Objects

```python
class GameplayEffectUIData_TextOnly(GameplayEffectUIData)
```

UI data that contains only text. This is mostly used as an example of a subclass of UGameplayEffectUIData.
If your game needs only text, this is a reasonable class to use. To include more data, make a custom subclass of UGameplayEffectUIData.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectUIData_TextOnly.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write]
- ``editor_friendly_name`` (str):  [Read-Only] Friendly name for displaying in the Editor's Gameplay Effect Component Index (
  see: UGameplayEffect::GEComponents). We set EditCondition False here so it doesn't show up otherwise.

<a id="unreal.GameplayEffectUIData_TextOnly.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Only]

<a id="unreal.ImmunityGameplayEffectComponent"></a>