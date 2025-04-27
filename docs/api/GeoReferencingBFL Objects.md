## GeoReferencingBFL Objects

```python
class GeoReferencingBFL(BlueprintFunctionLibrary)
```

Blueprint function library to convert geospatial coordinates to text

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencing
- **File**: GeoReferencingBFL.h

<a id="unreal.GeoReferencingBFL.to_separate_texts"></a>

#### to_separate_texts

```python
@classmethod
def to_separate_texts(
        cls,
        cartesian_coordinates: Vector,
        integral_digits: int = 3) -> Tuple[Vector, Text, Text, Text]
```

X.to_separate_texts(cartesian_coordinates, integral_digits=3) -> (cartesian_coordinates=Vector, out_x=Text, out_y=Text, out_z=Text)
Converts a LargeCoordinates value to 3 separate text values

Args:
    cartesian_coordinates (Vector): 
    integral_digits (int32): 

Returns:
    tuple: 

    cartesian_coordinates (Vector): 

    out_x (Text): 

    out_y (Text): 

    out_z (Text):

<a id="unreal.GeoReferencingBFL.to_full_text"></a>

#### to_full_text

```python
@classmethod
def to_full_text(cls,
                 cartesian_coordinates: Vector,
                 integral_digits: int = 3) -> Tuple[Text, Vector]
```

X.to_full_text(cartesian_coordinates, integral_digits=3) -> (Text, cartesian_coordinates=Vector)
Converts a LargeCoordinates value to localized formatted text, in the form 'X= Y= Z='

Args:
    cartesian_coordinates (Vector): 
    integral_digits (int32): 

Returns:
    Vector: 

    cartesian_coordinates (Vector):

<a id="unreal.GeoReferencingBFL.to_compact_text"></a>

#### to_compact_text

```python
@classmethod
def to_compact_text(cls,
                    cartesian_coordinates: Vector,
                    integral_digits: int = 3) -> Tuple[Text, Vector]
```

X.to_compact_text(cartesian_coordinates, integral_digits=3) -> (Text, cartesian_coordinates=Vector)
Converts a LargeCoordinates value to formatted text, in the form '(X, Y, Z)'

Args:
    cartesian_coordinates (Vector): 
    integral_digits (int32): 

Returns:
    Vector: 

    cartesian_coordinates (Vector):

<a id="unreal.GeoReferencingSystem"></a>