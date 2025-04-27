## GeoReferencingEditorBPLibrary Objects

```python
class GeoReferencingEditorBPLibrary(BlueprintFunctionLibrary)
```

Geo Referencing Editor BPLibrary

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencingEditor
- **File**: GeoReferencingEditorBPLibrary.h

<a id="unreal.GeoReferencingEditorBPLibrary.line_trace_viewport"></a>

#### line_trace_viewport

```python
@classmethod
def line_trace_viewport(cls, actors_to_ignore: Array[Actor],
                        trace_complex: bool,
                        show_trace: bool) -> Tuple[Vector2D, bool, HitResult]
```

X.line_trace_viewport(actors_to_ignore, trace_complex, show_trace) -> (screen_location=Vector2D, success=bool, hit_result=HitResult)
LineTrace under mouse cursor and return various information

Args:
    actors_to_ignore (Array[Actor]): Collection of actors for this trace to ignore.
    trace_complex (bool): 
    show_trace (bool): 

Returns:
    tuple: 

    screen_location (Vector2D): Viewport-Space position of cursor.

    success (bool): 

    hit_result (HitResult): The trace hits result.

<a id="unreal.GeoReferencingEditorBPLibrary.line_trace"></a>

#### line_trace

```python
@classmethod
def line_trace(cls, world_location: Vector, world_direction: Vector,
               actors_to_ignore: Array[Actor], trace_complex: bool,
               show_trace: bool) -> Tuple[bool, HitResult]
```

X.line_trace(world_location, world_direction, actors_to_ignore, trace_complex, show_trace) -> (success=bool, hit_result=HitResult)
LineTrace at specific location/direction

Args:
    world_location (Vector): Location of viewport origin (camera) in world space
    world_direction (Vector): Direction of viewport (camera) in world space
    actors_to_ignore (Array[Actor]): 
    trace_complex (bool): Whether we should trace against complex collision
    show_trace (bool): Whether we should debug draw the trace

Returns:
    tuple: 

    success (bool): If the Level editor not are in focus it will return false, and same if nothing is hit.

    hit_result (HitResult): The trace hits result.

<a id="unreal.GeoReferencingEditorBPLibrary.get_viewport_cursor_location"></a>

#### get_viewport_cursor_location

```python
@classmethod
def get_viewport_cursor_location(cls) -> Tuple[bool, Vector2D]
```

X.get_viewport_cursor_location() -> (focused=bool, screen_location=Vector2D)
Retrieve the Viewport-Space position of the mouse in the Level Editor Viewport. If the Level editor not are in focus it will return false.

Returns:
    tuple: 

    focused (bool): If the Level editor not are in focus it will return false.

    screen_location (Vector2D): The screen location result.

<a id="unreal.GeoReferencingEditorBPLibrary.get_viewport_cursor_information"></a>

#### get_viewport_cursor_information

```python
@classmethod
def get_viewport_cursor_information(
        cls) -> Tuple[bool, Vector2D, Vector, Vector]
```

X.get_viewport_cursor_information() -> (focused=bool, screen_location=Vector2D, world_location=Vector, world_direction=Vector)
Retrieve information about the viewport under the mouse cursor.

Returns:
    tuple: 

    focused (bool): If the Level editor not are in focus it will return false.

    screen_location (Vector2D): Viewport-Space position of cursor.

    world_location (Vector): Location of viewport origin (camera) in world space.

    world_direction (Vector): Direction of viewport (camera) in world space.

<a id="unreal.GooglePADFunctionLibrary"></a>