## PCGInstanceDataPackerByAttribute Objects

```python
class PCGInstanceDataPackerByAttribute(PCGInstanceDataPackerBase)
```

PCGInstance Data Packer by Attribute

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGInstanceDataPackerByAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_names`` (Array[Name]):  [Read-Write]
  deprecated: AttributeNames has been deprecated. Use AttributeSelectors instead.
- ``attribute_selectors`` (Array[PCGAttributePropertyInputSelector]):  [Read-Write]

<a id="unreal.PCGInstanceDataPackerByAttribute.attribute_selectors"></a>

#### attribute_selectors

```python
@property
def attribute_selectors() -> Array[PCGAttributePropertyInputSelector]
```

(Array[PCGAttributePropertyInputSelector]):  [Read-Write]

<a id="unreal.PCGInstanceDataPackerByAttribute.attribute_selectors"></a>

#### attribute_selectors

```python
@attribute_selectors.setter
def attribute_selectors(
        value: Array[PCGAttributePropertyInputSelector]) -> None
```

<a id="unreal.PCGInstanceDataPackerByAttribute.attribute_names"></a>

#### attribute_names

```python
@property
def attribute_names() -> Array[Name]
```

(Array[Name]):  [Read-Write]
deprecated: AttributeNames has been deprecated. Use AttributeSelectors instead.

<a id="unreal.PCGInstanceDataPackerByAttribute.attribute_names"></a>

#### attribute_names

```python
@attribute_names.setter
def attribute_names(value: Array[Name]) -> None
```

<a id="unreal.PCGInstancePackerByAttribute"></a>