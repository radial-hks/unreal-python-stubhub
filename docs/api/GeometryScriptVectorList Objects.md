## GeometryScriptVectorList Objects

```python
class GeometryScriptVectorList(StructBase)
```

Geometry Script Vector List

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptVectorList.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptVectorList.set_vector_list_item"></a>

#### set_vector_list_item

```python
def set_vector_list_item(index: int, new_value: Vector) -> bool
```

x.set_vector_list_item(index, new_value) -> bool
Updates the value of the FVector stored in the Vector List at the specified location.
If the Index is invalid, the operation will fail and bValidIndex will be set to false.

Args:
    index (int32): 
    new_value (Vector): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptVectorList.get_vector_list_length"></a>

#### get_vector_list_length

```python
def get_vector_list_length() -> int
```

x.get_vector_list_length() -> int32
Returns the number of items in the Vector List.

Returns:
    int32:

<a id="unreal.GeometryScriptVectorList.get_vector_list_last_index"></a>

#### get_vector_list_last_index

```python
def get_vector_list_last_index() -> int
```

x.get_vector_list_last_index() -> int32
Returns the index of the last item in the Vector List.
If Vector List is empty or invalid, the value -1 will be returned.

Returns:
    int32:

<a id="unreal.GeometryScriptVectorList.get_vector_list_item"></a>

#### get_vector_list_item

```python
def get_vector_list_item(index: int) -> Tuple[Vector, bool]
```

x.get_vector_list_item(index) -> (Vector, is_valid_index=bool)
Returns the FVector stored in the VectorList at the specified location.
if the Index is not valid for this Vector List, the Zero Vector will be returned and bIsValidIndex set to false.

Args:
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptVectorList.duplicate_vector_list"></a>

#### duplicate_vector_list

```python
def duplicate_vector_list() -> GeometryScriptVectorList
```

x.duplicate_vector_list() -> GeometryScriptVectorList
Copies the contents of Vector List into Duplicate Vector List.

Returns:
    GeometryScriptVectorList: 

    duplicate_list (GeometryScriptVectorList):

<a id="unreal.GeometryScriptVectorList.convert_vector_list_to_array"></a>

#### convert_vector_list_to_array

```python
def convert_vector_list_to_array() -> Array[Vector]
```

x.convert_vector_list_to_array() -> Array[Vector]
Converts Vector List to an array of FVectors (Vector Array).

Returns:
    Array[Vector]: 

    vector_array (Array[Vector]):

<a id="unreal.GeometryScriptVectorList.clear_vector_list"></a>

#### clear_vector_list

```python
def clear_vector_list(
        clear_value: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

x.clear_vector_list(clear_value=[0.000000, 0.000000, 0.000000]) -> None
Resets all the items in the Vector List to the Clear Value.

Args:
    clear_value (Vector):

<a id="unreal.GeometryScriptVectorList.vector_transform_in_place"></a>

#### vector_transform_in_place

```python
def vector_transform_in_place(transform: Transform,
                              as_position: bool = True) -> None
```

x.vector_transform_in_place(transform, as_position=True) -> None
Transform each vector in VectorList, and store in VectorList.

Args:
    transform (Transform): 
    as_position (bool): Whether to treat input as positions or vectors (if vectors, will ignore the Transform's translation part)

<a id="unreal.GeometryScriptVectorList.vector_to_scalar"></a>

#### vector_to_scalar

```python
def vector_to_scalar(constant_x: float = 1.000000,
                     constant_y: float = 0.000000,
                     constant_z: float = 0.000000) -> GeometryScriptScalarList
