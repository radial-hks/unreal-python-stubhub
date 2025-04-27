## PlayerMappableKeySettingBehaviors Objects

```python
class PlayerMappableKeySettingBehaviors(EnumBase)
```

Defines which Player Mappable Key Setting to use for a Action Key Mapping.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedActionKeyMapping.h

<a id="unreal.PlayerMappableKeySettingBehaviors.INHERIT_SETTINGS_FROM_ACTION"></a>

#### INHERIT_SETTINGS_FROM_ACTION

0: Use the Settings specified in the Input Action.

<a id="unreal.PlayerMappableKeySettingBehaviors.OVERRIDE_SETTINGS"></a>

#### OVERRIDE_SETTINGS

1: Use the Settings specified in the Action Key Mapping overriding the ones specified in the Input action.

<a id="unreal.PlayerMappableKeySettingBehaviors.IGNORE_SETTINGS"></a>

#### IGNORE_SETTINGS

2: Don't use any Settings even if one is specified in the Input Action.

<a id="unreal.TriggerEvent"></a>