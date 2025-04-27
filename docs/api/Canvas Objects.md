## Canvas Objects

```python
class Canvas(Object)
```

A drawing canvas.

**C++ Source:**

- **Module**: Engine
- **File**: Canvas.h

<a id="unreal.Canvas.clipped_text_size"></a>

#### clipped_text_size

```python
def clipped_text_size(render_font: Font,
                      render_text: str,
                      scale: Vector2D = [1.000000, 1.000000]) -> Vector2D
```

x.clipped_text_size(render_font, render_text, scale=[1.000000, 1.000000]) -> Vector2D
Returns the clipped text size in screen space coordinates.

Args:
    render_font (Font): Font to use when determining the size of the text. If this is null, then a default engine font is used.
    render_text (str): Text to determine the size of.
    scale (Vector2D): Scale of the font to use when determining the size of the text.

Returns:
    Vector2D: Returns the screen space size of the text.

<a id="unreal.Canvas.wrapped_text_size"></a>

#### wrapped_text_size

```python
def wrapped_text_size(render_font: Font, render_text: str) -> Vector2D
```

x.wrapped_text_size(render_font, render_text) -> Vector2D
Returns the wrapped text size in screen space coordinates.

Args:
    render_font (Font): Font to use when determining the size of the text. If this is null, then a default engine font is used.
    render_text (str): Text to determine the size of.

Returns:
    Vector2D: Returns the screen space size of the text.

<a id="unreal.Canvas.project"></a>

#### project

```python
def project(world_location: Vector) -> Vector
```

x.project(world_location) -> Vector
Performs a projection of a world space coordinates using the projection matrix set up for the Canvas.

Args:
    world_location (Vector): World space location to project onto the Canvas rendering plane.

Returns:
    Vector: Returns a vector where X, Y defines a screen space position representing the world space location.

<a id="unreal.Canvas.draw_triangles"></a>

#### draw_triangles

```python
def draw_triangles(render_texture: Texture,
                   triangles: Array[CanvasUVTri]) -> None
```

x.draw_triangles(render_texture, triangles) -> None
Draws a set of triangles on the Canvas.

Args:
    render_texture (Texture): Texture to use when rendering the triangles. If no texture is set, then the default white texture is used.
    triangles (Array[CanvasUVTri]): Triangles to render.

<a id="unreal.Canvas.draw_texture"></a>

#### draw_texture

```python
def draw_texture(render_texture: Texture,
                 screen_position: Vector2D,
                 screen_size: Vector2D,
                 coordinate_position: Vector2D,
                 coordinate_size: Vector2D = [1.000000, 1.000000],
                 render_color: LinearColor = [
                     1.000000, 1.000000, 1.000000, 1.000000
                 ],
                 blend_mode: BlendMode = BlendMode.BLEND_TRANSLUCENT,
                 rotation: float = 0.000000,
                 pivot_point: Vector2D = [0.500000, 0.500000]) -> None
```

x.draw_texture(render_texture, screen_position, screen_size, coordinate_position, coordinate_size=[1.000000, 1.000000], render_color=[1.000000, 1.000000, 1.000000, 1.000000], blend_mode=BlendMode.BLEND_TRANSLUCENT, rotation=0.000000, pivot_point=[0.500000, 0.500000]) -> None
Draws a texture on the Canvas.

Args:
    render_texture (Texture): Texture to use when rendering. If no texture is set then this will use the default white texture.
    screen_position (Vector2D): Screen space position to render the texture.
    screen_size (Vector2D): Screen space size to render the texture.
    coordinate_position (Vector2D): Normalized UV starting coordinate to use when rendering the texture.
    coordinate_size (Vector2D): Normalized UV size coordinate to use when rendering the texture.
    render_color (LinearColor): Color to use when rendering the texture.
    blend_mode (BlendMode): Blending mode to use when rendering the texture.
    rotation (float): Rotation, in degrees, to render the texture.
    pivot_point (Vector2D): Normalized pivot point to use when rotating the texture.

<a id="unreal.Canvas.draw_text"></a>

#### draw_text

```python
def draw_text(
    render_font: Font,
    render_text: str,
    screen_position: Vector2D,
    scale: Vector2D = [1.000000, 1.000000],
    render_color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
    kerning: float = 0.000000,
    shadow_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000],
    shadow_offset: Vector2D = [1.000000, 1.000000],
    centre_x: bool = False,
    centre_y: bool = False,
    outlined: bool = False,
    outline_color: LinearColor = [0.000000, 0.000000, 0.000000,
                                  1.000000]) -> None
```

