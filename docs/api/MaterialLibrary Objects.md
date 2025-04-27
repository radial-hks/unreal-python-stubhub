## MaterialLibrary Objects

```python
class MaterialLibrary(BlueprintFunctionLibrary)
```

Kismet Material Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetMaterialLibrary.h

<a id="unreal.MaterialLibrary.set_vector_parameter_value"></a>

#### set_vector_parameter_value

```python
@classmethod
def set_vector_parameter_value(cls, world_context_object: Object,
                               collection: MaterialParameterCollection,
                               parameter_name: Name,
                               parameter_value: LinearColor) -> None
```

X.set_vector_parameter_value(world_context_object, collection, parameter_name, parameter_value) -> None
Sets a vector parameter value on the material collection instance. Logs if ParameterName is invalid.

Args:
    world_context_object (Object): 
    collection (MaterialParameterCollection): 
    parameter_name (Name): 
    parameter_value (LinearColor):

<a id="unreal.MaterialLibrary.set_scalar_parameter_value"></a>

#### set_scalar_parameter_value

```python
@classmethod
def set_scalar_parameter_value(cls, world_context_object: Object,
                               collection: MaterialParameterCollection,
                               parameter_name: Name,
                               parameter_value: float) -> None
```

X.set_scalar_parameter_value(world_context_object, collection, parameter_name, parameter_value) -> None
Sets a scalar parameter value on the material collection instance. Logs if ParameterName is invalid.

Args:
    world_context_object (Object): 
    collection (MaterialParameterCollection): 
    parameter_name (Name): 
    parameter_value (float):

<a id="unreal.MaterialLibrary.get_vector_parameter_value"></a>

#### get_vector_parameter_value

```python
@classmethod
def get_vector_parameter_value(cls, world_context_object: Object,
                               collection: MaterialParameterCollection,
                               parameter_name: Name) -> LinearColor
```

X.get_vector_parameter_value(world_context_object, collection, parameter_name) -> LinearColor
Gets a vector parameter value from the material collection instance. Logs if ParameterName is invalid.

Args:
    world_context_object (Object): 
    collection (MaterialParameterCollection): 
    parameter_name (Name): 

Returns:
    LinearColor:

<a id="unreal.MaterialLibrary.get_scalar_parameter_value"></a>

#### get_scalar_parameter_value

```python
@classmethod
def get_scalar_parameter_value(cls, world_context_object: Object,
                               collection: MaterialParameterCollection,
                               parameter_name: Name) -> float
```

X.get_scalar_parameter_value(world_context_object, collection, parameter_name) -> float
Gets a scalar parameter value from the material collection instance. Logs if ParameterName is invalid.

Args:
    world_context_object (Object): 
    collection (MaterialParameterCollection): 
    parameter_name (Name): 

Returns:
    float:

<a id="unreal.MaterialLibrary.create_dynamic_material_instance"></a>

#### create_dynamic_material_instance

```python
@classmethod
def create_dynamic_material_instance(
    cls,
    world_context_object: Object,
    parent: MaterialInterface,
    optional_name: Name = "None",
    creation_flags: MIDCreationFlags = MIDCreationFlags.NONE
) -> MaterialInstanceDynamic
```

X.create_dynamic_material_instance(world_context_object, parent, optional_name="None", creation_flags=MIDCreationFlags.NONE) -> MaterialInstanceDynamic
Creates a Dynamic Material Instance which you can modify during gameplay.

Args:
    world_context_object (Object): 
    parent (MaterialInterface): 
    optional_name (Name): 
    creation_flags (MIDCreationFlags): 

Returns:
    MaterialInstanceDynamic:

<a id="unreal.MaterialLibrary.create_material_instance_dynamic"></a>

#### create_material_instance_dynamic

```python
@classmethod
def create_material_instance_dynamic(
    cls,
    world_context_object: Object,
    parent: MaterialInterface,
    optional_name: Name = "None",
    creation_flags: MIDCreationFlags = MIDCreationFlags.NONE
) -> MaterialInstanceDynamic
```

deprecated: 'create_material_instance_dynamic' was renamed to 'create_dynamic_material_instance'.

<a id="unreal.MathLibrary"></a>