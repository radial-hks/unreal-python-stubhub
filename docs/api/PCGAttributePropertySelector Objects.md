## PCGAttributePropertySelector Objects

```python
class PCGAttributePropertySelector(StructBase)
```

Blueprint class to allow to select an attribute or a property.
It will handle the logic and can only be modified using the blueprint library defined below.
Also has a custom detail view in the PCGEditor plugin.

Note: This class should not be used as is, but need to be referenced by either an "InputSelector" or an "OutputSelector" (defined below).
The reason for that is to provide 2 different default values for input and output. Input will have the "
Last": default value (meaning last attribute written to) and the Output will have "
Source": default value (meaning, same thing as input).

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributePropertySelector.h

<a id="unreal.PCGAttributePropertySelector.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PCGAttributePropertySelector.set_point_property"></a>

#### set_point_property

```python
def set_point_property(point_property: PCGPointProperties) -> bool
```

x.set_point_property(point_property) -> bool
Set Point Property

Args:
    point_property (PCGPointProperties): 

Returns:
    bool:

<a id="unreal.PCGAttributePropertySelector.set_extra_property"></a>

#### set_extra_property

```python
def set_extra_property(extra_property: PCGExtraProperties) -> bool
```

x.set_extra_property(extra_property) -> bool
Set Extra Property

Args:
    extra_property (PCGExtraProperties): 

Returns:
    bool:

<a id="unreal.PCGAttributePropertySelector.set_attribute_name"></a>

#### set_attribute_name

```python
def set_attribute_name(attribute_name: Name) -> bool
```

x.set_attribute_name(attribute_name) -> bool
Set Attribute Name

Args:
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGAttributePropertySelector.get_selection"></a>

#### get_selection

```python
def get_selection() -> PCGAttributePropertySelection
```

x.get_selection() -> PCGAttributePropertySelection
Get Selection

Returns:
    PCGAttributePropertySelection:

<a id="unreal.PCGAttributePropertySelector.get_point_property"></a>

#### get_point_property

```python
def get_point_property() -> PCGPointProperties
```

x.get_point_property() -> PCGPointProperties
Get Point Property

Returns:
    PCGPointProperties:

<a id="unreal.PCGAttributePropertySelector.get_name"></a>

#### get_name

```python
def get_name() -> Name
```

x.get_name() -> Name
Get Name

Returns:
    Name:

<a id="unreal.PCGAttributePropertySelector.get_extra_property"></a>

#### get_extra_property

```python
def get_extra_property() -> PCGExtraProperties
```

x.get_extra_property() -> PCGExtraProperties
Get Extra Property

Returns:
    PCGExtraProperties:

<a id="unreal.PCGAttributePropertySelector.get_extra_names"></a>

#### get_extra_names

```python
def get_extra_names() -> Array[str]
```

x.get_extra_names() -> Array[str]
Get Extra Names

Returns:
    Array[str]:

<a id="unreal.PCGAttributePropertySelector.get_attribute_name"></a>

#### get_attribute_name

```python
def get_attribute_name() -> Name
```

x.get_attribute_name() -> Name
Get Attribute Name

Returns:
    Name:

<a id="unreal.PCGAttributePropertyInputSelector"></a>