## PCGAttributePropertySelectorBlueprintHelpers Objects

```python
class PCGAttributePropertySelectorBlueprintHelpers(BlueprintFunctionLibrary)
```

Helper class to allow the BP to call the custom setters and getters on FPCGAttributePropertySelector.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributePropertySelector.h

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.set_point_property"></a>

#### set_point_property

```python
@classmethod
def set_point_property(
    cls, selector: PCGAttributePropertySelector,
    point_property: PCGPointProperties
) -> Optional[PCGAttributePropertySelector]
```

X.set_point_property(selector, point_property) -> PCGAttributePropertySelector or None
Set Point Property

Args:
    selector (PCGAttributePropertySelector): 
    point_property (PCGPointProperties): 

Returns:
    PCGAttributePropertySelector or None: 

    selector (PCGAttributePropertySelector):

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.set_extra_property"></a>

#### set_extra_property

```python
@classmethod
def set_extra_property(
    cls, selector: PCGAttributePropertySelector,
    extra_property: PCGExtraProperties
) -> Optional[PCGAttributePropertySelector]
```

X.set_extra_property(selector, extra_property) -> PCGAttributePropertySelector or None
Set Extra Property

Args:
    selector (PCGAttributePropertySelector): 
    extra_property (PCGExtraProperties): 

Returns:
    PCGAttributePropertySelector or None: 

    selector (PCGAttributePropertySelector):

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.set_attribute_name"></a>

#### set_attribute_name

```python
@classmethod
def set_attribute_name(
        cls, selector: PCGAttributePropertySelector,
        attribute_name: Name) -> Optional[PCGAttributePropertySelector]
```

X.set_attribute_name(selector, attribute_name) -> PCGAttributePropertySelector or None
Set Attribute Name

Args:
    selector (PCGAttributePropertySelector): 
    attribute_name (Name): 

Returns:
    PCGAttributePropertySelector or None: 

    selector (PCGAttributePropertySelector):

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.get_selection"></a>

#### get_selection

```python
@classmethod
def get_selection(
        cls, selector: PCGAttributePropertySelector
) -> PCGAttributePropertySelection
```

X.get_selection(selector) -> PCGAttributePropertySelection
Get Selection

Args:
    selector (PCGAttributePropertySelector): 

Returns:
    PCGAttributePropertySelection:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.get_point_property"></a>

#### get_point_property

```python
@classmethod
def get_point_property(
        cls, selector: PCGAttributePropertySelector) -> PCGPointProperties
```

X.get_point_property(selector) -> PCGPointProperties
Get Point Property

Args:
    selector (PCGAttributePropertySelector): 

Returns:
    PCGPointProperties:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.get_name"></a>

#### get_name

```python
@classmethod
def get_name(cls, selector: PCGAttributePropertySelector) -> Name
```

X.get_name(selector) -> Name
Get Name

Args:
    selector (PCGAttributePropertySelector): 

Returns:
    Name:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.get_extra_property"></a>

#### get_extra_property

```python
@classmethod
def get_extra_property(
        cls, selector: PCGAttributePropertySelector) -> PCGExtraProperties
```

X.get_extra_property(selector) -> PCGExtraProperties
Get Extra Property

Args:
    selector (PCGAttributePropertySelector): 

Returns:
    PCGExtraProperties:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.get_extra_names"></a>

#### get_extra_names

```python
@classmethod
def get_extra_names(cls, selector: PCGAttributePropertySelector) -> Array[str]
```

X.get_extra_names(selector) -> Array[str]
Get Extra Names

Args:
    selector (PCGAttributePropertySelector): 

Returns:
    Array[str]:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.get_attribute_name"></a>

#### get_attribute_name

```python
@classmethod
def get_attribute_name(cls, selector: PCGAttributePropertySelector) -> Name
```

X.get_attribute_name(selector) -> Name
Get Attribute Name

Args:
    selector (PCGAttributePropertySelector): 

Returns:
    Name:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.copy_and_fix_source"></a>

#### copy_and_fix_source

```python
@classmethod
def copy_and_fix_source(
    cls, output_selector: PCGAttributePropertyOutputSelector,
    input_selector: PCGAttributePropertyInputSelector
) -> PCGAttributePropertyOutputSelector
```

X.copy_and_fix_source(output_selector, input_selector) -> PCGAttributePropertyOutputSelector
Copy and Fix Source

Args:
    output_selector (PCGAttributePropertyOutputSelector): 
    input_selector (PCGAttributePropertyInputSelector): 

Returns:
    PCGAttributePropertyOutputSelector:

<a id="unreal.PCGAttributePropertySelectorBlueprintHelpers.copy_and_fix_last"></a>

#### copy_and_fix_last

```python
@classmethod
def copy_and_fix_last(cls, selector: PCGAttributePropertyInputSelector,
                      data: PCGData) -> PCGAttributePropertyInputSelector
```

X.copy_and_fix_last(selector, data) -> PCGAttributePropertyInputSelector
Copy and Fix Last

Args:
    selector (PCGAttributePropertyInputSelector): 
    data (PCGData): 

Returns:
    PCGAttributePropertyInputSelector:

<a id="unreal.PCGMetadataSettingsBase"></a>