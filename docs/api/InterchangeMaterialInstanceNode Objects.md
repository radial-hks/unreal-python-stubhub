## InterchangeMaterialInstanceNode Objects

```python
class InterchangeMaterialInstanceNode(InterchangeBaseNode)
```

Interchange Material Instance Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeMaterialInstanceNode.h

<a id="unreal.InterchangeMaterialInstanceNode.set_custom_parent"></a>

#### set\_custom\_parent

```python
def set_custom_parent(attribute_value: str) -> bool
```

x.set_custom_parent(attribute_value) -> bool
Set Custom Parent

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialInstanceNode.get_vector_parameter_value"></a>

#### get\_vector\_parameter\_value

```python
def get_vector_parameter_value(parameter_name: str) -> Optional[LinearColor]
```

x.get_vector_parameter_value(parameter_name) -> LinearColor or None
Get Vector Parameter Value

Args:
    parameter_name (str): 

Returns:
    LinearColor or None: 

    attribute_value (LinearColor):

<a id="unreal.InterchangeMaterialInstanceNode.get_texture_parameter_value"></a>

#### get\_texture\_parameter\_value

```python
def get_texture_parameter_value(parameter_name: str) -> Optional[str]
```

x.get_texture_parameter_value(parameter_name) -> str or None
Get Texture Parameter Value

Args:
    parameter_name (str): 

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeMaterialInstanceNode.get_static_switch_parameter_value"></a>

#### get\_static\_switch\_parameter\_value

```python
def get_static_switch_parameter_value(parameter_name: str) -> Optional[bool]
```

x.get_static_switch_parameter_value(parameter_name) -> bool or None
Get Static Switch Parameter Value

Args:
    parameter_name (str): 

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMaterialInstanceNode.get_scalar_parameter_value"></a>

#### get\_scalar\_parameter\_value

```python
def get_scalar_parameter_value(parameter_name: str) -> Optional[float]
```

x.get_scalar_parameter_value(parameter_name) -> float or None
Get Scalar Parameter Value

Args:
    parameter_name (str): 

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeMaterialInstanceNode.get_custom_parent"></a>

#### get\_custom\_parent

```python
def get_custom_parent() -> Optional[str]
```

x.get_custom_parent() -> str or None
Get Custom Parent

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeMaterialInstanceNode.add_vector_parameter_value"></a>

#### add\_vector\_parameter\_value

```python
def add_vector_parameter_value(parameter_name: str,
                               attribute_value: LinearColor) -> bool
```

x.add_vector_parameter_value(parameter_name, attribute_value) -> bool
Add Vector Parameter Value

Args:
    parameter_name (str): 
    attribute_value (LinearColor): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialInstanceNode.add_texture_parameter_value"></a>

#### add\_texture\_parameter\_value

```python
def add_texture_parameter_value(parameter_name: str,
                                attribute_value: str) -> bool
```

x.add_texture_parameter_value(parameter_name, attribute_value) -> bool
Add Texture Parameter Value

Args:
    parameter_name (str): 
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialInstanceNode.add_static_switch_parameter_value"></a>

#### add\_static\_switch\_parameter\_value

```python
def add_static_switch_parameter_value(parameter_name: str,
                                      attribute_value: bool) -> bool
```

x.add_static_switch_parameter_value(parameter_name, attribute_value) -> bool
Add Static Switch Parameter Value

Args:
    parameter_name (str): 
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialInstanceNode.add_scalar_parameter_value"></a>

#### add\_scalar\_parameter\_value

```python
def add_scalar_parameter_value(parameter_name: str,
                               attribute_value: float) -> bool
```

x.add_scalar_parameter_value(parameter_name, attribute_value) -> bool
Add Scalar Parameter Value

Args:
    parameter_name (str): 
    attribute_value (float): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode"></a>