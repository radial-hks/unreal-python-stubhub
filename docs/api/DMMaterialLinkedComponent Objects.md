## DMMaterialLinkedComponent Objects

```python
class DMMaterialLinkedComponent(DMMaterialComponent)
```

A component which links to a specific parent component in the hierarchy instead of its Outer.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialLinkedComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]

<a id="unreal.DMMaterialLinkedComponent.set_parent_component"></a>

#### set_parent_component

```python
def set_parent_component(parent_component: DMMaterialComponent) -> None
```

x.set_parent_component(parent_component) -> None
Sets the linked parent component.

Args:
    parent_component (DMMaterialComponent):

<a id="unreal.DMMaterialValue"></a>