## BlueprintFunctionLibraryAPI Objects

```python
class BlueprintFunctionLibraryAPI(BlueprintFunctionLibrary)
```

Blueprint Function Library API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: BlueprintFunctionLibraryAPI.h

<a id="unreal.BlueprintFunctionLibraryAPI.string_hex_color2_linear_color_original"></a>

#### string\_hex\_color2\_linear\_color\_original

```python
@classmethod
def string_hex_color2_linear_color_original(
        cls, hex_color: str) -> Optional[LinearColor]
```

X.string_hex_color2_linear_color_original(hex_color) -> LinearColor or None
String Hex Color 2Linear Color Original

Args:
    hex_color (str): 

Returns:
    LinearColor or None: 

    ou_linear_color (LinearColor):

<a id="unreal.BlueprintFunctionLibraryAPI.string_hex_color2_linear_color"></a>

#### string\_hex\_color2\_linear\_color

```python
@classmethod
def string_hex_color2_linear_color(cls,
                                   hex_color: str) -> Optional[LinearColor]
```

X.string_hex_color2_linear_color(hex_color) -> LinearColor or None
String Hex Color 2Linear Color

Args:
    hex_color (str): 

Returns:
    LinearColor or None: 

    ou_linear_color (LinearColor):

<a id="unreal.BlueprintFunctionLibraryAPI.set_cast_shadow"></a>

#### set\_cast\_shadow

```python
@classmethod
def set_cast_shadow(cls, entity: WdpActorEntity, shadow: bool) -> None
```

X.set_cast_shadow(entity, shadow) -> None
Set Cast Shadow

Args:
    entity (WdpActorEntity): 
    shadow (bool):

<a id="unreal.BlueprintFunctionLibraryAPI.process_polygon_data"></a>

#### process\_polygon\_data

```python
@classmethod
def process_polygon_data(cls, points: Array[Vector],
                         clockwise: bool) -> Optional[Array[Vector]]
```

X.process_polygon_data(points, clockwise) -> Array[Vector] or None
Process Polygon Data

Args:
    points (Array[Vector]): 
    clockwise (bool): 

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.BlueprintFunctionLibraryAPI.process_polygon2d_data"></a>

#### process\_polygon2d\_data

```python
@classmethod
def process_polygon2d_data(cls, points: Array[Vector2D],
                           clockwise: bool) -> Optional[Array[Vector2D]]
```

X.process_polygon2d_data(points, clockwise) -> Array[Vector2D] or None
Process Polygon 2DData

Args:
    points (Array[Vector2D]): 
    clockwise (bool): 

Returns:
    Array[Vector2D] or None: 

    out_points (Array[Vector2D]):

<a id="unreal.BlueprintFunctionLibraryAPI.point_is_in_range"></a>

#### point\_is\_in\_range

```python
@classmethod
def point_is_in_range(cls, range_points: Array[Vector],
                      test_point: Vector) -> bool
```

X.point_is_in_range(range_points, test_point) -> bool
判断点是否在多边形内

Args:
    range_points (Array[Vector]): 
    test_point (Vector): 

Returns:
    bool:

<a id="unreal.BlueprintFunctionLibraryAPI.notify_web_js_event"></a>

#### notify\_web\_js\_event

```python
@classmethod
def notify_web_js_event(cls, world_context_object: Object, name: str,
                        args: str) -> None
```

X.notify_web_js_event(world_context_object, name, args) -> None
Notify Web JSEvent

Args:
    world_context_object (Object): 
    name (str): 
    args (str):

<a id="unreal.BlueprintFunctionLibraryAPI.get_wdp_pick_filter"></a>

#### get\_wdp\_pick\_filter

```python
@classmethod
def get_wdp_pick_filter(cls, entity_eid: int) -> WdpPickFilter
```

X.get_wdp_pick_filter(entity_eid) -> WdpPickFilter
Get Wdp Pick Filter

Args:
    entity_eid (int64): 

Returns:
    WdpPickFilter: 

    out_pick_filter (WdpPickFilter):

<a id="unreal.BlueprintFunctionLibraryAPI.get_left_up_right_down_points_ex"></a>

#### get\_left\_up\_right\_down\_points\_ex

```python
@classmethod
def get_left_up_right_down_points_ex(
    cls, positions: Array[Vector]
) -> Optional[Tuple[Vector2D, Vector2D, int, int, int, int]]
```

X.get_left_up_right_down_points_ex(positions) -> (out_left_up_pos=Vector2D, out_right_down_pos=Vector2D, out_min_index_x=int32, out_min_index_y=int32, out_max_index_x=int32, out_max_index_y=int32) or None
Get Left Up Right Down Points Ex

Args:
    positions (Array[Vector]): 

Returns:
    tuple or None: 

    out_left_up_pos (Vector2D): 

    out_right_down_pos (Vector2D): 

    out_min_index_x (int32): 

    out_min_index_y (int32): 

    out_max_index_x (int32): 

    out_max_index_y (int32):

<a id="unreal.BlueprintFunctionLibraryAPI.get_left_up_right_down_points_diameter_ex"></a>

#### get\_left\_up\_right\_down\_points\_diameter\_ex

