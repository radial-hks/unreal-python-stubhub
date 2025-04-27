## PCGDataFunctionLibrary Objects

```python
class PCGDataFunctionLibrary(BlueprintFunctionLibrary)
```

PCGData Function Library

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGData.h

<a id="unreal.PCGDataFunctionLibrary.get_typed_inputs_by_tag"></a>

#### get_typed_inputs_by_tag

```python
@classmethod
def get_typed_inputs_by_tag(
    cls,
    collection: PCGDataCollection,
    tag: str,
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

X.get_typed_inputs_by_tag(collection, tag, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type and having the provided tag, returning matching tagged data in the OutTaggedData value too

Args:
    collection (PCGDataCollection): 
    tag (str): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataFunctionLibrary.get_typed_inputs_by_pin_label"></a>

#### get_typed_inputs_by_pin_label

```python
@classmethod
def get_typed_inputs_by_pin_label(
    cls,
    collection: PCGDataCollection,
    pin_label: Name,
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

X.get_typed_inputs_by_pin_label(collection, pin_label, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type and on the given pin label, returning matching tagged data in the OutTaggedData value too

Args:
    collection (PCGDataCollection): 
    pin_label (Name): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataFunctionLibrary.get_typed_inputs_by_pin"></a>

#### get_typed_inputs_by_pin

```python
@classmethod
def get_typed_inputs_by_pin(
    cls,
    collection: PCGDataCollection,
    pin: PCGPinProperties,
    data_type_class: Class = None
) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

X.get_typed_inputs_by_pin(collection, pin, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type and on the given pin, returning matching tagged data in the OutTaggedData value too

Args:
    collection (PCGDataCollection): 
    pin (PCGPinProperties): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataFunctionLibrary.get_typed_inputs"></a>

#### get_typed_inputs

```python
@classmethod
def get_typed_inputs(cls,
                     collection: PCGDataCollection,
                     data_type_class: Class = None
                     ) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

X.get_typed_inputs(collection, data_type_class=None) -> (Array[PCGData], out_tagged_data=Array[PCGTaggedData])
Gets all inputs of the given class type, returning matching tagged data in the OutTaggedData value too

Args:
    collection (PCGDataCollection): 
    data_type_class (type(Class)): 

Returns:
    Array[PCGTaggedData]: 

    out_tagged_data (Array[PCGTaggedData]):

<a id="unreal.PCGDataFunctionLibrary.get_params_by_tag"></a>

#### get_params_by_tag

```python
@classmethod
def get_params_by_tag(cls, collection: PCGDataCollection,
                      tag: str) -> Array[PCGTaggedData]
```

X.get_params_by_tag(collection, tag) -> Array[PCGTaggedData]
Get Params by Tag

Args:
    collection (PCGDataCollection): 
    tag (str): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.get_tagged_params"></a>

#### get_tagged_params

```python
@classmethod
def get_tagged_params(cls, collection: PCGDataCollection,
                      tag: str) -> Array[PCGTaggedData]
```

deprecated: 'get_tagged_params' was renamed to 'get_params_by_tag'.

<a id="unreal.PCGDataFunctionLibrary.get_params_by_pin_label"></a>

#### get_params_by_pin_label

```python
@classmethod
def get_params_by_pin_label(cls, collection: PCGDataCollection,
                            pin_label: Name) -> Array[PCGTaggedData]
```

X.get_params_by_pin_label(collection, pin_label) -> Array[PCGTaggedData]
Get Params by Pin Label

Args:
    collection (PCGDataCollection): 
    pin_label (Name): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.get_params_by_pin"></a>

#### get_params_by_pin

```python
@classmethod
def get_params_by_pin(cls, collection: PCGDataCollection,
                      pin_label: Name) -> Array[PCGTaggedData]
```

deprecated: 'get_params_by_pin' was renamed to 'get_params_by_pin_label'.

<a id="unreal.PCGDataFunctionLibrary.get_params"></a>

#### get_params

```python
@classmethod
def get_params(cls, collection: PCGDataCollection) -> Array[PCGTaggedData]
```

X.get_params(collection) -> Array[PCGTaggedData]
Get Params

Args:
    collection (PCGDataCollection): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.get_inputs_by_tag"></a>

#### get_inputs_by_tag

```python
@classmethod
def get_inputs_by_tag(cls, collection: PCGDataCollection,
                      tag: str) -> Array[PCGTaggedData]
```

X.get_inputs_by_tag(collection, tag) -> Array[PCGTaggedData]
Get Inputs by Tag

Args:
    collection (PCGDataCollection): 
    tag (str): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.get_tagged_inputs"></a>

#### get_tagged_inputs

```python
@classmethod
def get_tagged_inputs(cls, collection: PCGDataCollection,
                      tag: str) -> Array[PCGTaggedData]
```

deprecated: 'get_tagged_inputs' was renamed to 'get_inputs_by_tag'.

<a id="unreal.PCGDataFunctionLibrary.get_inputs_by_pin_label"></a>

#### get_inputs_by_pin_label

```python
@classmethod
def get_inputs_by_pin_label(cls, collection: PCGDataCollection,
                            pin_label: Name) -> Array[PCGTaggedData]
```

X.get_inputs_by_pin_label(collection, pin_label) -> Array[PCGTaggedData]
Get Inputs by Pin Label

Args:
    collection (PCGDataCollection): 
    pin_label (Name): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.get_inputs_by_pin"></a>

#### get_inputs_by_pin

```python
@classmethod
def get_inputs_by_pin(cls, collection: PCGDataCollection,
                      pin_label: Name) -> Array[PCGTaggedData]
```

deprecated: 'get_inputs_by_pin' was renamed to 'get_inputs_by_pin_label'.

<a id="unreal.PCGDataFunctionLibrary.get_inputs"></a>

#### get_inputs

```python
@classmethod
def get_inputs(cls, collection: PCGDataCollection) -> Array[PCGTaggedData]
```

X.get_inputs(collection) -> Array[PCGTaggedData]
Blueprint methods to support interaction with FPCGDataCollection

Args:
    collection (PCGDataCollection): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.get_all_settings"></a>

#### get_all_settings

```python
@classmethod
def get_all_settings(cls,
                     collection: PCGDataCollection) -> Array[PCGTaggedData]
```

X.get_all_settings(collection) -> Array[PCGTaggedData]
Get All Settings

Args:
    collection (PCGDataCollection): 

Returns:
    Array[PCGTaggedData]:

<a id="unreal.PCGDataFunctionLibrary.add_to_collection"></a>

#### add_to_collection

```python
@classmethod
def add_to_collection(cls, collection: PCGDataCollection, data: PCGData,
                      pin_label: Name, tags: Array[str]) -> PCGDataCollection
```

X.add_to_collection(collection, data, pin_label, tags) -> PCGDataCollection
Adds a data object to a given collection, simpler usage than making a PCGTaggedData object. InTags can be empty.

Args:
    collection (PCGDataCollection): 
    data (PCGData): 
    pin_label (Name): 
    tags (Array[str]): 

Returns:
    PCGDataCollection: 

    collection (PCGDataCollection):

<a id="unreal.PCGGraphInterface"></a>