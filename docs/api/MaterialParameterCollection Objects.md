## MaterialParameterCollection Objects

```python
class MaterialParameterCollection(Object)
```

Asset class that contains a list of parameter names and their default values.
Any number of materials can reference these parameters and get new values when the parameter values are changed.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialParameterCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scalar_parameters`` (Array[CollectionScalarParameter]):  [Read-Write]
- ``vector_parameters`` (Array[CollectionVectorParameter]):  [Read-Write]

<a id="unreal.MaterialParameterCollection.get_vector_parameter_names"></a>

#### get_vector_parameter_names

```python
def get_vector_parameter_names() -> Array[Name]
```

x.get_vector_parameter_names() -> Array[Name]
Returns an array of the names of all the vector parameters in this Material Parameter Collection *

Returns:
    Array[Name]:

<a id="unreal.MaterialParameterCollection.get_vector_parameter_default_value"></a>

#### get_vector_parameter_default_value

```python
def get_vector_parameter_default_value(
        parameter_name: Name) -> Tuple[LinearColor, bool]
```

x.get_vector_parameter_default_value(parameter_name) -> (LinearColor, parameter_found=bool)
Gets the default value of a scalar parameter from a material collection.

Args:
    parameter_name (Name): The name of the value to get the value of

Returns:
    bool: the value of the parameter

    parameter_found (bool): if a parameter with the input name was found

<a id="unreal.MaterialParameterCollection.get_scalar_parameter_names"></a>

#### get_scalar_parameter_names

```python
def get_scalar_parameter_names() -> Array[Name]
```

x.get_scalar_parameter_names() -> Array[Name]
Returns an array of the names of all the scalar parameters in this Material Parameter Collection *

Returns:
    Array[Name]:

<a id="unreal.MaterialParameterCollection.get_scalar_parameter_default_value"></a>

#### get_scalar_parameter_default_value

```python
def get_scalar_parameter_default_value(
        parameter_name: Name) -> Tuple[float, bool]
```

x.get_scalar_parameter_default_value(parameter_name) -> (float, parameter_found=bool)
Gets the default value of a scalar parameter from a material collection.

Args:
    parameter_name (Name): The name of the value to get the value of

Returns:
    bool: the value of the parameter

    parameter_found (bool): if a parameter with the input name was found

<a id="unreal.MeshMergeCullingVolume"></a>