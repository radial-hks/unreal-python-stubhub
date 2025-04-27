## PCGDataCollection Objects

```python
class PCGDataCollection(StructBase)
```

PCGData Collection

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cancel_execution_on_empty`` (bool):  [Read-Write] Deprecated - Will be removed in 5.4
- ``tagged_data`` (Array[PCGTaggedData]):  [Read-Write]

<a id="unreal.PCGDataCollection.__init__"></a>

#### __init__

```python
def __init__(tagged_data: Array[PCGTaggedData] = [],
             cancel_execution_on_empty: bool = False) -> None
```

<a id="unreal.PCGDataCollection.tagged_data"></a>

#### tagged_data

```python
@property
def tagged_data() -> Array[PCGTaggedData]
```

(Array[PCGTaggedData]):  [Read-Write]

<a id="unreal.PCGDataCollection.tagged_data"></a>

#### tagged_data

```python
@tagged_data.setter
def tagged_data(value: Array[PCGTaggedData]) -> None
```

<a id="unreal.PCGDataCollection.cancel_execution_on_empty"></a>

#### cancel_execution_on_empty

```python
@property
def cancel_execution_on_empty() -> bool
```

(bool):  [Read-Write] Deprecated - Will be removed in 5.4

<a id="unreal.PCGDataCollection.cancel_execution_on_empty"></a>

#### cancel_execution_on_empty

```python
@cancel_execution_on_empty.setter
def cancel_execution_on_empty(value: bool) -> None
```

<a id="unreal.PCGDataCollection.get_typed_inputs_by_tag"></a>

#### get_typed_inputs_by_tag

```python
def get_typed_inputs_by_tag(
    tag: str,
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

x.get_typed_inputs_by_tag(tag, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type and having the provided tag, returning matching tagged data in the OutTaggedData value too

Args:
    tag (str): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataCollection.get_typed_inputs_by_pin_label"></a>

#### get_typed_inputs_by_pin_label

```python
def get_typed_inputs_by_pin_label(
    pin_label: Name,
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

x.get_typed_inputs_by_pin_label(pin_label, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type and on the given pin label, returning matching tagged data in the OutTaggedData value too

Args:
    pin_label (Name): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataCollection.get_typed_inputs_by_pin"></a>

#### get_typed_inputs_by_pin

```python
def get_typed_inputs_by_pin(
    pin: PCGPinProperties,
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

x.get_typed_inputs_by_pin(pin, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type and on the given pin, returning matching tagged data in the OutTaggedData value too

Args:
    pin (PCGPinProperties): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataCollection.get_typed_inputs"></a>

#### get_typed_inputs

```python
def get_typed_inputs(
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

x.get_typed_inputs(data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type, returning matching tagged data in the OutTaggedData value too

Args:
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataCollection.add_to_collection"></a>

#### add_to_collection

```python
def add_to_collection(data: PCGData, pin_label: Name,
                      tags: Array[str]) -> None
```

x.add_to_collection(data, pin_label, tags) -> None
Adds a data object to a given collection, simpler usage than making a PCGTaggedData object. InTags can be empty.

Args:
    data (PCGData): 
    pin_label (Name): 
    tags (Array[str]):

<a id="unreal.PCGTaggedData"></a>