```

x.vector_to_scalar(constant_x=1.000000, constant_y=0.000000, constant_z=0.000000) -> GeometryScriptScalarList
Convert each Vector in VectorList to a Scalar by computing (ConstantX*Vector.X + ConstantY*Vector.Y + ConstantZ*Vector.Z), and return in a new ScalarList.
This can be used to extract the X/Y/Z values from a Vector, or other component-wise math

Args:
    constant_x (double): 
    constant_y (double): 
    constant_z (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScriptVectorList.vector_plane_project_in_place"></a>

#### vector_plane_project_in_place

```python
def vector_plane_project_in_place(plane: Plane) -> None
```

x.vector_plane_project_in_place(plane) -> None
Project each vector in VectorList to the given Plane, and store in VectorList.

Args:
    plane (Plane):

<a id="unreal.GeometryScriptVectorList.vector_normalize_in_place"></a>

#### vector_normalize_in_place

```python
def vector_normalize_in_place(
        set_on_failure: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

x.vector_normalize_in_place(set_on_failure=[0.000000, 0.000000, 0.000000]) -> None
Normalize each vector in VectorList, and store in VectorList.
If a vector is degenerate, set the normal to the SetOnFailure vector.

Args:
    set_on_failure (Vector):

<a id="unreal.GeometryScriptVectorList.vector_length"></a>

#### vector_length

```python
def vector_length() -> GeometryScriptScalarList
```

x.vector_length() -> GeometryScriptScalarList
Compute the length/magnitude of each vector in VectorListA and return in new ScalarList.
Note that SquaredLength can be computed using VectorDot(A,A).

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScriptVectorList.vector_inverse_transform_in_place"></a>

#### vector_inverse_transform_in_place

```python
def vector_inverse_transform_in_place(transform: Transform,
                                      as_position: bool = True) -> None
```

x.vector_inverse_transform_in_place(transform, as_position=True) -> None
Inverse transform each vector in VectorList, and store in VectorList.

Args:
    transform (Transform): 
    as_position (bool): Whether to treat input as positions or vectors (if vectors, will ignore the Transform's translation part)

<a id="unreal.GeometryScriptVectorList.vector_dot"></a>

#### vector_dot

```python
def vector_dot(
        vector_list_b: GeometryScriptVectorList) -> GeometryScriptScalarList
```

x.vector_dot(vector_list_b) -> GeometryScriptScalarList
Compute the dot-product between each pair of vectors in VectorListA and VectorListB and return in new ScalarList

Args:
    vector_list_b (GeometryScriptVectorList): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScriptVectorList.vector_cross"></a>

#### vector_cross

```python
def vector_cross(
        vector_list_b: GeometryScriptVectorList) -> GeometryScriptVectorList
```

x.vector_cross(vector_list_b) -> GeometryScriptVectorList
Compute the cross-product between each pair of vectors in VectorListA and VectorListB and return in new VectorList

Args:
    vector_list_b (GeometryScriptVectorList): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScriptVectorList.vector_blend_in_place"></a>

#### vector_blend_in_place

```python
def vector_blend_in_place(
        vector_list_b: GeometryScriptVectorList,
        constant_a: float = 1.000000,
        constant_b: float = 1.000000) -> GeometryScriptVectorList
```

x.vector_blend_in_place(vector_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptVectorList
Compute (ConstantA * A) + (ConstantB * B) for each pair of vectors in VectorListA and VectorListB, and store in VectorListB
By default (constants = 1) this just adds the two vectors. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    vector_list_b (GeometryScriptVectorList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptVectorList: 

    vector_list_b (GeometryScriptVectorList):

<a id="unreal.GeometryScriptVectorList.vector_blend"></a>

#### vector_blend

```python
def vector_blend(vector_list_b: GeometryScriptVectorList,
                 constant_a: float = 1.000000,
                 constant_b: float = 1.000000) -> GeometryScriptVectorList
```

x.vector_blend(vector_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptVectorList
Compute (ConstantA * A) + (ConstantB * B) for each pair of vectors in VectorListA and VectorListB and return in new VectorList.
By default (constants = 1) this just adds the two vectors. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    vector_list_b (GeometryScriptVectorList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScriptUVList"></a>