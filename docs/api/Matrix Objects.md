## Matrix Objects

```python
class Matrix(StructBase)
```

A 4x4 matrix.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Matrix.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``w_plane`` (Plane):  [Read-Write]
- ``x_plane`` (Plane):  [Read-Write]
- ``y_plane`` (Plane):  [Read-Write]
- ``z_plane`` (Plane):  [Read-Write]

<a id="unreal.Matrix.__init__"></a>

#### __init__

```python
def __init__(
        x_plane: Plane = [0.000000, 0.000000, 0.000000, 0.000000],
        y_plane: Plane = [0.000000, 0.000000, 0.000000, 0.000000],
        z_plane: Plane = [0.000000, 0.000000, 0.000000, 0.000000],
        w_plane: Plane = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.Matrix.x_plane"></a>

#### x_plane

```python
@property
def x_plane() -> Plane
```

(Plane):  [Read-Write]

<a id="unreal.Matrix.x_plane"></a>

#### x_plane

```python
@x_plane.setter
def x_plane(value: Plane) -> None
```

<a id="unreal.Matrix.y_plane"></a>

#### y_plane

```python
@property
def y_plane() -> Plane
```

(Plane):  [Read-Write]

<a id="unreal.Matrix.y_plane"></a>

#### y_plane

```python
@y_plane.setter
def y_plane(value: Plane) -> None
```

<a id="unreal.Matrix.z_plane"></a>

#### z_plane

```python
@property
def z_plane() -> Plane
```

(Plane):  [Read-Write]

<a id="unreal.Matrix.z_plane"></a>

#### z_plane

```python
@z_plane.setter
def z_plane(value: Plane) -> None
```

<a id="unreal.Matrix.w_plane"></a>

#### w_plane

```python
@property
def w_plane() -> Plane
```

(Plane):  [Read-Write]

<a id="unreal.Matrix.w_plane"></a>

#### w_plane

```python
@w_plane.setter
def w_plane(value: Plane) -> None
```

<a id="unreal.Matrix.not_equal"></a>

#### not_equal

```python
def not_equal(b: Matrix, tolerance: float = 0.000100) -> bool
```

x.not_equal(b, tolerance=0.000100) -> bool
Checks whether another Matrix is not equal to this, within specified tolerance.

Args:
    b (Matrix): 
    tolerance (float): 

Returns:
    bool: true if two Matrix are not equal, within specified tolerance, otherwise false.

<a id="unreal.Matrix.multiply"></a>

#### multiply

```python
def multiply(b: Matrix) -> Matrix
```

x.multiply(b) -> Matrix
Gets the result of multiplying a Matrix to this.

Args:
    b (Matrix): 

Returns:
    Matrix: The result of multiplication.

<a id="unreal.Matrix.multiply_float"></a>

#### multiply_float

```python
def multiply_float(b: float) -> Matrix
```

x.multiply_float(b) -> Matrix
Multiplies all values of the matrix by a float.
If your Matrix represents a Transform that you wish to scale you should use Apply Scale instead

Args:
    b (double): 

Returns:
    Matrix:

<a id="unreal.Matrix.transform_vector4"></a>

#### transform_vector4

```python
def transform_vector4(v: Vector4) -> Vector4
```

x.transform_vector4(v) -> Vector4
Transform a vector by the matrix.
(Assumes Matrix represents a transform)

Args:
    v (Vector4): 

Returns:
    Vector4:

<a id="unreal.Matrix.transform_vector"></a>

#### transform_vector

```python
def transform_vector(v: Vector) -> Vector4
```

x.transform_vector(v) -> Vector4
Transform a direction vector - will not take into account translation part of the FMatrix.
If you want to transform a surface normal (or plane) and correctly account for non-uniform scaling you should use TransformByUsingAdjointT.
(Assumes Matrix represents a transform)

Args:
    v (Vector): 

Returns:
    Vector4:

<a id="unreal.Matrix.transform_position"></a>

#### transform_position

```python
def transform_position(v: Vector) -> Vector4
```

x.transform_position(v) -> Vector4
Transform a location - will take into account translation part of the FMatrix.
(Assumes Matrix represents a transform)

Args:
    v (Vector): 

Returns:
    Vector4:

<a id="unreal.Matrix.to_quat"></a>

#### to_quat

```python
def to_quat() -> Quat
```

x.to_quat() -> Quat
Transform a rotation matrix into a quaternion.
(Assumes Matrix represents a transform)
warning: rotation part will need to be unit length for this to be right!

Returns:
    Quat:

<a id="unreal.Matrix.set_origin"></a>

#### set_origin

```python
def set_origin(new_origin: Vector) -> None
```

x.set_origin(new_origin) -> None
Set the origin of the coordinate system to the given vector
(Assumes Matrix represents a transform)

Args:
    new_origin (Vector):

<a id="unreal.Matrix.set_column"></a>

#### set_column

```python
def set_column(column: MatrixColumns, value: Vector) -> None
```

x.set_column(column, value) -> None
Matrix Set Column

Args:
    column (MatrixColumns): 
    value (Vector):

<a id="unreal.Matrix.set_axis"></a>

#### set_axis

```python
def set_axis(axis: AxisType, axis_vector: Vector) -> None
```

x.set_axis(axis, axis_vector) -> None
set an axis of this matrix
(Assumes Matrix represents a transform)

Args:
    axis (AxisType): vector of the axis
    axis_vector (Vector):

<a id="unreal.Matrix.scale_translation"></a>

#### scale_translation

```python
def scale_translation(scale3d: Vector) -> Matrix
```

x.scale_translation(scale3d) -> Matrix
Scale the translation part of the matrix by the supplied vector.
(Assumes Matrix represents a transform)

Args:
    scale3d (Vector): 

Returns:
    Matrix:

<a id="unreal.Matrix.remove_translation"></a>

#### remove_translation

```python
def remove_translation() -> Matrix
```

x.remove_translation() -> Matrix
Remove any translation from this matrix
(Assumes Matrix represents a transform)

Returns:
    Matrix:

<a id="unreal.Matrix.remove_scaling"></a>

#### remove_scaling

```python
def remove_scaling(tolerance: float = 0.000000) -> None
```

x.remove_scaling(tolerance=0.000000) -> None
Remove any scaling from this matrix (ie magnitude of each row is 1) with error Tolerance
(Assumes Matrix represents a transform)

Args:
    tolerance (float):

<a id="unreal.Matrix.mirror"></a>

#### mirror

```python
def mirror(mirror_axis: AxisType, flip_axis: AxisType) -> Matrix
```

x.mirror(mirror_axis, flip_axis) -> Matrix
Utility for mirroring this transform across a certain plane, and flipping one of the axis as well.
(Assumes Matrix represents a transform)

Args:
    mirror_axis (AxisType): 
    flip_axis (AxisType): 

Returns:
    Matrix:

<a id="unreal.Matrix.inverse_transform_vector"></a>

#### inverse_transform_vector

```python
def inverse_transform_vector(v: Vector) -> Vector
```

x.inverse_transform_vector(v) -> Vector
Transform a direction vector by the inverse of this matrix - will not take into account translation part.
If you want to transform a surface normal (or plane) and correctly account for non-uniform scaling you should use TransformByUsingAdjointT with adjoint of matrix inverse.
(Assumes Matrix represents a transform)

Args:
    v (Vector): 

Returns:
    Vector:

<a id="unreal.Matrix.inverse_transform_position"></a>

#### inverse_transform_position

```python
def inverse_transform_position(v: Vector) -> Vector
```

x.inverse_transform_position(v) -> Vector
Inverts the matrix and then transforms V - correctly handles scaling in this matrix.
(Assumes Matrix represents a transform)

Args:
    v (Vector): 

Returns:
    Vector:

<a id="unreal.Matrix.get_unit_axis"></a>

#### get_unit_axis

```python
def get_unit_axis(axis: AxisType) -> Vector
```

x.get_unit_axis(axis) -> Vector
get unit length axis of this matrix
(Assumes Matrix represents a transform)

Args:
    axis (AxisType): 

Returns:
    Vector: vector of the axis

<a id="unreal.Matrix.get_unit_axes"></a>

#### get_unit_axes

```python
def get_unit_axes() -> Tuple[Vector, Vector, Vector]
```

x.get_unit_axes() -> (x=Vector, y=Vector, z=Vector)
get unit length axes of this matrix
(Assumes Matrix represents a transform)

Returns:
    tuple: 

    x (Vector): axes returned to this param

    y (Vector): axes returned to this param

    z (Vector): axes returned to this param

<a id="unreal.Matrix.get_transposed"></a>

#### get_transposed

```python
def get_transposed() -> Matrix
```

x.get_transposed() -> Matrix
Transpose.

Returns:
    Matrix:

<a id="unreal.Matrix.get_transpose_adjoint"></a>

#### get_transpose_adjoint

```python
def get_transpose_adjoint() -> Matrix
```

x.get_transpose_adjoint() -> Matrix
Get the Transose Adjoint of the Matrix.

Returns:
    Matrix:

<a id="unreal.Matrix.get_scale_vector"></a>

#### get_scale_vector

```python
def get_scale_vector(tolerance: float = 0.000000) -> Vector
```

x.get_scale_vector(tolerance=0.000000) -> Vector
return a 3D scale vector calculated from this matrix (where each component is the magnitude of a row vector) with error Tolerance.
(Assumes Matrix represents a transform)

Args:
    tolerance (float): 

Returns:
    Vector:

<a id="unreal.Matrix.get_scaled_axis"></a>

#### get_scaled_axis

```python
def get_scaled_axis(axis: AxisType) -> Vector
```

x.get_scaled_axis(axis) -> Vector
get axis of this matrix scaled by the scale of the matrix
(Assumes Matrix represents a transform)

Args:
    axis (AxisType): 

Returns:
    Vector: vector of the axis

<a id="unreal.Matrix.get_scaled_axes"></a>

#### get_scaled_axes

```python
def get_scaled_axes() -> Tuple[Vector, Vector, Vector]
```

x.get_scaled_axes() -> (x=Vector, y=Vector, z=Vector)
get axes of this matrix scaled by the scale of the matrix
(Assumes Matrix represents a transform)

Returns:
    tuple: 

    x (Vector): axes returned to this param

    y (Vector): axes returned to this param

    z (Vector): axes returned to this param

<a id="unreal.Matrix.get_rot_determinant"></a>

#### get_rot_determinant

```python
def get_rot_determinant() -> float
```

x.get_rot_determinant() -> float


Returns:
    float: the determinant of rotation 3x3 matrix (Assumes Top Left 3x3 Submatrix represents a Rotation)

<a id="unreal.Matrix.get_rotator"></a>

#### get_rotator

```python
def get_rotator() -> Rotator
```

x.get_rotator() -> Rotator
Get the rotator representation of this matrix
(Assumes Matrix represents a transform)

Returns:
    Rotator: rotator representation of this matrix

<a id="unreal.Matrix.get_origin"></a>

#### get_origin

```python
def get_origin() -> Vector
```

x.get_origin() -> Vector
Get the origin of the co-ordinate system
(Assumes Matrix represents a transform)

Returns:
    Vector: co-ordinate system origin

<a id="unreal.Matrix.get_maximum_axis_scale"></a>

#### get_maximum_axis_scale

```python
def get_maximum_axis_scale() -> float
```

x.get_maximum_axis_scale() -> float


Returns:
    float: the maximum magnitude of any row of the matrix. (Assumes Matrix represents a transform)

<a id="unreal.Matrix.get_matrix_without_scale"></a>

#### get_matrix_without_scale

```python
def get_matrix_without_scale(tolerance: float = 0.000000) -> Matrix
```

x.get_matrix_without_scale(tolerance=0.000000) -> Matrix
Returns matrix after RemoveScaling with error Tolerance
(Assumes Matrix represents a transform)

Args:
    tolerance (float): 

Returns:
    Matrix:

<a id="unreal.Matrix.get_inverse"></a>

#### get_inverse

```python
def get_inverse() -> Matrix
```

x.get_inverse() -> Matrix
Get the inverse of the Matrix. Handles nil matrices.

Returns:
    Matrix:

<a id="unreal.Matrix.get_frustum_top_plane"></a>

#### get_frustum_top_plane

```python
def get_frustum_top_plane() -> Optional[Plane]
```

x.get_frustum_top_plane() -> Plane or None
Get the top plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Returns:
    Plane or None: 

    out_plane (Plane): the top plane of the Frustum of this matrix

<a id="unreal.Matrix.get_frustum_right_plane"></a>

#### get_frustum_right_plane

```python
def get_frustum_right_plane() -> Optional[Plane]
```

x.get_frustum_right_plane() -> Plane or None
Get the right plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Returns:
    Plane or None: 

    out_plane (Plane): the right plane of the Frustum of this matrix

<a id="unreal.Matrix.get_frustum_near_plane"></a>

#### get_frustum_near_plane

```python
def get_frustum_near_plane() -> Optional[Plane]
```

x.get_frustum_near_plane() -> Plane or None
Get the near plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Returns:
    Plane or None: 

    out_plane (Plane): the near plane of the Frustum of this matrix

<a id="unreal.Matrix.get_frustum_left_plane"></a>

#### get_frustum_left_plane

```python
def get_frustum_left_plane() -> Optional[Plane]
```

x.get_frustum_left_plane() -> Plane or None
Get the left plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Returns:
    Plane or None: 

    out_plane (Plane): the left plane of the Frustum of this matrix

<a id="unreal.Matrix.get_frustum_far_plane"></a>

#### get_frustum_far_plane

```python
def get_frustum_far_plane() -> Optional[Plane]
```

x.get_frustum_far_plane() -> Plane or None
Get the far plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Returns:
    Plane or None: 

    out_plane (Plane): the far plane of the Frustum of this matrix

<a id="unreal.Matrix.get_frustum_bottom_plane"></a>

#### get_frustum_bottom_plane

```python
def get_frustum_bottom_plane() -> Optional[Plane]
```

x.get_frustum_bottom_plane() -> Plane or None
Get the bottom plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Returns:
    Plane or None: 

    out_plane (Plane): the bottom plane of the Frustum of this matrix

<a id="unreal.Matrix.get_determinant"></a>

#### get_determinant

```python
def get_determinant() -> float
```

x.get_determinant() -> float


Returns:
    float: determinant of this matrix.

<a id="unreal.Matrix.get_column"></a>

#### get_column

```python
def get_column(column: MatrixColumns) -> Vector
```

x.get_column(column) -> Vector
get a column of this matrix

Args:
    column (MatrixColumns): 

Returns:
    Vector: vector of the column

<a id="unreal.Matrix.contains_na_n"></a>

#### contains_na_n

```python
def contains_na_n() -> bool
```

x.contains_na_n() -> bool
Returns true if any element of this matrix is NaN

Returns:
    bool:

<a id="unreal.Matrix.concatenate_translation"></a>

#### concatenate_translation

```python
def concatenate_translation(translation: Vector) -> Matrix
```

x.concatenate_translation(translation) -> Matrix
Returns a matrix with an additional translation concatenated.
(Assumes Matrix represents a transform)

Args:
    translation (Vector): 

Returns:
    Matrix:

<a id="unreal.Matrix.apply_scale"></a>

#### apply_scale

```python
def apply_scale(scale: float) -> Matrix
```

x.apply_scale(scale) -> Matrix
Apply Scale to this matrix
(Assumes Matrix represents a transform)

Args:
    scale (float): 

Returns:
    Matrix:

<a id="unreal.Matrix.equals"></a>

#### equals

```python
def equals(b: Matrix, tolerance: float = 0.000100) -> bool
```

x.equals(b, tolerance=0.000100) -> bool
Checks whether another Matrix is equal to this, within specified tolerance.

Args:
    b (Matrix): 
    tolerance (float): Error Tolerance.

Returns:
    bool: true if two Matrix are equal, within specified tolerance, otherwise false.

<a id="unreal.Matrix.transform"></a>

#### transform

```python
def transform() -> Transform
```

x.transform() -> Transform
Converts a Matrix to a Transform
(Assumes Matrix represents a transform)

Returns:
    Transform:

<a id="unreal.Matrix.rotator"></a>

#### rotator

```python
def rotator() -> Rotator
```

x.rotator() -> Rotator
Converts a Matrix to a Rotator
(Assumes Matrix represents a transform)

Returns:
    Rotator:

<a id="unreal.Matrix.add"></a>

#### add

```python
def add(b: Matrix) -> Matrix
```

x.add(b) -> Matrix
Gets the result of adding a matrix to this.

Args:
    b (Matrix): 

Returns:
    Matrix: The result of addition.

<a id="unreal.Matrix.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Matrix`` Checks whether another Matrix is equal to this, within specified tolerance.

  @param Other The other Matrix.
  @param Tolerance Error Tolerance.
  @return true if two Matrix are equal, within specified tolerance, otherwise false.

<a id="unreal.Matrix.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``Matrix`` Checks whether another Matrix is not equal to this, within specified tolerance.

  @param Other The other Matrix.
  @return true if two Matrix are not equal, within specified tolerance, otherwise false.

<a id="unreal.Matrix.__add__"></a>

#### __add__

```python
def __add__(other: Matrix) -> None
```

**Overloads:**

- ``Matrix`` Gets the result of adding a matrix to this.

  @param Other The Matrix to add.
  @return The result of addition.

<a id="unreal.Matrix.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: Matrix) -> None
```

**Overloads:**

- ``Matrix`` Gets the result of adding a matrix to this.

  @param Other The Matrix to add.
  @return The result of addition.

<a id="unreal.Matrix.__mul__"></a>

#### __mul__

```python
def __mul__(other: Matrix) -> None
```

**Overloads:**

- ``Matrix`` Gets the result of multiplying a Matrix to this.

  @param Other The matrix to multiply this by.
  @return The result of multiplication.
- ``double`` Multiplies all values of the matrix by a float.
  If your Matrix represents a Transform that you wish to scale you should use Apply Scale instead

<a id="unreal.Matrix.__imul__"></a>

#### __imul__

```python
def __imul__(other: Matrix) -> None
```

**Overloads:**

- ``Matrix`` Gets the result of multiplying a Matrix to this.

  @param Other The matrix to multiply this by.
  @return The result of multiplication.
- ``double`` Multiplies all values of the matrix by a float.
  If your Matrix represents a Transform that you wish to scale you should use Apply Scale instead

<a id="unreal.Matrix.IDENTITY"></a>

#### IDENTITY

(Matrix): Identity matrix

<a id="unreal.Plane"></a>