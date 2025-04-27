## PropertyEntry Objects

```python
class PropertyEntry(StructBase)
```

Structure to represent a single property the user wants to bake out for a given set of materials

**C++ Source:**

- **Module**: MaterialBaking
- **File**: MaterialOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constant_value`` (float):  [Read-Write] Defines the value representing this property in the final proxy material
- ``custom_size`` (IntPoint):  [Read-Write] Defines the size of the output textures for the baked out material properties
- ``property_`` (MaterialProperty):  [Read-Write] Property which should be baked out
- ``use_constant_value`` (bool):  [Read-Write] Wheter or not to use Constant Value as the final 'baked out' value for the this property
- ``use_custom_size`` (bool):  [Read-Write] Whether or not to use the value of custom size for the output texture

<a id="unreal.PropertyEntry.__init__"></a>

#### __init__

```python
def __init__(property_: MaterialProperty = MaterialProperty.MP_EMISSIVE_COLOR,
             use_custom_size: bool = False,
             custom_size: IntPoint = [0, 0],
             use_constant_value: bool = False,
             constant_value: float = 0.000000) -> None
```

<a id="unreal.PropertyEntry.property_"></a>

#### property_

```python
@property
def property_() -> MaterialProperty
```

(MaterialProperty):  [Read-Write] Property which should be baked out

<a id="unreal.PropertyEntry.property_"></a>

#### property_

```python
@property_.setter
def property_(value: MaterialProperty) -> None
```

<a id="unreal.PropertyEntry.use_custom_size"></a>

#### use_custom_size

```python
@property
def use_custom_size() -> bool
```

(bool):  [Read-Write] Whether or not to use the value of custom size for the output texture

<a id="unreal.PropertyEntry.use_custom_size"></a>

#### use_custom_size

```python
@use_custom_size.setter
def use_custom_size(value: bool) -> None
```

<a id="unreal.PropertyEntry.custom_size"></a>

#### custom_size

```python
@property
def custom_size() -> IntPoint
```

(IntPoint):  [Read-Write] Defines the size of the output textures for the baked out material properties

<a id="unreal.PropertyEntry.custom_size"></a>

#### custom_size

```python
@custom_size.setter
def custom_size(value: IntPoint) -> None
```

<a id="unreal.PropertyEntry.use_constant_value"></a>

#### use_constant_value

```python
@property
def use_constant_value() -> bool
```

(bool):  [Read-Write] Wheter or not to use Constant Value as the final 'baked out' value for the this property

<a id="unreal.PropertyEntry.use_constant_value"></a>

#### use_constant_value

```python
@use_constant_value.setter
def use_constant_value(value: bool) -> None
```

<a id="unreal.PropertyEntry.constant_value"></a>

#### constant_value

```python
@property
def constant_value() -> float
```

(float):  [Read-Write] Defines the value representing this property in the final proxy material

<a id="unreal.PropertyEntry.constant_value"></a>

#### constant_value

```python
@constant_value.setter
def constant_value(value: float) -> None
```

<a id="unreal.MaterialStatistics"></a>