## GeometryScriptScalarList Objects

```python
class GeometryScriptScalarList(StructBase)
```

Geometry Script Scalar List

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptScalarList.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptScalarList.set_scalar_list_item"></a>

#### set_scalar_list_item

```python
def set_scalar_list_item(index: int, new_value: float) -> bool
```

x.set_scalar_list_item(index, new_value) -> bool
Updates the value associated with Index in the Scalar List.
If the Index is invalid, the operation will fail and bValidIndex will be set to false.

Args:
    index (int32): 
    new_value (double): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptScalarList.get_scalar_list_length"></a>

#### get_scalar_list_length

```python
def get_scalar_list_length() -> int
```

x.get_scalar_list_length() -> int32
Returns the number of items in the Scalar List.

Returns:
    int32:

<a id="unreal.GeometryScriptScalarList.get_scalar_list_last_index"></a>

#### get_scalar_list_last_index

```python
def get_scalar_list_last_index() -> int
```

x.get_scalar_list_last_index() -> int32
Returns the index of the last Scalar in Scalar List.
If Scalar List is empty or invalid, the value -1 will be returned

Returns:
    int32:

<a id="unreal.GeometryScriptScalarList.get_scalar_list_item"></a>

#### get_scalar_list_item

```python
def get_scalar_list_item(index: int) -> Tuple[float, bool]
```

x.get_scalar_list_item(index) -> (double, is_valid_index=bool)
Returns the Scalar value associated with Index in Scalar List.
If the Index is not valid for this Scalar List, the value 0.0 will be returned and bIsValidIndex set to false.

Args:
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptScalarList.duplicate_scalar_list"></a>

#### duplicate_scalar_list

```python
def duplicate_scalar_list() -> GeometryScriptScalarList
```

x.duplicate_scalar_list() -> GeometryScriptScalarList
Copies the contents of Scalar List into Duplicate List.

Returns:
    GeometryScriptScalarList: 

    duplicate_list (GeometryScriptScalarList):

<a id="unreal.GeometryScriptScalarList.convert_scalar_list_to_array"></a>

#### convert_scalar_list_to_array

```python
def convert_scalar_list_to_array() -> Array[float]
```

x.convert_scalar_list_to_array() -> Array[double]
Converts a Scalar List to an Scalar Array (an array of doubles).

Returns:
    Array[double]: 

    scalar_array (Array[double]):

<a id="unreal.GeometryScriptScalarList.clear_scalar_list"></a>

#### clear_scalar_list

```python
def clear_scalar_list(clear_value: float = 0.000000) -> None
```

x.clear_scalar_list(clear_value=0.000000) -> None
Resets all the items in the Scalar List to the Clear Value.

Args:
    clear_value (double):

<a id="unreal.GeometryScriptScalarList.scalar_vector_multiply_in_place"></a>

#### scalar_vector_multiply_in_place

```python
def scalar_vector_multiply_in_place(
        vector_list: GeometryScriptVectorList,
        scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
```

x.scalar_vector_multiply_in_place(vector_list, scalar_multiplier=1.000000) -> GeometryScriptVectorList
Compute (ScalarMultiplier * Scalar * Vector) for each scalar/vector pair in the two input lists, and store in the input VectorList

Args:
    vector_list (GeometryScriptVectorList): 
    scalar_multiplier (double): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScriptScalarList.scalar_vector_multiply"></a>

#### scalar_vector_multiply

```python
def scalar_vector_multiply(
        vector_list: GeometryScriptVectorList,
        scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
```

x.scalar_vector_multiply(vector_list, scalar_multiplier=1.000000) -> GeometryScriptVectorList
Compute (ScalarMultiplier * Scalar * Vector) for each scalar/vector pair in the two input lists, and return in a new VectorList.

Args:
    vector_list (GeometryScriptVectorList): 
    scalar_multiplier (double): 

Returns:
    GeometryScriptVectorList:

<a id="unreal.GeometryScriptScalarList.scalar_multiply_in_place"></a>

#### scalar_multiply_in_place

```python
def scalar_multiply_in_place(
        scalar_list_b: GeometryScriptScalarList,
        constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
```

