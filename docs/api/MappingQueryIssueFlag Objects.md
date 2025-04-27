## MappingQueryIssueFlag Objects

```python
class MappingQueryIssueFlag(EnumBase)
```

Mapping issues arising from a QueryMapKeyIn... call

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputMappingQuery.h

<a id="unreal.MappingQueryIssueFlag.NO_ISSUE"></a>

#### NO_ISSUE

0: Mapping will not affect any existing mappings and is safe to apply.

<a id="unreal.MappingQueryIssueFlag.RESERVED_BY_ACTION"></a>

#### RESERVED_BY_ACTION

1: Mapping has been reserved for the exclusive use of another action. The new mapping should be refused.

<a id="unreal.MappingQueryIssueFlag.HIDES_EXISTING_MAPPING"></a>

#### HIDES_EXISTING_MAPPING

2: Mapping will cause an existing mapping to be hidden and/or need remapping.

<a id="unreal.MappingQueryIssueFlag.HIDDEN_BY_EXISTING_MAPPING"></a>

#### HIDDEN_BY_EXISTING_MAPPING

4: Mapping will not be functional, due to an existing mapping blocking it.

<a id="unreal.MappingQueryIssueFlag.COLLISION_WITH_MAPPING_IN_SAME_CONTEXT"></a>

#### COLLISION_WITH_MAPPING_IN_SAME_CONTEXT

8: Mapping will be functional, but a collision with another mapping within this context may cause issues.

<a id="unreal.MappingQueryIssueFlag.FORCES_TYPE_PROMOTION"></a>

#### FORCES_TYPE_PROMOTION

16: Trying to bind an FKey with a less complex type than the bound action expects (e.g. Keyboard key bound to a 2D Gamepad axis. May not be desirable). Note: bool -> Axis1D promotions are never considered forced.

<a id="unreal.MappingQueryIssueFlag.FORCES_TYPE_DEMOTION"></a>

#### FORCES_TYPE_DEMOTION

32: Trying to bind an FKey with a more complex type than the bound action supports (this could behave oddly e.g. 2D Gamepad axis bound to a 1D axis will ignore Y axis)

<a id="unreal.PlayerMappableKeySettingBehaviors"></a>