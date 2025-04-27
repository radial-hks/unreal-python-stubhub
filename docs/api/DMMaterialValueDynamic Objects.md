## DMMaterialValueDynamic Objects

```python
class DMMaterialValueDynamic(DMMaterialComponentDynamic)
```

A value used inside an instanced material instance. Links to the original value in the parent material.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]

<a id="unreal.DMMaterialValueDynamic.is_default_value"></a>

#### is_default_value

```python
def is_default_value() -> bool
```

x.is_default_value() -> bool
Returns true if this value dynamic's value is the same as the parent value's value.

Returns:
    bool:

<a id="unreal.DMMaterialValueDynamic.get_parent_value"></a>

#### get_parent_value

```python
def get_parent_value() -> DMMaterialValue
```

x.get_parent_value() -> DMMaterialValue
Resolves (if necessary) and returns the value this dynamic value is based on.

Returns:
    DMMaterialValue:

<a id="unreal.DMMaterialValueDynamic.apply_default_value"></a>

#### apply_default_value

```python
def apply_default_value() -> None
```

x.apply_default_value() -> None
Apply Default Value

<a id="unreal.DMMaterialValueBoolDynamic"></a>