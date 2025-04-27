## DMMaterialValueFloat1Dynamic Objects

```python
class DMMaterialValueFloat1Dynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValueFloat1 for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat1Dynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (float):  [Read-Write]

<a id="unreal.DMMaterialValueFloat1Dynamic.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.DMMaterialValueFloat1Dynamic.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.DMMaterialValueFloat1Dynamic.set_value"></a>

#### set_value

```python
def set_value(value: float) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (float):

<a id="unreal.DMMaterialValueFloat1Dynamic.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Get Value

Returns:
    float:

<a id="unreal.DMMaterialValueFloat1Dynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> float
```

x.get_default_value() -> float
Get Default Value

Returns:
    float:

<a id="unreal.DMMaterialValueFloat2Dynamic"></a>