## GeographicCoordinatesFunctionLibrary Objects

```python
class GeographicCoordinatesFunctionLibrary(BlueprintFunctionLibrary)
```

Geographic Coordinates Function Library

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencing
- **File**: GeographicCoordinates.h

<a id="unreal.GeographicCoordinatesFunctionLibrary.to_separate_texts"></a>

#### to_separate_texts

```python
@classmethod
def to_separate_texts(
        cls,
        geographic_coordinates: GeographicCoordinates,
        integral_digits_lat_lon: int = 8,
        integral_digits_alti: int = 2,
        as_dms: bool = False
) -> Tuple[GeographicCoordinates, Text, Text, Text]
```

X.to_separate_texts(geographic_coordinates, integral_digits_lat_lon=8, integral_digits_alti=2, as_dms=False) -> (geographic_coordinates=GeographicCoordinates, out_latitude=Text, out_longitude=Text, out_altitude=Text)
Converts a GeographicCoordinates value to 3 separate text values

Args:
    geographic_coordinates (GeographicCoordinates): 
    integral_digits_lat_lon (int32): 
    integral_digits_alti (int32): 
    as_dms (bool): 

Returns:
    tuple: 

    geographic_coordinates (GeographicCoordinates): 

    out_latitude (Text): 

    out_longitude (Text): 

    out_altitude (Text):

<a id="unreal.GeographicCoordinatesFunctionLibrary.to_lat_long_alt_vector"></a>

#### to_lat_long_alt_vector

```python
@classmethod
def to_lat_long_alt_vector(
    cls, geographic_coordinates: GeographicCoordinates
) -> Tuple[GeographicCoordinates, Vector]
```

X.to_lat_long_alt_vector(geographic_coordinates) -> (geographic_coordinates=GeographicCoordinates, out_lat_long_alt_vector=Vector)
Express the Geographic coordinates as a FVector where  where X=Latitude, Y=Longitude, Z=Altitude
deprecated: BP now support doubles, Function useless and can lead to precision issues

Args:
    geographic_coordinates (GeographicCoordinates): 

Returns:
    tuple: 

    geographic_coordinates (GeographicCoordinates): 

    out_lat_long_alt_vector (Vector):

<a id="unreal.GeographicCoordinatesFunctionLibrary.to_full_text"></a>

#### to_full_text

```python
@classmethod
def to_full_text(cls,
                 geographic_coordinates: GeographicCoordinates,
                 integral_digits_lat_lon: int = 8,
                 integral_digits_alti: int = 2,
                 as_dms: bool = False) -> Tuple[Text, GeographicCoordinates]
```

X.to_full_text(geographic_coordinates, integral_digits_lat_lon=8, integral_digits_alti=2, as_dms=False) -> (Text, geographic_coordinates=GeographicCoordinates)
Converts a GeographicCoordinates value to localized formatted text, in the form 'X= Y= Z='

Args:
    geographic_coordinates (GeographicCoordinates): 
    integral_digits_lat_lon (int32): 
    integral_digits_alti (int32): 
    as_dms (bool): 

Returns:
    GeographicCoordinates: 

    geographic_coordinates (GeographicCoordinates):

<a id="unreal.GeographicCoordinatesFunctionLibrary.to_compact_text"></a>

#### to_compact_text

```python
@classmethod
def to_compact_text(
        cls,
        geographic_coordinates: GeographicCoordinates,
        integral_digits_lat_lon: int = 8,
        integral_digits_alti: int = 2,
        as_dms: bool = False) -> Tuple[Text, GeographicCoordinates]
```

X.to_compact_text(geographic_coordinates, integral_digits_lat_lon=8, integral_digits_alti=2, as_dms=False) -> (Text, geographic_coordinates=GeographicCoordinates)
Converts a GeographicCoordinates value to formatted text, in the form '(X, Y, Z)'

Args:
    geographic_coordinates (GeographicCoordinates): 
    integral_digits_lat_lon (int32): 
    integral_digits_alti (int32): 
    as_dms (bool): 

Returns:
    GeographicCoordinates: 

    geographic_coordinates (GeographicCoordinates):

<a id="unreal.GeographicCoordinatesFunctionLibrary.make_geographic_coordinates"></a>

#### make_geographic_coordinates

```python
@classmethod
def make_geographic_coordinates(
        cls, lat_long_alt_vector: Vector) -> GeographicCoordinates
```

X.make_geographic_coordinates(lat_long_alt_vector) -> GeographicCoordinates
Make Geographic Coordinates from a FVector where X=Latitude, Y=Longitude, Z=Altitude

Args:
    lat_long_alt_vector (Vector): 

Returns:
    GeographicCoordinates:

<a id="unreal.GeoReferencingBFL"></a>