```python
@classmethod
def get_left_up_right_down_points_diameter_ex(
    cls, positions: Array[Vector], diameters: Array[float]
) -> Optional[Tuple[Vector2D, Vector2D, float, float]]
```

X.get_left_up_right_down_points_diameter_ex(positions, diameters) -> (out_left_up_pos=Vector2D, out_right_down_pos=Vector2D, out_left_up_diameter=float, out_right_down_diameter=float) or None
Get Left Up Right Down Points Diameter Ex

Args:
    positions (Array[Vector]): 
    diameters (Array[float]): 

Returns:
    tuple or None: 

    out_left_up_pos (Vector2D): 

    out_right_down_pos (Vector2D): 

    out_left_up_diameter (float): 

    out_right_down_diameter (float):

<a id="unreal.BlueprintFunctionLibraryAPI.get_left_up_right_down_points"></a>

#### get\_left\_up\_right\_down\_points

```python
@classmethod
def get_left_up_right_down_points(
        cls,
        positions: Array[Vector],
        radius: float = 0.000000) -> Optional[Tuple[Vector2D, Vector2D]]
```

X.get_left_up_right_down_points(positions, radius=0.000000) -> (out_left_up_pos=Vector2D, out_right_down_pos=Vector2D) or None
Get Left Up Right Down Points

Args:
    positions (Array[Vector]): 
    radius (double): 

Returns:
    tuple or None: 

    out_left_up_pos (Vector2D): 

    out_right_down_pos (Vector2D):

<a id="unreal.BlueprintFunctionLibraryAPI.get_coord_z_ref"></a>

#### get\_coord\_z\_ref

```python
@classmethod
def get_coord_z_ref(cls, incoord_ref: int) -> Coord_Z_Ref
```

X.get_coord_z_ref(incoord_ref) -> Coord_Z_Ref
Get Coord Z Ref

Args:
    incoord_ref (int32): 

Returns:
    Coord_Z_Ref: 

    out_coordz_ref (Coord_Z_Ref):

<a id="unreal.BlueprintFunctionLibraryAPI.get_center_point"></a>

#### get\_center\_point

```python
@classmethod
def get_center_point(cls, positions: Array[Vector]) -> Optional[Vector]
```

X.get_center_point(positions) -> Vector or None
Get Center Point

Args:
    positions (Array[Vector]): 

Returns:
    Vector or None: 

    out_center_pos (Vector):

<a id="unreal.BlueprintFunctionLibraryAPI.delaunay_polygon"></a>

#### delaunay\_polygon

```python
@classmethod
def delaunay_polygon(cls, points: Array[Vector]) -> Array[int]
```

X.delaunay_polygon(points) -> Array[int32]
Delaunay Polygon

Args:
    points (Array[Vector]): 

Returns:
    Array[int32]: 

    triangle_index (Array[int32]):

<a id="unreal.BlueprintFunctionLibraryAPI.create_texture_render_target2d"></a>

#### create\_texture\_render\_target2d

```python
@classmethod
def create_texture_render_target2d(
        cls,
        width: int = 256,
        height: int = 256,
        clear_color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        gamma: float = 1.000000) -> TextureRenderTarget2D
```

X.create_texture_render_target2d(width=256, height=256, clear_color=[1.000000, 1.000000, 1.000000, 1.000000], gamma=1.000000) -> TextureRenderTarget2D
Create a new Texture Render Target 2D, ideal for use with Scene Capture Components created during runtime that need their own unique Render Targets

Args:
    width (int32): Texture Width
    height (int32): Texture Height
    clear_color (LinearColor): The color the texture is cleared to
    gamma (float): Will override FTextureRenderTarget2DResource::GetDisplayGamma if > 0.

Returns:
    TextureRenderTarget2D: A new Texture Render Target 2D!

<a id="unreal.BlueprintFunctionLibraryAPI.calculate_bounding_box"></a>

#### calculate\_bounding\_box

```python
@classmethod
def calculate_bounding_box(cls,
                           contour_points: Array[Vector],
                           contour_height: float,
                           use_average_z: bool = True) -> Box
```

X.calculate_bounding_box(contour_points, contour_height, use_average_z=True) -> Box
Calculate Bounding Box

Args:
    contour_points (Array[Vector]): 
    contour_height (float): 
    use_average_z (bool): 

Returns:
    Box: 

    out_bounding_box (Box):

<a id="unreal.BlueprintFunctionLibraryAPI.api_ue_to_gis"></a>

#### api\_ue\_to\_gis

```python
@classmethod
def api_ue_to_gis(cls, input_ue: Vector) -> Vector
```

X.api_ue_to_gis(input_ue) -> Vector
API UETo GIS

Args:
    input_ue (Vector): 

Returns:
    Vector: 

    out_gis (Vector):

<a id="unreal.BlueprintFunctionLibraryAPI.api_gis_to_ue"></a>

#### api\_gis\_to\_ue

```python
@classmethod
def api_gis_to_ue(cls, input_gis: Vector) -> Vector
```

X.api_gis_to_ue(input_gis) -> Vector
API GISTo UE

Args:
    input_gis (Vector): 

Returns:
    Vector: 

    ue_pos (Vector):

<a id="unreal.ChinaMapEntity"></a>