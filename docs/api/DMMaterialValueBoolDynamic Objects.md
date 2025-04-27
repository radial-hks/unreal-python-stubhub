## DMMaterialValueBoolDynamic Objects

```python
class DMMaterialValueBoolDynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValueBool for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueBoolDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (bool):  [Read-Write]

<a id="unreal.DMMaterialValueBoolDynamic.value"></a>

#### value

```python
@property
def value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialValueBoolDynamic.value"></a>

#### value

```python
@value.setter
def value(value: bool) -> None
```

<a id="unreal.DMMaterialValueBoolDynamic.set_value"></a>

#### set_value

```python
def set_value(value: bool) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (bool):

<a id="unreal.DMMaterialValueBoolDynamic.get_value"></a>

#### get_value

```python
def get_value() -> bool
```

x.get_value() -> bool
Get Value

Returns:
    bool:

<a id="unreal.DMMaterialValueBoolDynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> bool
```

x.get_default_value() -> bool
Get Default Value

Returns:
    bool:

<a id="unreal.DMMaterialValueColorAtlasDynamic"></a>