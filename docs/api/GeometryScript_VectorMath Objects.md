## GeometryScript_VectorMath Objects

```python
class GeometryScript_VectorMath(BlueprintFunctionLibrary)
```

Geometry Script Library Vector Math Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: VectorMathFunctions.h

<a id="unreal.GeometryScript_VectorMath.vector_transform_in_place"></a>

#### vector_transform_in_place

```python
@classmethod
def vector_transform_in_place(
        cls,
        vector_list: GeometryScriptVectorList,
        transform: Transform,
        as_position: bool = True) -> GeometryScriptVectorList
```

X.vector_transform_in_place(vector_list, transform, as_position=True) -> GeometryScriptVectorList
Transform each vector in VectorList, and store in VectorList.

Args:
    vector_list (GeometryScriptVectorList): 
    transform (Transform): 
    as_position (bool): Whether to treat input as positions or vectors (if vectors, will ignore the Transform's translation part)

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.vector_to_scalar"></a>

#### vector_to_scalar

```python
@classmethod
def vector_to_scalar(cls,
                     vector_list: GeometryScriptVectorList,
                     constant_x: float = 1.000000,
                     constant_y: float = 0.000000,
                     constant_z: float = 0.000000) -> GeometryScriptScalarList
```

X.vector_to_scalar(vector_list, constant_x=1.000000, constant_y=0.000000, constant_z=0.000000) -> GeometryScriptScalarList
Convert each Vector in VectorList to a Scalar by computing (ConstantX*Vector.X + ConstantY*Vector.Y + ConstantZ*Vector.Z), and return in a new ScalarList.
This can be used to extract the X/Y/Z values from a Vector, or other component-wise math

Args:
    vector_list (GeometryScriptVectorList): 
    constant_x (double): 
    constant_y (double): 
    constant_z (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VectorMath.vector_plane_project_in_place"></a>

#### vector_plane_project_in_place

```python
@classmethod
def vector_plane_project_in_place(cls, vector_list: GeometryScriptVectorList,
                                  plane: Plane) -> GeometryScriptVectorList
```

X.vector_plane_project_in_place(vector_list, plane) -> GeometryScriptVectorList
Project each vector in VectorList to the given Plane, and store in VectorList.

Args:
    vector_list (GeometryScriptVectorList): 
    plane (Plane): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.vector_normalize_in_place"></a>

#### vector_normalize_in_place

```python
@classmethod
def vector_normalize_in_place(
    cls,
    vector_list: GeometryScriptVectorList,
    set_on_failure: Vector = [0.000000, 0.000000, 0.000000]
) -> GeometryScriptVectorList
```

X.vector_normalize_in_place(vector_list, set_on_failure=[0.000000, 0.000000, 0.000000]) -> GeometryScriptVectorList
Normalize each vector in VectorList, and store in VectorList.
If a vector is degenerate, set the normal to the SetOnFailure vector.

Args:
    vector_list (GeometryScriptVectorList): 
    set_on_failure (Vector): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.vector_length"></a>

#### vector_length

```python
@classmethod
def vector_length(
        cls,
        vector_list: GeometryScriptVectorList) -> GeometryScriptScalarList
```

X.vector_length(vector_list) -> GeometryScriptScalarList
Compute the length/magnitude of each vector in VectorListA and return in new ScalarList.
Note that SquaredLength can be computed using VectorDot(A,A).

Args:
    vector_list (GeometryScriptVectorList): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VectorMath.vector_inverse_transform_in_place"></a>

#### vector_inverse_transform_in_place

```python
@classmethod
def vector_inverse_transform_in_place(
        cls,
        vector_list: GeometryScriptVectorList,
        transform: Transform,
        as_position: bool = True) -> GeometryScriptVectorList
```

X.vector_inverse_transform_in_place(vector_list, transform, as_position=True) -> GeometryScriptVectorList
Inverse transform each vector in VectorList, and store in VectorList.

Args:
    vector_list (GeometryScriptVectorList): 
    transform (Transform): 
    as_position (bool): Whether to treat input as positions or vectors (if vectors, will ignore the Transform's translation part)

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.vector_dot"></a>

#### vector_dot

```python
@classmethod
def vector_dot(
        cls, vector_list_a: GeometryScriptVectorList,
        vector_list_b: GeometryScriptVectorList) -> GeometryScriptScalarList
```

X.vector_dot(vector_list_a, vector_list_b) -> GeometryScriptScalarList
Compute the dot-product between each pair of vectors in VectorListA and VectorListB and return in new ScalarList

Args:
    vector_list_a (GeometryScriptVectorList): 
    vector_list_b (GeometryScriptVectorList): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VectorMath.vector_cross"></a>

#### vector_cross

```python
@classmethod
def vector_cross(
        cls, vector_list_a: GeometryScriptVectorList,
        vector_list_b: GeometryScriptVectorList) -> GeometryScriptVectorList
```

X.vector_cross(vector_list_a, vector_list_b) -> GeometryScriptVectorList
Compute the cross-product between each pair of vectors in VectorListA and VectorListB and return in new VectorList

Args:
    vector_list_a (GeometryScriptVectorList): 
    vector_list_b (GeometryScriptVectorList): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScript_VectorMath.vector_blend_in_place"></a>

#### vector_blend_in_place

```python
@classmethod
def vector_blend_in_place(
        cls,
        vector_list_a: GeometryScriptVectorList,
        vector_list_b: GeometryScriptVectorList,
        constant_a: float = 1.000000,
        constant_b: float = 1.000000) -> GeometryScriptVectorList
```

X.vector_blend_in_place(vector_list_a, vector_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptVectorList
Compute (ConstantA * A) + (ConstantB * B) for each pair of vectors in VectorListA and VectorListB, and store in VectorListB
By default (constants = 1) this just adds the two vectors. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    vector_list_a (GeometryScriptVectorList): 
    vector_list_b (GeometryScriptVectorList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptVectorList: 

    vector_list_b (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.vector_blend"></a>

#### vector_blend

```python
@classmethod
def vector_blend(cls,
                 vector_list_a: GeometryScriptVectorList,
                 vector_list_b: GeometryScriptVectorList,
                 constant_a: float = 1.000000,
                 constant_b: float = 1.000000) -> GeometryScriptVectorList
```

X.vector_blend(vector_list_a, vector_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptVectorList
Compute (ConstantA * A) + (ConstantB * B) for each pair of vectors in VectorListA and VectorListB and return in new VectorList.
By default (constants = 1) this just adds the two vectors. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    vector_list_a (GeometryScriptVectorList): 
    vector_list_b (GeometryScriptVectorList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScript_VectorMath.scalar_vector_multiply_in_place"></a>

#### scalar_vector_multiply_in_place

```python
@classmethod
def scalar_vector_multiply_in_place(
        cls,
        scalar_list: GeometryScriptScalarList,
        vector_list: GeometryScriptVectorList,
        scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
```

X.scalar_vector_multiply_in_place(scalar_list, vector_list, scalar_multiplier=1.000000) -> GeometryScriptVectorList
Compute (ScalarMultiplier * Scalar * Vector) for each scalar/vector pair in the two input lists, and store in the input VectorList

Args:
    scalar_list (GeometryScriptScalarList): 
    vector_list (GeometryScriptVectorList): 
    scalar_multiplier (double): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.scalar_vector_multiply"></a>

#### scalar_vector_multiply

```python
@classmethod
def scalar_vector_multiply(
        cls,
        scalar_list: GeometryScriptScalarList,
        vector_list: GeometryScriptVectorList,
        scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
```

X.scalar_vector_multiply(scalar_list, vector_list, scalar_multiplier=1.000000) -> GeometryScriptVectorList
Compute (ScalarMultiplier * Scalar * Vector) for each scalar/vector pair in the two input lists, and return in a new VectorList.

Args:
    scalar_list (GeometryScriptScalarList): 
    vector_list (GeometryScriptVectorList): 
    scalar_multiplier (double): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScript_VectorMath.scalar_multiply_in_place"></a>

#### scalar_multiply_in_place

```python
@classmethod
def scalar_multiply_in_place(
        cls,
        scalar_list_a: GeometryScriptScalarList,
        scalar_list_b: GeometryScriptScalarList,
        constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
```

X.scalar_multiply_in_place(scalar_list_a, scalar_list_b, constant_multiplier=1.000000) -> GeometryScriptScalarList
Compute (ConstantMultiplier * A * B)  where A and B are the corresponding elements from ScalarListA and ScalarListB accordingly, and store the
result in ScalarListA.
If ScalarListA and ScalarListB have different lengths, the computation will be skipped.

Args:
    scalar_list_a (GeometryScriptScalarList): 
    scalar_list_b (GeometryScriptScalarList): 
    constant_multiplier (double): 

Returns:
    GeometryScriptScalarList: 

    scalar_list_b (GeometryScriptScalarList):

<a id="unreal.GeometryScript_VectorMath.scalar_multiply"></a>

#### scalar_multiply

```python
@classmethod
def scalar_multiply(
        cls,
        scalar_list_a: GeometryScriptScalarList,
        scalar_list_b: GeometryScriptScalarList,
        constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
```

X.scalar_multiply(scalar_list_a, scalar_list_b, constant_multiplier=1.000000) -> GeometryScriptScalarList
Returns a Scalar List constructed with each element is the product (ConstantMultiplier * A * B)
where A and B are the corresponding elements from ScalarListA and ScalarListB accordingly.
If ScalarListA and ScalarListB have different lengths, no operation will be performed and an empty Scalar List will be returned.

Args:
    scalar_list_a (GeometryScriptScalarList): 
    scalar_list_b (GeometryScriptScalarList): 
    constant_multiplier (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VectorMath.scalar_invert_in_place"></a>

#### scalar_invert_in_place

```python
@classmethod
def scalar_invert_in_place(
        cls,
        scalar_list: GeometryScriptScalarList,
        numerator: float = 1.000000,
        set_on_failure: float = 0.000000,
        epsilon: float = 0.000000) -> GeometryScriptScalarList
```

X.scalar_invert_in_place(scalar_list, numerator=1.000000, set_on_failure=0.000000, epsilon=0.000000) -> GeometryScriptScalarList
Compute (Numerator / Scalar) for each element of ScalarList and store in input ScalarList
If Abs(Scalar) < Epsilon, set to SetOnFailure value.

Args:
    scalar_list (GeometryScriptScalarList): 
    numerator (double): 
    set_on_failure (double): 
    epsilon (double): 

Returns:
    GeometryScriptScalarList: 

    scalar_list (GeometryScriptScalarList):

<a id="unreal.GeometryScript_VectorMath.scalar_invert"></a>

#### scalar_invert

```python
@classmethod
def scalar_invert(cls,
                  scalar_list: GeometryScriptScalarList,
                  numerator: float = 1.000000,
                  set_on_failure: float = 0.000000,
                  epsilon: float = 0.000000) -> GeometryScriptScalarList
```

X.scalar_invert(scalar_list, numerator=1.000000, set_on_failure=0.000000, epsilon=0.000000) -> GeometryScriptScalarList
Compute (Numerator / Scalar) for each element of ScalarList and return in a new ScalarList.
If Abs(Scalar) < Epsilon, set to SetOnFailure value.

Args:
    scalar_list (GeometryScriptScalarList): 
    numerator (double): 
    set_on_failure (double): 
    epsilon (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VectorMath.scalar_blend_in_place"></a>

#### scalar_blend_in_place

```python
@classmethod
def scalar_blend_in_place(
        cls,
        scalar_list_a: GeometryScriptScalarList,
        scalar_list_b: GeometryScriptScalarList,
        constant_a: float = 1.000000,
        constant_b: float = 1.000000) -> GeometryScriptScalarList
```

X.scalar_blend_in_place(scalar_list_a, scalar_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptScalarList
Compute (ConstantA * A) + (ConstantB * B) for each pair of values in ScalarListA and ScalarListB and return in ScalarListB.
By default (constants = 1) this just adds the two values. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    scalar_list_a (GeometryScriptScalarList): 
    scalar_list_b (GeometryScriptScalarList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptScalarList: 

    scalar_list_b (GeometryScriptScalarList):

<a id="unreal.GeometryScript_VectorMath.scalar_blend"></a>

#### scalar_blend

```python
@classmethod
def scalar_blend(cls,
                 scalar_list_a: GeometryScriptScalarList,
                 scalar_list_b: GeometryScriptScalarList,
                 constant_a: float = 1.000000,
                 constant_b: float = 1.000000) -> GeometryScriptScalarList
```

X.scalar_blend(scalar_list_a, scalar_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptScalarList
Compute (ConstantA * A) + (ConstantB * B) for each pair of values in ScalarListA and ScalarListB and return in new ScalarList.
By default (constants = 1) this just adds the two values. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    scalar_list_a (GeometryScriptScalarList): 
    scalar_list_b (GeometryScriptScalarList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VectorMath.constant_vector_multiply_in_place"></a>

#### constant_vector_multiply_in_place

```python
@classmethod
def constant_vector_multiply_in_place(
        cls, constant: float,
        vector_list: GeometryScriptVectorList) -> GeometryScriptVectorList
```

X.constant_vector_multiply_in_place(constant, vector_list) -> GeometryScriptVectorList
Compute (Constant * Vector) for each element in VectorList, and store in VectorList

Args:
    constant (double): 
    vector_list (GeometryScriptVectorList): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_VectorMath.constant_vector_multiply"></a>

#### constant_vector_multiply

```python
@classmethod
def constant_vector_multiply(
        cls, constant: float,
        vector_list: GeometryScriptVectorList) -> GeometryScriptVectorList
```

X.constant_vector_multiply(constant, vector_list) -> GeometryScriptVectorList
Compute (Constant * Vector) for each element in VectorList, and return in a new list

Args:
    constant (double): 
    vector_list (GeometryScriptVectorList): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScript_VectorMath.constant_scalar_multiply_in_place"></a>

#### constant_scalar_multiply_in_place

```python
@classmethod
def constant_scalar_multiply_in_place(
        cls, constant: float,
        scalar_list: GeometryScriptScalarList) -> GeometryScriptScalarList
```

X.constant_scalar_multiply_in_place(constant, scalar_list) -> GeometryScriptScalarList
Compute (Constant * A) for each element A is the Scalar List, and the result is stored in the original Scalar List.

Args:
    constant (double): 
    scalar_list (GeometryScriptScalarList): 

Returns:
    GeometryScriptScalarList: 

    scalar_list (GeometryScriptScalarList):

<a id="unreal.GeometryScript_VectorMath.constant_scalar_multiply"></a>

#### constant_scalar_multiply

```python
@classmethod
def constant_scalar_multiply(
        cls, constant: float,
        scalar_list: GeometryScriptScalarList) -> GeometryScriptScalarList
```

X.constant_scalar_multiply(constant, scalar_list) -> GeometryScriptScalarList
Returns a Scalar List of the same length as the input Scalar List, with the elements computed as (Constant * A) where A is the corresponding element in the input List.

Args:
    constant (double): 
    scalar_list (GeometryScriptScalarList): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScript_VolumeBake"></a>