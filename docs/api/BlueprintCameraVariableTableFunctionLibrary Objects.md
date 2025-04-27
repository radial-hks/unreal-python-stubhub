## BlueprintCameraVariableTableFunctionLibrary Objects

```python
class BlueprintCameraVariableTableFunctionLibrary(BlueprintFunctionLibrary)
```

Utility Blueprint functions for camera variable tables.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraVariableTable.h

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_vector4_camera_variable"></a>

#### set_vector4_camera_variable

```python
@classmethod
def set_vector4_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Vector4dCameraVariable,
                                value: Vector4) -> None
```

X.set_vector4_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Vector4dCameraVariable): 
    value (Vector4):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_vector3_camera_variable"></a>

#### set_vector3_camera_variable

```python
@classmethod
def set_vector3_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Vector3dCameraVariable,
                                value: Vector) -> None
```

X.set_vector3_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Vector3dCameraVariable): 
    value (Vector):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_vector2_camera_variable"></a>

#### set_vector2_camera_variable

```python
@classmethod
def set_vector2_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Vector2dCameraVariable,
                                value: Vector2D) -> None
```

X.set_vector2_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Vector2dCameraVariable): 
    value (Vector2D):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_transform_camera_variable"></a>

#### set_transform_camera_variable

```python
@classmethod
def set_transform_camera_variable(cls,
                                  variable_table: BlueprintCameraVariableTable,
                                  variable: Transform3dCameraVariable,
                                  value: Transform) -> None
```

X.set_transform_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Transform3dCameraVariable): 
    value (Transform):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_rotator_camera_variable"></a>

#### set_rotator_camera_variable

```python
@classmethod
def set_rotator_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Rotator3dCameraVariable,
                                value: Rotator) -> None
```

X.set_rotator_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Rotator3dCameraVariable): 
    value (Rotator):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_integer32_camera_variable"></a>

#### set_integer32_camera_variable

```python
@classmethod
def set_integer32_camera_variable(cls,
                                  variable_table: BlueprintCameraVariableTable,
                                  variable: Integer32CameraVariable,
                                  value: int) -> None
```

X.set_integer32_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Integer32CameraVariable): 
    value (int32):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_float_camera_variable"></a>

#### set_float_camera_variable

```python
@classmethod
def set_float_camera_variable(cls,
                              variable_table: BlueprintCameraVariableTable,
                              variable: FloatCameraVariable,
                              value: float) -> None
```

X.set_float_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (FloatCameraVariable): 
    value (float):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_double_camera_variable"></a>

#### set_double_camera_variable

```python
@classmethod
def set_double_camera_variable(cls,
                               variable_table: BlueprintCameraVariableTable,
                               variable: DoubleCameraVariable,
                               value: float) -> None
```

X.set_double_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (DoubleCameraVariable): 
    value (double):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.set_boolean_camera_variable"></a>

#### set_boolean_camera_variable

```python
@classmethod
def set_boolean_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: BooleanCameraVariable,
                                value: bool) -> None
```

X.set_boolean_camera_variable(variable_table, variable, value) -> None
Sets a camera variable's value in the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (BooleanCameraVariable): 
    value (bool):

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_vector4_camera_variable"></a>

#### get_vector4_camera_variable

```python
@classmethod
def get_vector4_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Vector4dCameraVariable) -> Vector4
```

X.get_vector4_camera_variable(variable_table, variable) -> Vector4
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Vector4dCameraVariable): 

Returns:
    Vector4:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_vector3_camera_variable"></a>

#### get_vector3_camera_variable

```python
@classmethod
def get_vector3_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Vector3dCameraVariable) -> Vector
```

X.get_vector3_camera_variable(variable_table, variable) -> Vector
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Vector3dCameraVariable): 

Returns:
    Vector:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_vector2_camera_variable"></a>

#### get_vector2_camera_variable

```python
@classmethod
def get_vector2_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Vector2dCameraVariable) -> Vector2D
```

X.get_vector2_camera_variable(variable_table, variable) -> Vector2D
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Vector2dCameraVariable): 

Returns:
    Vector2D:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_transform_camera_variable"></a>

#### get_transform_camera_variable

```python
@classmethod
def get_transform_camera_variable(
        cls, variable_table: BlueprintCameraVariableTable,
        variable: Transform3dCameraVariable) -> Transform
```

X.get_transform_camera_variable(variable_table, variable) -> Transform
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Transform3dCameraVariable): 

Returns:
    Transform:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_rotator_camera_variable"></a>

#### get_rotator_camera_variable

```python
@classmethod
def get_rotator_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: Rotator3dCameraVariable) -> Rotator
```

X.get_rotator_camera_variable(variable_table, variable) -> Rotator
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Rotator3dCameraVariable): 

Returns:
    Rotator:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_integer32_camera_variable"></a>

#### get_integer32_camera_variable

```python
@classmethod
def get_integer32_camera_variable(cls,
                                  variable_table: BlueprintCameraVariableTable,
                                  variable: Integer32CameraVariable) -> int
```

X.get_integer32_camera_variable(variable_table, variable) -> int32
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (Integer32CameraVariable): 

Returns:
    int32:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_float_camera_variable"></a>

#### get_float_camera_variable

```python
@classmethod
def get_float_camera_variable(cls,
                              variable_table: BlueprintCameraVariableTable,
                              variable: FloatCameraVariable) -> float
```

X.get_float_camera_variable(variable_table, variable) -> float
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (FloatCameraVariable): 

Returns:
    float:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_double_camera_variable"></a>

#### get_double_camera_variable

```python
@classmethod
def get_double_camera_variable(cls,
                               variable_table: BlueprintCameraVariableTable,
                               variable: DoubleCameraVariable) -> float
```

X.get_double_camera_variable(variable_table, variable) -> double
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (DoubleCameraVariable): 

Returns:
    double:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary.get_boolean_camera_variable"></a>

#### get_boolean_camera_variable

```python
@classmethod
def get_boolean_camera_variable(cls,
                                variable_table: BlueprintCameraVariableTable,
                                variable: BooleanCameraVariable) -> bool
```

X.get_boolean_camera_variable(variable_table, variable) -> bool
Gets a camera variable's value from the given table.

Args:
    variable_table (BlueprintCameraVariableTable): 
    variable (BooleanCameraVariable): 

Returns:
    bool:

<a id="unreal.ControllerGameplayCameraEvaluationComponent"></a>