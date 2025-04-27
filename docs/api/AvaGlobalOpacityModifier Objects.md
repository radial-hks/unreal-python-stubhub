## AvaGlobalOpacityModifier Objects

```python
class AvaGlobalOpacityModifier(AvaMaterialParameterModifier)
```

This modifier sets global opacity parameters on an actor with Material Designer Instances generated with the Material Designer

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaGlobalOpacityModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_opacity`` (float):  [Read-Write] Global opacity to set on all Material Designer Instances
- ``material_parameters`` (AvaMaterialParameterMap):  [Read-Write] Which parameters should we set on the Material Designer Instance
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``update_children`` (bool):  [Read-Write] Will also look into attached children actors

<a id="unreal.AvaGlobalOpacityModifier.set_global_opacity"></a>

#### set_global_opacity

```python
def set_global_opacity(opacity: float) -> None
```

x.set_global_opacity(opacity) -> None
Set Global Opacity

Args:
    opacity (float):

<a id="unreal.AvaGlobalOpacityModifier.get_global_opacity"></a>

#### get_global_opacity

```python
def get_global_opacity() -> float
```

x.get_global_opacity() -> float
Get Global Opacity

Returns:
    float:

<a id="unreal.AvaGridArrangeModifier"></a>