## LandmassBlueprintFunctionLibrary Objects

```python
class LandmassBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Landmass Blueprint Function Library

**C++ Source:**

- **Plugin**: Landmass
- **Module**: LandmassEditor
- **File**: LandmassBPEditorExtension.h

<a id="unreal.LandmassBlueprintFunctionLibrary.world_extents_to_canvas_coordinates"></a>

#### world_extents_to_canvas_coordinates

```python
@classmethod
def world_extents_to_canvas_coordinates(
    cls, world_extents: Vector4, landscape_info: LandmassLandscapeInfo
) -> Tuple[Vector2D, Vector2D, Vector2D, Vector2D]
```

X.world_extents_to_canvas_coordinates(world_extents, landscape_info) -> (screen_position=Vector2D, screen_size=Vector2D, coordinate_position=Vector2D, coordinate_size=Vector2D)
World Extents to Canvas Coordinates

Args:
    world_extents (Vector4): 
    landscape_info (LandmassLandscapeInfo): 

Returns:
    tuple: 

    screen_position (Vector2D): 

    screen_size (Vector2D): 

    coordinate_position (Vector2D): 

    coordinate_size (Vector2D):

<a id="unreal.LandmassBlueprintFunctionLibrary.get_cursor_world_ray"></a>

#### get_cursor_world_ray

```python
@classmethod
def get_cursor_world_ray(cls) -> Optional[Tuple[Vector, Vector, Vector]]
```

X.get_cursor_world_ray() -> (camera_location=Vector, ray_origin=Vector, ray_direction=Vector) or None
Get Cursor World Ray

Returns:
    tuple or None: 

    camera_location (Vector): 

    ray_origin (Vector): 

    ray_direction (Vector):

<a id="unreal.LandmassBlueprintFunctionLibrary.force_update_texture"></a>

#### force_update_texture

```python
@classmethod
def force_update_texture(cls, texture: Texture) -> None
```

X.force_update_texture(texture) -> None
Force Update Texture

Args:
    texture (Texture):

<a id="unreal.LandmassBlueprintFunctionLibrary.combine_world_extents"></a>

#### combine_world_extents

```python
@classmethod
def combine_world_extents(cls, extents_a: Vector4,
                          extents_b: Vector4) -> Vector4
```

X.combine_world_extents(extents_a, extents_b) -> Vector4
Combine World Extents

Args:
    extents_a (Vector4): 
    extents_b (Vector4): 

Returns:
    Vector4: 

    combined_extents (Vector4):

<a id="unreal.LandmassErosionBrushBase"></a>