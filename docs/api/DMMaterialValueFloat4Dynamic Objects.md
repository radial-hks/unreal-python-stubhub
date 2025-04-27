## DMMaterialValueFloat4Dynamic Objects

```python
class DMMaterialValueFloat4Dynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValueFloat4 for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat4Dynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueFloat4Dynamic.value"></a>

#### value

```python
@property
def value() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueFloat4Dynamic.value"></a>

#### value

```python
@value.setter
def value(value: LinearColor) -> None
```

<a id="unreal.DMMaterialValueFloat4Dynamic.set_value"></a>

#### set_value

```python
def set_value(value: LinearColor) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (LinearColor):

<a id="unreal.DMMaterialValueFloat4Dynamic.get_value"></a>

#### get_value

```python
def get_value() -> LinearColor
```

x.get_value() -> LinearColor
Get Value

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueFloat4Dynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> LinearColor
```

x.get_default_value() -> LinearColor
Get Default Value

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueRenderTarget"></a>