x.draw_text(render_font, render_text, screen_position, scale=[1.000000, 1.000000], render_color=[1.000000, 1.000000, 1.000000, 1.000000], kerning=0.000000, shadow_color=[0.000000, 0.000000, 0.000000, 1.000000], shadow_offset=[1.000000, 1.000000], centre_x=False, centre_y=False, outlined=False, outline_color=[0.000000, 0.000000, 0.000000, 1.000000]) -> None
Draws text on the Canvas.

Args:
    render_font (Font): Font to use when rendering the text. If this is null, then a default engine font is used.
    render_text (str): Text to render on the Canvas.
    screen_position (Vector2D): Screen space position to render the text.
    scale (Vector2D): 
    render_color (LinearColor): Color to render the text.
    kerning (float): Horizontal spacing adjustment to modify the spacing between each letter.
    shadow_color (LinearColor): Color to render the shadow of the text.
    shadow_offset (Vector2D): Pixel offset relative to the screen space position to render the shadow of the text.
    centre_x (bool): If true, then interpret the screen space position X coordinate as the center of the rendered text.
    centre_y (bool): If true, then interpret the screen space position Y coordinate as the center of the rendered text.
    outlined (bool): If true, then the text should be rendered with an outline.
    outline_color (LinearColor): Color to render the outline for the text.

<a id="unreal.Canvas.draw_polygon"></a>

#### draw_polygon

```python
def draw_polygon(
    render_texture: Texture,
    screen_position: Vector2D,
    radius: Vector2D = [1.000000, 1.000000],
    number_of_sides: int = 3,
    render_color: LinearColor = [1.000000, 1.000000, 1.000000,
                                 1.000000]) -> None
```

x.draw_polygon(render_texture, screen_position, radius=[1.000000, 1.000000], number_of_sides=3, render_color=[1.000000, 1.000000, 1.000000, 1.000000]) -> None
Draws a polygon on the Canvas.

Args:
    render_texture (Texture): Texture to use when rendering the triangles. If no texture is set, then the default white texture is used.
    screen_position (Vector2D): Screen space position to render the text.
    radius (Vector2D): How large in pixels this polygon should be.
    number_of_sides (int32): How many sides this polygon should have. This should be above or equal to three.
    render_color (LinearColor): Color to tint the polygon.

<a id="unreal.Canvas.draw_material_triangles"></a>

#### draw_material_triangles

```python
def draw_material_triangles(render_material: MaterialInterface,
                            triangles: Array[CanvasUVTri]) -> None
```

x.draw_material_triangles(render_material, triangles) -> None
Draws a set of triangles on the Canvas.

Args:
    render_material (MaterialInterface): Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas.
    triangles (Array[CanvasUVTri]): Triangles to render.

<a id="unreal.Canvas.draw_material"></a>

#### draw_material

```python
def draw_material(render_material: MaterialInterface,
                  screen_position: Vector2D,
                  screen_size: Vector2D,
                  coordinate_position: Vector2D,
                  coordinate_size: Vector2D = [1.000000, 1.000000],
                  rotation: float = 0.000000,
                  pivot_point: Vector2D = [0.500000, 0.500000]) -> None
```

x.draw_material(render_material, screen_position, screen_size, coordinate_position, coordinate_size=[1.000000, 1.000000], rotation=0.000000, pivot_point=[0.500000, 0.500000]) -> None
Draws a material on the Canvas.

Args:
    render_material (MaterialInterface): Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas.
    screen_position (Vector2D): Screen space position to render the texture.
    screen_size (Vector2D): Screen space size to render the texture.
    coordinate_position (Vector2D): Normalized UV starting coordinate to use when rendering the texture.
    coordinate_size (Vector2D): Normalized UV size coordinate to use when rendering the texture.
    rotation (float): Rotation, in degrees, to render the texture.
    pivot_point (Vector2D): Normalized pivot point to use when rotating the texture.

<a id="unreal.Canvas.draw_line"></a>

#### draw_line

```python
def draw_line(
    screen_position_a: Vector2D = [0.000000, 0.000000],
    screen_position_b: Vector2D = [0.000000, 0.000000],
    thickness: float = 1.000000,
    render_color: LinearColor = [1.000000, 1.000000, 1.000000,
                                 1.000000]) -> None
```

