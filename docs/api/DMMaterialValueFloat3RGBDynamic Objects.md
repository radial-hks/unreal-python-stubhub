## DMMaterialValueFloat3RGBDynamic Objects

```python
class DMMaterialValueFloat3RGBDynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValue3RGB for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat3RGBDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3RGBDynamic.value"></a>

#### value

```python
@property
def value() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3RGBDynamic.value"></a>

#### value

```python
@value.setter
def value(value: LinearColor) -> None
```

<a id="unreal.DMMaterialValueFloat3RGBDynamic.set_value"></a>

#### set_value

```python
def set_value(value: LinearColor) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (LinearColor):

<a id="unreal.DMMaterialValueFloat3RGBDynamic.get_value"></a>

#### get_value

```python
def get_value() -> LinearColor
```

x.get_value() -> LinearColor
Get Value

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueFloat3RGBDynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> LinearColor
```

x.get_default_value() -> LinearColor
Get Default Value

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueFloat3RPYDynamic"></a>