## ChaosClothAssetInteractor Objects

```python
class ChaosClothAssetInteractor(Object)
```

Chaos Cloth Asset Interactor

**C++ Source:**

- **Plugin**: ChaosClothAsset
- **Module**: ChaosClothAssetEngine
- **File**: ClothAssetInteractor.h

<a id="unreal.ChaosClothAssetInteractor.set_weighted_float_value"></a>

#### set_weighted_float_value

```python
def set_weighted_float_value(property_name: str,
                             lod_index: int = -1,
                             value: Vector2D = [0.000000, 0.000000]) -> None
```

x.set_weighted_float_value(property_name, lod_index=-1, value=[0.000000, 0.000000]) -> None
Set the low and high values for a weighted property (if it exists). All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (Vector2D):

<a id="unreal.ChaosClothAssetInteractor.set_vector_value"></a>

#### set_vector_value

```python
def set_vector_value(property_name: str,
                     lod_index: int = -1,
                     value: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

x.set_vector_value(property_name, lod_index=-1, value=[0.000000, 0.000000, 0.000000]) -> None
Set the value for a property (if it exists). All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (Vector):

<a id="unreal.ChaosClothAssetInteractor.set_string_value"></a>

#### set_string_value

```python
def set_string_value(property_name: str,
                     lod_index: int = -1,
                     value: str = "") -> None
```

x.set_string_value(property_name, lod_index=-1, value="") -> None
Set the string value for a property (if it exists). This is typically the map name associated with a property. All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (str):

<a id="unreal.ChaosClothAssetInteractor.set_low_float_value"></a>

#### set_low_float_value

```python
def set_low_float_value(property_name: str,
                        lod_index: int = -1,
                        value: float = 0.000000) -> None
```

x.set_low_float_value(property_name, lod_index=-1, value=0.000000) -> None
Set the low value for a weighted property (if it exists). All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (float):

<a id="unreal.ChaosClothAssetInteractor.set_int_value"></a>

#### set_int_value

```python
def set_int_value(property_name: str,
                  lod_index: int = -1,
                  value: int = 0) -> None
```

x.set_int_value(property_name, lod_index=-1, value=0) -> None
Set the value for a property (if it exists). All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (int32):

<a id="unreal.ChaosClothAssetInteractor.set_high_float_value"></a>

#### set_high_float_value

```python
def set_high_float_value(property_name: str,
                         lod_index: int = -1,
                         value: float = 0.000000) -> None
```

x.set_high_float_value(property_name, lod_index=-1, value=0.000000) -> None
Set the high value for a weighted property (if it exists). All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (float):

<a id="unreal.ChaosClothAssetInteractor.set_float_value"></a>

#### set_float_value

```python
def set_float_value(property_name: str,
                    lod_index: int = -1,
                    value: float = 0.000000) -> None
```

x.set_float_value(property_name, lod_index=-1, value=0.000000) -> None
Set the value for a property (if it exists). This sets the Low and High values for weighted values. All LODs will be set when LODIndex = -1.

Args:
    property_name (str): 
    lod_index (int32): 
    value (float):

<a id="unreal.ChaosClothAssetInteractor.get_weighted_float_value"></a>

#### get_weighted_float_value

```python
def get_weighted_float_value(
        property_name: str,
        lod_index: int = 0,
        default_value: Vector2D = [0.000000, 0.000000]) -> Vector2D
```

x.get_weighted_float_value(property_name, lod_index=0, default_value=[0.000000, 0.000000]) -> Vector2D
Get the low and high values for a weighted property value. DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.ChaosClothAssetInteractor.get_vector_value"></a>

#### get_vector_value

```python
def get_vector_value(
        property_name: str,
        lod_index: int = 0,
        default_value: Vector = [0.000000, 0.000000, 0.000000]) -> Vector
```

x.get_vector_value(property_name, lod_index=0, default_value=[0.000000, 0.000000, 0.000000]) -> Vector
Get the value for a property cast to vector. DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (Vector): 

Returns:
    Vector:

<a id="unreal.ChaosClothAssetInteractor.get_string_value"></a>

#### get_string_value

```python
def get_string_value(property_name: str,
                     lod_index: int = 0,
                     default_value: str = "") -> str
```

x.get_string_value(property_name, lod_index=0, default_value="") -> str
Get the string value for a property (typically the associated map name for weighted values). DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (str): 

Returns:
    str:

<a id="unreal.ChaosClothAssetInteractor.get_low_float_value"></a>

#### get_low_float_value

```python
def get_low_float_value(property_name: str,
                        lod_index: int = 0,
                        default_value: float = 0.000000) -> float
```

x.get_low_float_value(property_name, lod_index=0, default_value=0.000000) -> float
Get the low value for a weighted property value (same as GetFloatValue). DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (float): 

Returns:
    float:

<a id="unreal.ChaosClothAssetInteractor.get_int_value"></a>

#### get_int_value

```python
def get_int_value(property_name: str,
                  lod_index: int = 0,
                  default_value: int = 0) -> int
```

x.get_int_value(property_name, lod_index=0, default_value=0) -> int32
Get the value for a property cast to int. DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (int32): 

Returns:
    int32:

<a id="unreal.ChaosClothAssetInteractor.get_high_float_value"></a>

#### get_high_float_value

```python
def get_high_float_value(property_name: str,
                         lod_index: int = 0,
                         default_value: float = 0.000000) -> float
```

x.get_high_float_value(property_name, lod_index=0, default_value=0.000000) -> float
Get the high value for a weighted property value. DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (float): 

Returns:
    float:

<a id="unreal.ChaosClothAssetInteractor.get_float_value"></a>

#### get_float_value

```python
def get_float_value(property_name: str,
                    lod_index: int = 0,
                    default_value: float = 0.000000) -> float
```

x.get_float_value(property_name, lod_index=0, default_value=0.000000) -> float
Get the value for a property cast to float. DefaultValue will be returned if the property is not found.

Args:
    property_name (str): 
    lod_index (int32): 
    default_value (float): 

Returns:
    float:

<a id="unreal.ChaosClothAssetInteractor.get_all_properties"></a>

#### get_all_properties

```python
def get_all_properties(lod_index: int = -1) -> Array[str]
```

x.get_all_properties(lod_index=-1) -> Array[str]
Generate a list of all properties held by this interactor. Properties for all LODs will be returned if LODIndex = -1.

Args:
    lod_index (int32): 

Returns:
    Array[str]:

<a id="unreal.ChaosVDSolverDataComponent"></a>