x.scalar_multiply_in_place(scalar_list_b, constant_multiplier=1.000000) -> GeometryScriptScalarList
Compute (ConstantMultiplier * A * B)  where A and B are the corresponding elements from ScalarListA and ScalarListB accordingly, and store the
result in ScalarListA.
If ScalarListA and ScalarListB have different lengths, the computation will be skipped.

Args:
    scalar_list_b (GeometryScriptScalarList): 
    constant_multiplier (double): 

Returns:
    GeometryScriptScalarList: 

    scalar_list_b (GeometryScriptScalarList):

<a id="unreal.GeometryScriptScalarList.scalar_multiply"></a>

#### scalar_multiply

```python
def scalar_multiply(
        scalar_list_b: GeometryScriptScalarList,
        constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
```

x.scalar_multiply(scalar_list_b, constant_multiplier=1.000000) -> GeometryScriptScalarList
Returns a Scalar List constructed with each element is the product (ConstantMultiplier * A * B)
where A and B are the corresponding elements from ScalarListA and ScalarListB accordingly.
If ScalarListA and ScalarListB have different lengths, no operation will be performed and an empty Scalar List will be returned.

Args:
    scalar_list_b (GeometryScriptScalarList): 
    constant_multiplier (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScriptScalarList.scalar_invert_in_place"></a>

#### scalar_invert_in_place

```python
def scalar_invert_in_place(numerator: float = 1.000000,
                           set_on_failure: float = 0.000000,
                           epsilon: float = 0.000000) -> None
```

x.scalar_invert_in_place(numerator=1.000000, set_on_failure=0.000000, epsilon=0.000000) -> None
Compute (Numerator / Scalar) for each element of ScalarList and store in input ScalarList
If Abs(Scalar) < Epsilon, set to SetOnFailure value.

Args:
    numerator (double): 
    set_on_failure (double): 
    epsilon (double):

<a id="unreal.GeometryScriptScalarList.scalar_invert"></a>

#### scalar_invert

```python
def scalar_invert(numerator: float = 1.000000,
                  set_on_failure: float = 0.000000,
                  epsilon: float = 0.000000) -> GeometryScriptScalarList
```

x.scalar_invert(numerator=1.000000, set_on_failure=0.000000, epsilon=0.000000) -> GeometryScriptScalarList
Compute (Numerator / Scalar) for each element of ScalarList and return in a new ScalarList.
If Abs(Scalar) < Epsilon, set to SetOnFailure value.

Args:
    numerator (double): 
    set_on_failure (double): 
    epsilon (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScriptScalarList.scalar_blend_in_place"></a>

#### scalar_blend_in_place

```python
def scalar_blend_in_place(
        scalar_list_b: GeometryScriptScalarList,
        constant_a: float = 1.000000,
        constant_b: float = 1.000000) -> GeometryScriptScalarList
```

x.scalar_blend_in_place(scalar_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptScalarList
Compute (ConstantA * A) + (ConstantB * B) for each pair of values in ScalarListA and ScalarListB and return in ScalarListB.
By default (constants = 1) this just adds the two values. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    scalar_list_b (GeometryScriptScalarList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptScalarList: 

    scalar_list_b (GeometryScriptScalarList):

<a id="unreal.GeometryScriptScalarList.scalar_blend"></a>

#### scalar_blend

```python
def scalar_blend(scalar_list_b: GeometryScriptScalarList,
                 constant_a: float = 1.000000,
                 constant_b: float = 1.000000) -> GeometryScriptScalarList
```

x.scalar_blend(scalar_list_b, constant_a=1.000000, constant_b=1.000000) -> GeometryScriptScalarList
Compute (ConstantA * A) + (ConstantB * B) for each pair of values in ScalarListA and ScalarListB and return in new ScalarList.
By default (constants = 1) this just adds the two values. Set ConstantB = -1 to subtract B from A.
Can also be used to Linear Interpolate, by setting ConstantB = (1-ConstantA)

Args:
    scalar_list_b (GeometryScriptScalarList): 
    constant_a (double): 
    constant_b (double): 

Returns:
    GeometryScriptScalarList:

<a id="unreal.GeometryScriptVectorList"></a>