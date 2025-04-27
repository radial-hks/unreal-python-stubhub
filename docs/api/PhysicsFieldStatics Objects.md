## PhysicsFieldStatics Objects

```python
class PhysicsFieldStatics(BlueprintFunctionLibrary)
```

Static function with world field evaluation

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsFieldComponent.h

<a id="unreal.PhysicsFieldStatics.eval_physics_vector_field"></a>

#### eval_physics_vector_field

```python
@classmethod
def eval_physics_vector_field(cls, world_context_object: Object,
                              world_position: Vector,
                              vector_type: FieldVectorType) -> Vector
```

X.eval_physics_vector_field(world_context_object, world_position, vector_type) -> Vector
Evaluate the world physics vector field from BP

Args:
    world_context_object (Object): 
    world_position (Vector): 
    vector_type (FieldVectorType): 

Returns:
    Vector:

<a id="unreal.PhysicsFieldStatics.eval_physics_scalar_field"></a>

#### eval_physics_scalar_field

```python
@classmethod
def eval_physics_scalar_field(cls, world_context_object: Object,
                              world_position: Vector,
                              scalar_type: FieldScalarType) -> float
```

X.eval_physics_scalar_field(world_context_object, world_position, scalar_type) -> float
Evaluate the world physics scalar field from BP

Args:
    world_context_object (Object): 
    world_position (Vector): 
    scalar_type (FieldScalarType): 

Returns:
    float:

<a id="unreal.PhysicsFieldStatics.eval_physics_integer_field"></a>

#### eval_physics_integer_field

```python
@classmethod
def eval_physics_integer_field(cls, world_context_object: Object,
                               world_position: Vector,
                               integer_type: FieldIntegerType) -> int
```

X.eval_physics_integer_field(world_context_object, world_position, integer_type) -> int32
Evaluate the world physics integer field from BP

Args:
    world_context_object (Object): 
    world_position (Vector): 
    integer_type (FieldIntegerType): 

Returns:
    int32:

<a id="unreal.PlayerStart"></a>