## NiagaraParameterCollectionInstance Objects

```python
class NiagaraParameterCollectionInstance(Object)
```

Can be used to override selected parameters from a Niagara parameter collection with another value.
The values in the parameter collection instance can be set from Blueprint or C++, same as the regular parameter collection.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraParameterCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (NiagaraParameterCollection):  [Read-Write] TODO: Abstract to some interface to allow a hierarchy like UMaterialInstance?

<a id="unreal.NiagaraParameterCollectionInstance.set_vector_parameter"></a>

#### set_vector_parameter

```python
def set_vector_parameter(variable_name: str, value: Vector) -> None
```

x.set_vector_parameter(variable_name, value) -> None
Set Vector Parameter

Args:
    variable_name (str): 
    value (Vector):

<a id="unreal.NiagaraParameterCollectionInstance.set_vector4_parameter"></a>

#### set_vector4_parameter

```python
def set_vector4_parameter(variable_name: str, value: Vector4) -> None
```

x.set_vector4_parameter(variable_name, value) -> None
TODO[mg]: add position setter for LWC

Args:
    variable_name (str): 
    value (Vector4):

<a id="unreal.NiagaraParameterCollectionInstance.set_vector2d_parameter"></a>

#### set_vector2d_parameter

```python
def set_vector2d_parameter(variable_name: str, value: Vector2D) -> None
```

x.set_vector2d_parameter(variable_name, value) -> None
Set Vector 2DParameter

Args:
    variable_name (str): 
    value (Vector2D):

<a id="unreal.NiagaraParameterCollectionInstance.set_quat_parameter"></a>

#### set_quat_parameter

```python
def set_quat_parameter(variable_name: str, value: Quat) -> None
```

x.set_quat_parameter(variable_name, value) -> None
Set Quat Parameter

Args:
    variable_name (str): 
    value (Quat):

<a id="unreal.NiagaraParameterCollectionInstance.set_int_parameter"></a>

#### set_int_parameter

```python
def set_int_parameter(variable_name: str, value: int) -> None
```

x.set_int_parameter(variable_name, value) -> None
Set Int Parameter

Args:
    variable_name (str): 
    value (int32):

<a id="unreal.NiagaraParameterCollectionInstance.set_float_parameter"></a>

#### set_float_parameter

```python
def set_float_parameter(variable_name: str, value: float) -> None
```

x.set_float_parameter(variable_name, value) -> None
Set Float Parameter

Args:
    variable_name (str): 
    value (float):

<a id="unreal.NiagaraParameterCollectionInstance.set_color_parameter"></a>

#### set_color_parameter

```python
def set_color_parameter(variable_name: str, value: LinearColor) -> None
```

x.set_color_parameter(variable_name, value) -> None
Set Color Parameter

Args:
    variable_name (str): 
    value (LinearColor):

<a id="unreal.NiagaraParameterCollectionInstance.set_bool_parameter"></a>

#### set_bool_parameter

```python
def set_bool_parameter(variable_name: str, value: bool) -> None
```

x.set_bool_parameter(variable_name, value) -> None
Set Bool Parameter

Args:
    variable_name (str): 
    value (bool):

<a id="unreal.NiagaraParameterCollectionInstance.get_vector_parameter"></a>

#### get_vector_parameter

```python
def get_vector_parameter(variable_name: str) -> Vector
```

x.get_vector_parameter(variable_name) -> Vector
Get Vector Parameter

Args:
    variable_name (str): 

Returns:
    Vector:

<a id="unreal.NiagaraParameterCollectionInstance.get_vector4_parameter"></a>

#### get_vector4_parameter

```python
def get_vector4_parameter(variable_name: str) -> Vector4
```

x.get_vector4_parameter(variable_name) -> Vector4
Get Vector 4Parameter

Args:
    variable_name (str): 

Returns:
    Vector4:

<a id="unreal.NiagaraParameterCollectionInstance.get_vector2d_parameter"></a>

#### get_vector2d_parameter

```python
def get_vector2d_parameter(variable_name: str) -> Vector2D
```

x.get_vector2d_parameter(variable_name) -> Vector2D
Get Vector 2DParameter

Args:
    variable_name (str): 

Returns:
    Vector2D:

<a id="unreal.NiagaraParameterCollectionInstance.get_quat_parameter"></a>

#### get_quat_parameter

```python
def get_quat_parameter(variable_name: str) -> Quat
```

x.get_quat_parameter(variable_name) -> Quat
Get Quat Parameter

Args:
    variable_name (str): 

Returns:
    Quat:

<a id="unreal.NiagaraParameterCollectionInstance.get_int_parameter"></a>

#### get_int_parameter

```python
def get_int_parameter(variable_name: str) -> int
```

x.get_int_parameter(variable_name) -> int32
Get Int Parameter

Args:
    variable_name (str): 

Returns:
    int32:

<a id="unreal.NiagaraParameterCollectionInstance.get_float_parameter"></a>

#### get_float_parameter

```python
def get_float_parameter(variable_name: str) -> float
```

x.get_float_parameter(variable_name) -> float
Get Float Parameter

Args:
    variable_name (str): 

Returns:
    float:

<a id="unreal.NiagaraParameterCollectionInstance.get_color_parameter"></a>

#### get_color_parameter

```python
def get_color_parameter(variable_name: str) -> LinearColor
```

x.get_color_parameter(variable_name) -> LinearColor
Get Color Parameter

Args:
    variable_name (str): 

Returns:
    LinearColor:

<a id="unreal.NiagaraParameterCollectionInstance.get_bool_parameter"></a>

#### get_bool_parameter

```python
def get_bool_parameter(variable_name: str) -> bool
```

x.get_bool_parameter(variable_name) -> bool
Accessors from Blueprint. For now just exposing common types but ideally we can expose any somehow in future.

Args:
    variable_name (str): 

Returns:
    bool:

<a id="unreal.NiagaraBaselineController"></a>