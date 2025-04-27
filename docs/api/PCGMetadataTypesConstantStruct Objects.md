## PCGMetadataTypesConstantStruct Objects

```python
class PCGMetadataTypesConstantStruct(StructBase)
```

Struct to be re-used when you need to show constants types for a metadata type
It will store all our values, and will display nicely depending on the type chosen

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadataTypesConstantStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_value`` (bool):  [Read-Write]
- ``double_value`` (double):  [Read-Write]
- ``float_value`` (float):  [Read-Write] All different types
- ``int32_value`` (int32):  [Read-Write]
- ``int_value`` (int64):  [Read-Write]
- ``name_value`` (Name):  [Read-Write]
- ``quat_value`` (Quat):  [Read-Write]
- ``rotator_value`` (Rotator):  [Read-Write]
- ``soft_class_path_value`` (SoftClassPath):  [Read-Write]
- ``soft_object_path_value`` (SoftObjectPath):  [Read-Write]
- ``string_value`` (str):  [Read-Write]
- ``transform_value`` (Transform):  [Read-Write]
- ``type`` (PCGMetadataTypes):  [Read-Write]
- ``vector2_value`` (Vector2D):  [Read-Write]
- ``vector4_value`` (Vector4):  [Read-Write]
- ``vector_value`` (Vector):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.__init__"></a>

#### __init__

```python
def __init__(type: PCGMetadataTypes = PCGMetadataTypes.FLOAT,
             float_value: float = 0.000000,
             int32_value: int = 0,
             double_value: float = 0.000000,
             int_value: int = 0,
             vector2_value: Vector2D = [0.000000, 0.000000],
             vector_value: Vector = [0.000000, 0.000000, 0.000000],
             vector4_value: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
             quat_value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             transform_value: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             string_value: str = "",
             bool_value: bool = False,
             rotator_value: Rotator = [0.000000, 0.000000, 0.000000],
             name_value: Name = "None",
             soft_class_path_value: SoftClassPath = [""],
             soft_object_path_value: SoftObjectPath = [""]) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.type"></a>

#### type

```python
@property
def type() -> PCGMetadataTypes
```

(PCGMetadataTypes):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.type"></a>

#### type

```python
@type.setter
def type(value: PCGMetadataTypes) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.float_value"></a>

#### float_value

```python
@property
def float_value() -> float
```

(float):  [Read-Write] All different types

<a id="unreal.PCGMetadataTypesConstantStruct.float_value"></a>

#### float_value

```python
@float_value.setter
def float_value(value: float) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.int32_value"></a>

#### int32_value

```python
@property
def int32_value() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.int32_value"></a>

#### int32_value

```python
@int32_value.setter
def int32_value(value: int) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.double_value"></a>

#### double_value

```python
@property
def double_value() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.double_value"></a>

#### double_value

```python
@double_value.setter
def double_value(value: float) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.int_value"></a>

#### int_value

```python
@property
def int_value() -> int
```

(int64):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.int_value"></a>

#### int_value

```python
@int_value.setter
def int_value(value: int) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.vector2_value"></a>

#### vector2_value

```python
@property
def vector2_value() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.vector2_value"></a>

#### vector2_value

```python
@vector2_value.setter
def vector2_value(value: Vector2D) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.vector_value"></a>

#### vector_value

```python
@property
def vector_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.vector_value"></a>

#### vector_value

```python
@vector_value.setter
def vector_value(value: Vector) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.vector4_value"></a>

#### vector4_value

```python
@property
def vector4_value() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.vector4_value"></a>

#### vector4_value

```python
@vector4_value.setter
def vector4_value(value: Vector4) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.quat_value"></a>

#### quat_value

```python
@property
def quat_value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.quat_value"></a>

#### quat_value

```python
@quat_value.setter
def quat_value(value: Quat) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.transform_value"></a>

#### transform_value

```python
@property
def transform_value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.transform_value"></a>

#### transform_value

```python
@transform_value.setter
def transform_value(value: Transform) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.string_value"></a>

#### string_value

```python
@property
def string_value() -> str
```

(str):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.string_value"></a>

#### string_value

```python
@string_value.setter
def string_value(value: str) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.bool_value"></a>

#### bool_value

```python
@property
def bool_value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.bool_value"></a>

#### bool_value

```python
@bool_value.setter
def bool_value(value: bool) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.rotator_value"></a>

#### rotator_value

```python
@property
def rotator_value() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.rotator_value"></a>

#### rotator_value

```python
@rotator_value.setter
def rotator_value(value: Rotator) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.name_value"></a>

#### name_value

```python
@property
def name_value() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.name_value"></a>

#### name_value

```python
@name_value.setter
def name_value(value: Name) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.soft_class_path_value"></a>

#### soft_class_path_value

```python
@property
def soft_class_path_value() -> SoftClassPath
```

(SoftClassPath):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.soft_class_path_value"></a>

#### soft_class_path_value

```python
@soft_class_path_value.setter
def soft_class_path_value(value: SoftClassPath) -> None
```

<a id="unreal.PCGMetadataTypesConstantStruct.soft_object_path_value"></a>

#### soft_object_path_value

```python
@property
def soft_object_path_value() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]

<a id="unreal.PCGMetadataTypesConstantStruct.soft_object_path_value"></a>

#### soft_object_path_value

```python
@soft_object_path_value.setter
def soft_object_path_value(value: SoftObjectPath) -> None
```

<a id="unreal.PCGAttributePropertySelector"></a>