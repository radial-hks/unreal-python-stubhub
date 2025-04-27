## SlateLibrary Objects

```python
class SlateLibrary(BlueprintFunctionLibrary)
```

Slate Blueprint Library

**C++ Source:**

- **Module**: UMG
- **File**: SlateBlueprintLibrary.h

<a id="unreal.SlateLibrary.transform_vector_local_to_absolute"></a>

#### transform_vector_local_to_absolute

```python
@classmethod
def transform_vector_local_to_absolute(cls, geometry: Geometry,
                                       local_vector: Vector2D) -> Vector2D
```

X.transform_vector_local_to_absolute(geometry, local_vector) -> Vector2D
Transform Vector Local to Absolute

Args:
    geometry (Geometry): 
    local_vector (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.SlateLibrary.transform_vector_absolute_to_local"></a>

#### transform_vector_absolute_to_local

```python
@classmethod
def transform_vector_absolute_to_local(cls, geometry: Geometry,
                                       absolute_vector: Vector2D) -> Vector2D
```

X.transform_vector_absolute_to_local(geometry, absolute_vector) -> Vector2D
Transform Vector Absolute to Local

Args:
    geometry (Geometry): 
    absolute_vector (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.SlateLibrary.transform_scalar_local_to_absolute"></a>

#### transform_scalar_local_to_absolute

```python
@classmethod
def transform_scalar_local_to_absolute(cls, geometry: Geometry,
                                       local_scalar: float) -> float
```

X.transform_scalar_local_to_absolute(geometry, local_scalar) -> float
Transform Scalar Local to Absolute

Args:
    geometry (Geometry): 
    local_scalar (float): 

Returns:
    float:

<a id="unreal.SlateLibrary.transform_scalar_absolute_to_local"></a>

#### transform_scalar_absolute_to_local

```python
@classmethod
def transform_scalar_absolute_to_local(cls, geometry: Geometry,
                                       absolute_scalar: float) -> float
```

X.transform_scalar_absolute_to_local(geometry, absolute_scalar) -> float
Transform Scalar Absolute to Local

Args:
    geometry (Geometry): 
    absolute_scalar (float): 

Returns:
    float:

<a id="unreal.SlateLibrary.screen_to_widget_local"></a>

#### screen_to_widget_local

```python
@classmethod
def screen_to_widget_local(cls,
                           world_context_object: Object,
                           geometry: Geometry,
                           screen_position: Vector2D,
                           include_window_position: bool = False) -> Vector2D
```

X.screen_to_widget_local(world_context_object, geometry, screen_position, include_window_position=False) -> Vector2D
Translates a screen position in pixels into the local space of a widget with the given geometry.
If bIncludeWindowPosition is true, then this method will also remove the game window's position (useful when in windowed mode).

Args:
    world_context_object (Object): 
    geometry (Geometry): 
    screen_position (Vector2D): 
    include_window_position (bool): 

Returns:
    Vector2D: 

    local_coordinate (Vector2D):

<a id="unreal.SlateLibrary.screen_to_widget_absolute"></a>

#### screen_to_widget_absolute

```python
@classmethod
def screen_to_widget_absolute(
        cls,
        world_context_object: Object,
        screen_position: Vector2D,
        include_window_position: bool = False) -> Vector2D
```

X.screen_to_widget_absolute(world_context_object, screen_position, include_window_position=False) -> Vector2D
Translates a screen position in pixels into absolute application coordinates.
If bIncludeWindowPosition is true, then this method will also remove the game window's position (useful when in windowed mode).

Args:
    world_context_object (Object): 
    screen_position (Vector2D): 
    include_window_position (bool): 

Returns:
    Vector2D: 

    absolute_coordinate (Vector2D):

<a id="unreal.SlateLibrary.screen_to_viewport"></a>

#### screen_to_viewport

```python
@classmethod
def screen_to_viewport(cls, world_context_object: Object,
                       screen_position: Vector2D) -> Vector2D
```

X.screen_to_viewport(world_context_object, screen_position) -> Vector2D
Translates a screen position in pixels into the local space of the viewport widget.

Args:
    world_context_object (Object): 
    screen_position (Vector2D): 

Returns:
    Vector2D: 

    viewport_position (Vector2D):

<a id="unreal.SlateLibrary.local_to_viewport"></a>

#### local_to_viewport

```python
@classmethod
def local_to_viewport(cls, world_context_object: Object, geometry: Geometry,
                      local_coordinate: Vector2D) -> Tuple[Vector2D, Vector2D]
```

X.local_to_viewport(world_context_object, geometry, local_coordinate) -> (pixel_position=Vector2D, viewport_position=Vector2D)
Translates local coordinate of the geometry provided into local viewport coordinates.

Args:
    world_context_object (Object): 
    geometry (Geometry): 
    local_coordinate (Vector2D): 

Returns:
    tuple: 

    pixel_position (Vector2D): The position in the game's viewport, usable for line traces and other uses where you need a coordinate in the space of viewport resolution units.

    viewport_position (Vector2D): The position in the space of other widgets in the viewport.  Like if you wanted to add another widget to the viewport at the same position in viewport space as this location, this is what you would use.

<a id="unreal.SlateLibrary.local_to_absolute"></a>

#### local_to_absolute

```python
@classmethod
def local_to_absolute(cls, geometry: Geometry,
                      local_coordinate: Vector2D) -> Vector2D
```

X.local_to_absolute(geometry, local_coordinate) -> Vector2D
Translates local coordinates into absolute coordinates

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

Args:
    geometry (Geometry): 
    local_coordinate (Vector2D): 

Returns:
    Vector2D: Absolute coordinates

<a id="unreal.SlateLibrary.is_under_location"></a>

#### is_under_location

```python
@classmethod
def is_under_location(cls, geometry: Geometry,
                      absolute_coordinate: Vector2D) -> bool
```

X.is_under_location(geometry, absolute_coordinate) -> bool
Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

Args:
    geometry (Geometry): 
    absolute_coordinate (Vector2D): 

Returns:
    bool: true if the provided location in absolute coordinates is within the bounds of this geometry.

<a id="unreal.SlateLibrary.get_local_top_left"></a>

#### get_local_top_left

```python
@classmethod
def get_local_top_left(cls, geometry: Geometry) -> Vector2D
```

X.get_local_top_left(geometry) -> Vector2D
Returns the local top/left of the geometry in local space.

Args:
    geometry (Geometry): 

Returns:
    Vector2D:

<a id="unreal.SlateLibrary.get_local_size"></a>

#### get_local_size

```python
@classmethod
def get_local_size(cls, geometry: Geometry) -> Vector2D
```

X.get_local_size(geometry) -> Vector2D
Returns the size of the geometry in local space.

Args:
    geometry (Geometry): 

Returns:
    Vector2D:

<a id="unreal.SlateLibrary.get_absolute_size"></a>

#### get_absolute_size

```python
@classmethod
def get_absolute_size(cls, geometry: Geometry) -> Vector2D
```

X.get_absolute_size(geometry) -> Vector2D
Returns the size of the geometry in absolute space.

Args:
    geometry (Geometry): 

Returns:
    Vector2D:

<a id="unreal.SlateLibrary.equal_equal_slate_brush"></a>

#### equal_equal_slate_brush

```python
@classmethod
def equal_equal_slate_brush(cls, a: SlateBrush, b: SlateBrush) -> bool
```

X.equal_equal_slate_brush(a, b) -> bool
Returns whether brushes A and B are identical.

Args:
    a (SlateBrush): 
    b (SlateBrush): 

Returns:
    bool:

<a id="unreal.SlateLibrary.absolute_to_viewport"></a>

#### absolute_to_viewport

```python
@classmethod
def absolute_to_viewport(
        cls, world_context_object: Object,
        absolute_desktop_coordinate: Vector2D) -> Tuple[Vector2D, Vector2D]
```

X.absolute_to_viewport(world_context_object, absolute_desktop_coordinate) -> (pixel_position=Vector2D, viewport_position=Vector2D)
Translates absolute coordinate in desktop space of the geometry provided into local viewport coordinates.

Args:
    world_context_object (Object): 
    absolute_desktop_coordinate (Vector2D): 

Returns:
    tuple: 

    pixel_position (Vector2D): The position in the game's viewport, usable for line traces and other uses where you need a coordinate in the space of viewport resolution units.

    viewport_position (Vector2D): The position in the space of other widgets in the viewport.  Like if you wanted to add another widget to the viewport at the same position in viewport space as this location, this is what you would use.

<a id="unreal.SlateLibrary.absolute_to_local"></a>

#### absolute_to_local

```python
@classmethod
def absolute_to_local(cls, geometry: Geometry,
                      absolute_coordinate: Vector2D) -> Vector2D
```

X.absolute_to_local(geometry, absolute_coordinate) -> Vector2D
Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

Args:
    geometry (Geometry): 
    absolute_coordinate (Vector2D): 

Returns:
    Vector2D: Transforms AbsoluteCoordinate into the local space of this Geometry.

<a id="unreal.WidgetLibrary"></a>