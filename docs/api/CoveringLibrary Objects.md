## CoveringLibrary Objects

```python
class CoveringLibrary(BlueprintFunctionLibrary)
```

Covering Library

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: CoveringBlueprintFunctionLibrary.h

<a id="unreal.CoveringLibrary.store_triangles_location_to_texture"></a>

#### store\_triangles\_location\_to\_texture

```python
@classmethod
def store_triangles_location_to_texture(cls, bottom_vertexes: Array[Vector],
                                        bottom_triangles: Array[int],
                                        min_x: float, max_x: float,
                                        min_y: float, max_y: float,
                                        use32_texture: bool) -> Texture2D
```

X.store_triangles_location_to_texture(bottom_vertexes, bottom_triangles, min_x, max_x, min_y, max_y, use32_texture) -> Texture2D
Store Triangles Location to Texture

Args:
    bottom_vertexes (Array[Vector]): 
    bottom_triangles (Array[int32]): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double): 
    use32_texture (bool): 

Returns:
    Texture2D:

<a id="unreal.CoveringLibrary.store_points_location_to_texture"></a>

#### store\_points\_location\_to\_texture

```python
@classmethod
def store_points_location_to_texture(cls, points_array: Array[Vector],
                                     min_x: float, max_x: float, min_y: float,
                                     max_y: float,
                                     use32_texture: bool) -> Texture2D
```

X.store_points_location_to_texture(points_array, min_x, max_x, min_y, max_y, use32_texture) -> Texture2D
Store Points Location to Texture

Args:
    points_array (Array[Vector]): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double): 
    use32_texture (bool): 

Returns:
    Texture2D:

<a id="unreal.CoveringLibrary.calculate_square_bounds"></a>

#### calculate\_square\_bounds

```python
@classmethod
def calculate_square_bounds(
    cls, out_ring_points: Array[Vector]
) -> Tuple[float, float, float, float, float, float]
```

X.calculate_square_bounds(out_ring_points) -> (double, min_x=double, max_x=double, min_y=double, max_y=double, min_z=double)
Calculate Square Bounds

Args:
    out_ring_points (Array[Vector]): 

Returns:
    tuple: 

    min_x (double): 

    max_x (double): 

    min_y (double): 

    max_y (double): 

    min_z (double):

<a id="unreal.CoveringDataDriveObjectComponent"></a>