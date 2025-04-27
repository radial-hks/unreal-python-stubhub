## AvaMaterialParameterModifier Objects

```python
class AvaMaterialParameterModifier(AvaArrangeBaseModifier)
```

This modifier sets specified dynamic materials parameters on an actor and its children

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaMaterialParameterModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_parameters`` (AvaMaterialParameterMap):  [Read-Write] Which parameters should we set on the Material Designer Instance
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``update_children`` (bool):  [Read-Write] Will also look into attached children actors

<a id="unreal.AvaMaterialParameterModifier.set_update_children"></a>

#### set_update_children

```python
def set_update_children(update_children: bool) -> None
```

x.set_update_children(update_children) -> None
Set Update Children

Args:
    update_children (bool):

<a id="unreal.AvaMaterialParameterModifier.set_material_parameters"></a>

#### set_material_parameters

```python
def set_material_parameters(parameter_map: AvaMaterialParameterMap) -> None
```

x.set_material_parameters(parameter_map) -> None
Set Material Parameters

Args:
    parameter_map (AvaMaterialParameterMap):

<a id="unreal.AvaMaterialParameterModifier.get_update_children"></a>

#### get_update_children

```python
def get_update_children() -> bool
```

x.get_update_children() -> bool
Get Update Children

Returns:
    bool:

<a id="unreal.AvaMaterialParameterModifier.get_material_parameters"></a>

#### get_material_parameters

```python
def get_material_parameters() -> AvaMaterialParameterMap
```

x.get_material_parameters() -> AvaMaterialParameterMap
Get Material Parameters

Returns:
    AvaMaterialParameterMap:

<a id="unreal.AvaGlobalOpacityModifier"></a>