x.draw_line(screen_position_a=[0.000000, 0.000000], screen_position_b=[0.000000, 0.000000], thickness=1.000000, render_color=[1.000000, 1.000000, 1.000000, 1.000000]) -> None
Draws a line on the Canvas.

Args:
    screen_position_a (Vector2D): Starting position of the line in screen space.
    screen_position_b (Vector2D): Ending position of the line in screen space.
    thickness (float): How many pixels thick this line should be.
    render_color (LinearColor): Color to render the line.

<a id="unreal.Canvas.draw_box"></a>

#### draw_box

```python
def draw_box(
    screen_position: Vector2D,
    screen_size: Vector2D,
    thickness: float = 1.000000,
    render_color: LinearColor = [1.000000, 1.000000, 1.000000,
                                 1.000000]) -> None
```

x.draw_box(screen_position, screen_size, thickness=1.000000, render_color=[1.000000, 1.000000, 1.000000, 1.000000]) -> None
Draws an unfilled box on the Canvas.

Args:
    screen_position (Vector2D): Screen space position to render the text.
    screen_size (Vector2D): Screen space size to render the texture.
    thickness (float): How many pixels thick the box lines should be.
    render_color (LinearColor): Color to tint the box.

<a id="unreal.Canvas.draw_border"></a>

#### draw_border

```python
def draw_border(border_texture: Texture,
                background_texture: Texture,
                left_border_texture: Texture,
                right_border_texture: Texture,
                top_border_texture: Texture,
                bottom_border_texture: Texture,
                screen_position: Vector2D,
                screen_size: Vector2D,
                coordinate_position: Vector2D,
                coordinate_size: Vector2D = [1.000000, 1.000000],
                render_color: LinearColor = [
                    1.000000, 1.000000, 1.000000, 1.000000
                ],
                border_scale: Vector2D = [0.100000, 0.100000],
                background_scale: Vector2D = [0.100000, 0.100000],
                rotation: float = 0.000000,
                pivot_point: Vector2D = [0.500000, 0.500000],
                corner_size: Vector2D = [0.000000, 0.000000]) -> None
```

x.draw_border(border_texture, background_texture, left_border_texture, right_border_texture, top_border_texture, bottom_border_texture, screen_position, screen_size, coordinate_position, coordinate_size=[1.000000, 1.000000], render_color=[1.000000, 1.000000, 1.000000, 1.000000], border_scale=[0.100000, 0.100000], background_scale=[0.100000, 0.100000], rotation=0.000000, pivot_point=[0.500000, 0.500000], corner_size=[0.000000, 0.000000]) -> None
Draws a 3x3 grid border with tiled frame and tiled interior on the Canvas.

Args:
    border_texture (Texture): Texture to use for border.
    background_texture (Texture): Texture to use for border background.
    left_border_texture (Texture): Texture to use for the tiling left border.
    right_border_texture (Texture): Texture to use for the tiling right border.
    top_border_texture (Texture): Texture to use for the tiling top border.
    bottom_border_texture (Texture): Texture to use for the tiling bottom border.
    screen_position (Vector2D): Screen space position to render the texture.
    screen_size (Vector2D): Screen space size to render the texture.
    coordinate_position (Vector2D): Normalized UV starting coordinate to use when rendering the border texture.
    coordinate_size (Vector2D): Normalized UV size coordinate to use when rendering the border texture.
    render_color (LinearColor): Color to tint the border.
    border_scale (Vector2D): Scale of the border.
    background_scale (Vector2D): Scale of the background.
    rotation (float): Rotation, in degrees, to render the texture.
    pivot_point (Vector2D): Normalized pivot point to use when rotating the texture.
    corner_size (Vector2D): Frame corner size in percent of frame texture (should be < 0.5f).

<a id="unreal.Canvas.deproject"></a>

#### deproject

```python
def deproject(screen_position: Vector2D) -> Tuple[Vector, Vector]
```

x.deproject(screen_position) -> (world_origin=Vector, world_direction=Vector)
Performs a deprojection of a screen space coordinate using the projection matrix set up for the Canvas.

Args:
    screen_position (Vector2D): Screen space position to deproject to the World.

Returns:
    tuple: 

    world_origin (Vector): Vector which is the world position of the screen space position.

    world_direction (Vector): Vector which can be used in a trace to determine what is "behind" the screen space position. Useful for object picking.

<a id="unreal.InputSettings"></a>