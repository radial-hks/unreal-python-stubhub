## OptimusDeformerInstance Objects

```python
class OptimusDeformerInstance(MeshDeformerInstance)
```

Class representing an instance of an Optimus Mesh Deformer, used in a OptimusDeformerDynamicInstanceManager
It contains the per instance deformer variable state and local state for each of the graphs in the deformer.

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusDeformerInstance.h

<a id="unreal.OptimusDeformerInstance.set_vector_variable"></a>

#### set_vector_variable

```python
def set_vector_variable(variable_name: Name, value: Vector) -> bool
```

x.set_vector_variable(variable_name, value) -> bool
Set Vector Variable

Args:
    variable_name (Name): 
    value (Vector): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_vector_array_variable"></a>

#### set_vector_array_variable

```python
def set_vector_array_variable(variable_name: Name,
                              value: Array[Vector]) -> bool
```

x.set_vector_array_variable(variable_name, value) -> bool
Set Vector Array Variable

Args:
    variable_name (Name): 
    value (Array[Vector]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_vector4_variable"></a>

#### set_vector4_variable

```python
def set_vector4_variable(variable_name: Name, value: Vector4) -> bool
```

x.set_vector4_variable(variable_name, value) -> bool
Set Vector 4Variable

Args:
    variable_name (Name): 
    value (Vector4): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_vector4_array_variable"></a>

#### set_vector4_array_variable

```python
def set_vector4_array_variable(variable_name: Name,
                               value: Array[Vector4]) -> bool
```

x.set_vector4_array_variable(variable_name, value) -> bool
Set Vector 4Array Variable

Args:
    variable_name (Name): 
    value (Array[Vector4]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_vector2_variable"></a>

#### set_vector2_variable

```python
def set_vector2_variable(variable_name: Name, value: Vector2D) -> bool
```

x.set_vector2_variable(variable_name, value) -> bool
Set Vector 2Variable

Args:
    variable_name (Name): 
    value (Vector2D): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_vector2_array_variable"></a>

#### set_vector2_array_variable

```python
def set_vector2_array_variable(variable_name: Name,
                               value: Array[Vector2D]) -> bool
```

x.set_vector2_array_variable(variable_name, value) -> bool
Set Vector 2Array Variable

Args:
    variable_name (Name): 
    value (Array[Vector2D]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_transform_variable"></a>

#### set_transform_variable

```python
def set_transform_variable(variable_name: Name, value: Transform) -> bool
```

x.set_transform_variable(variable_name, value) -> bool
Set the value of a transform variable.

Args:
    variable_name (Name): 
    value (Transform): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_transform_array_variable"></a>

#### set_transform_array_variable

```python
def set_transform_array_variable(variable_name: Name,
                                 value: Array[Transform]) -> bool
```

x.set_transform_array_variable(variable_name, value) -> bool
Set Transform Array Variable

Args:
    variable_name (Name): 
    value (Array[Transform]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_rotator_variable"></a>

#### set_rotator_variable

```python
def set_rotator_variable(variable_name: Name, value: Rotator) -> bool
```

x.set_rotator_variable(variable_name, value) -> bool
Set Rotator Variable

Args:
    variable_name (Name): 
    value (Rotator): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_rotator_array_variable"></a>

#### set_rotator_array_variable

```python
def set_rotator_array_variable(variable_name: Name,
                               value: Array[Rotator]) -> bool
```

x.set_rotator_array_variable(variable_name, value) -> bool
Set Rotator Array Variable

Args:
    variable_name (Name): 
    value (Array[Rotator]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_quat_variable"></a>

#### set_quat_variable

```python
def set_quat_variable(variable_name: Name, value: Quat) -> bool
```

x.set_quat_variable(variable_name, value) -> bool
Set Quat Variable

Args:
    variable_name (Name): 
    value (Quat): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_quat_array_variable"></a>

#### set_quat_array_variable

```python
def set_quat_array_variable(variable_name: Name, value: Array[Quat]) -> bool
```

x.set_quat_array_variable(variable_name, value) -> bool
Set Quat Array Variable

Args:
    variable_name (Name): 
    value (Array[Quat]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_name_variable"></a>

#### set_name_variable

```python
def set_name_variable(variable_name: Name, value: Name) -> bool
```

x.set_name_variable(variable_name, value) -> bool
Set Name Variable

Args:
    variable_name (Name): 
    value (Name): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_name_array_variable"></a>

#### set_name_array_variable

```python
def set_name_array_variable(variable_name: Name, value: Array[Name]) -> bool
```

x.set_name_array_variable(variable_name, value) -> bool
Set Name Array Variable

Args:
    variable_name (Name): 
    value (Array[Name]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_linear_color_variable"></a>

#### set_linear_color_variable

```python
def set_linear_color_variable(variable_name: Name, value: LinearColor) -> bool
```

x.set_linear_color_variable(variable_name, value) -> bool
Set Linear Color Variable

Args:
    variable_name (Name): 
    value (LinearColor): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_linear_color_array_variable"></a>

#### set_linear_color_array_variable

```python
def set_linear_color_array_variable(variable_name: Name,
                                    value: Array[LinearColor]) -> bool
```

x.set_linear_color_array_variable(variable_name, value) -> bool
Set Linear Color Array Variable

Args:
    variable_name (Name): 
    value (Array[LinearColor]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int_variable"></a>

#### set_int_variable

```python
def set_int_variable(variable_name: Name, value: int) -> bool
```

x.set_int_variable(variable_name, value) -> bool
Set the value of an integer variable.

Args:
    variable_name (Name): 
    value (int32): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int_array_variable"></a>

#### set_int_array_variable

```python
def set_int_array_variable(variable_name: Name, value: Array[int]) -> bool
```

x.set_int_array_variable(variable_name, value) -> bool
Set Int Array Variable

Args:
    variable_name (Name): 
    value (Array[int32]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int4_variable"></a>

#### set_int4_variable

```python
def set_int4_variable(variable_name: Name, value: IntVector4) -> bool
```

x.set_int4_variable(variable_name, value) -> bool
Set Int 4Variable

Args:
    variable_name (Name): 
    value (IntVector4): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int4_array_variable"></a>

#### set_int4_array_variable

```python
def set_int4_array_variable(variable_name: Name,
                            value: Array[IntVector4]) -> bool
```

x.set_int4_array_variable(variable_name, value) -> bool
Set Int 4Array Variable

Args:
    variable_name (Name): 
    value (Array[IntVector4]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int3_variable"></a>

#### set_int3_variable

```python
def set_int3_variable(variable_name: Name, value: IntVector) -> bool
```

x.set_int3_variable(variable_name, value) -> bool
Set Int 3Variable

Args:
    variable_name (Name): 
    value (IntVector): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int3_array_variable"></a>

#### set_int3_array_variable

```python
def set_int3_array_variable(variable_name: Name,
                            value: Array[IntVector]) -> bool
```

x.set_int3_array_variable(variable_name, value) -> bool
Set Int 3Array Variable

Args:
    variable_name (Name): 
    value (Array[IntVector]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int2_variable"></a>

#### set_int2_variable

```python
def set_int2_variable(variable_name: Name, value: IntPoint) -> bool
```

x.set_int2_variable(variable_name, value) -> bool
Set Int 2Variable

Args:
    variable_name (Name): 
    value (IntPoint): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_int2_array_variable"></a>

#### set_int2_array_variable

```python
def set_int2_array_variable(variable_name: Name,
                            value: Array[IntPoint]) -> bool
```

x.set_int2_array_variable(variable_name, value) -> bool
Set Int 2Array Variable

Args:
    variable_name (Name): 
    value (Array[IntPoint]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_float_variable"></a>

#### set_float_variable

```python
def set_float_variable(variable_name: Name, value: float) -> bool
```

x.set_float_variable(variable_name, value) -> bool
Set Float Variable

Args:
    variable_name (Name): 
    value (double): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_float_array_variable"></a>

#### set_float_array_variable

```python
def set_float_array_variable(variable_name: Name, value: Array[float]) -> bool
```

x.set_float_array_variable(variable_name, value) -> bool
Set Float Array Variable

Args:
    variable_name (Name): 
    value (Array[double]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_bool_variable"></a>

#### set_bool_variable

```python
def set_bool_variable(variable_name: Name, value: bool) -> bool
```

x.set_bool_variable(variable_name, value) -> bool
Set the value of a boolean variable.

Args:
    variable_name (Name): 
    value (bool): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.set_bool_array_variable"></a>

#### set_bool_array_variable

```python
def set_bool_array_variable(variable_name: Name, value: Array[bool]) -> bool
```

x.set_bool_array_variable(variable_name, value) -> bool
Set Bool Array Variable

Args:
    variable_name (Name): 
    value (Array[bool]): 

Returns:
    bool:

<a id="unreal.OptimusDeformerInstance.enqueue_trigger_graph"></a>

#### enqueue_trigger_graph

```python
def enqueue_trigger_graph(trigger_graph_name: Name) -> bool
```

x.enqueue_trigger_graph(trigger_graph_name) -> bool
Trigger a named trigger graph to run on the next tick

Args:
    trigger_graph_name (Name): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph"></a>