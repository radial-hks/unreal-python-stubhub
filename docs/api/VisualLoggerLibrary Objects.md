## VisualLoggerLibrary Objects

```python
class VisualLoggerLibrary(BlueprintFunctionLibrary)
```

Visual Logger Kismet Library

**C++ Source:**

- **Module**: Engine
- **File**: VisualLoggerKismetLibrary.h

<a id="unreal.VisualLoggerLibrary.redirect_vislog"></a>

#### redirect_vislog

```python
@classmethod
def redirect_vislog(cls, source_owner: Object,
                    destination_owner: Object) -> None
```

X.redirect_vislog(source_owner, destination_owner) -> None
Makes SourceOwner log to DestinationOwner's vislog

Args:
    source_owner (Object): 
    destination_owner (Object):

<a id="unreal.VisualLoggerLibrary.log_text"></a>

#### log_text

```python
@classmethod
def log_text(cls,
             world_context_object: Object,
             text: str,
             log_category: Name = "VisLogBP",
             add_to_message_log: bool = False) -> None
```

X.log_text(world_context_object, text, log_category="VisLogBP", add_to_message_log=False) -> None
Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    text (str): 
    log_category (Name): 
    add_to_message_log (bool):

<a id="unreal.VisualLoggerLibrary.log_sphere"></a>

#### log_sphere

```python
@classmethod
def log_sphere(cls,
               world_context_object: Object,
               center: Vector,
               radius: float,
               text: str,
               object_color: LinearColor = [
                   0.000000, 0.000000, 1.000000, 1.000000
               ],
               log_category: Name = "VisLogBP",
               add_to_message_log: bool = False,
               wireframe: bool = False) -> None
```

X.log_sphere(world_context_object, center, radius, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], log_category="VisLogBP", add_to_message_log=False, wireframe=False) -> None
Logs sphere shape - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    center (Vector): 
    radius (float): 
    text (str): 
    object_color (LinearColor): 
    log_category (Name): 
    add_to_message_log (bool): 
    wireframe (bool):

<a id="unreal.VisualLoggerLibrary.log_segment"></a>

#### log_segment

```python
@classmethod
def log_segment(cls,
                world_context_object: Object,
                segment_start: Vector,
                segment_end: Vector,
                text: str,
                object_color: LinearColor = [
                    0.000000, 0.000000, 1.000000, 1.000000
                ],
                thickness: float = 0.000000,
                category_name: Name = "VisLogBP",
                add_to_message_log: bool = False) -> None
```

X.log_segment(world_context_object, segment_start, segment_end, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], thickness=0.000000, category_name="VisLogBP", add_to_message_log=False) -> None
Logs segment - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    segment_start (Vector): 
    segment_end (Vector): 
    text (str): 
    object_color (LinearColor): 
    thickness (float): 
    category_name (Name): 
    add_to_message_log (bool):

<a id="unreal.VisualLoggerLibrary.log_oriented_box"></a>

#### log_oriented_box

```python
@classmethod
def log_oriented_box(cls,
                     world_context_object: Object,
                     box_shape: Box,
                     transform: Transform,
                     text: str,
                     object_color: LinearColor = [
                         0.000000, 0.000000, 1.000000, 1.000000
                     ],
                     log_category: Name = "VisLogBP",
                     add_to_message_log: bool = False,
                     wireframe: bool = False) -> None
```

X.log_oriented_box(world_context_object, box_shape, transform, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], log_category="VisLogBP", add_to_message_log=False, wireframe=False) -> None
Logs oriented box shape - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    box_shape (Box): 
    transform (Transform): 
    text (str): 
    object_color (LinearColor): 
    log_category (Name): 
    add_to_message_log (bool): 
    wireframe (bool):

<a id="unreal.VisualLoggerLibrary.log_location"></a>

#### log_location

```python
@classmethod
def log_location(cls,
                 world_context_object: Object,
                 location: Vector,
                 text: str,
                 object_color: LinearColor = [
                     0.000000, 0.000000, 1.000000, 1.000000
                 ],
                 radius: float = 10.000000,
                 log_category: Name = "VisLogBP",
                 add_to_message_log: bool = False) -> None
```

X.log_location(world_context_object, location, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], radius=10.000000, log_category="VisLogBP", add_to_message_log=False) -> None
Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    location (Vector): 
    text (str): 
    object_color (LinearColor): 
    radius (float): 
    log_category (Name): 
    add_to_message_log (bool):

<a id="unreal.VisualLoggerLibrary.log_cylinder"></a>

#### log_cylinder

```python
@classmethod
def log_cylinder(cls,
                 world_context_object: Object,
                 start: Vector,
                 end: Vector,
                 radius: float,
                 text: str,
                 object_color: LinearColor = [
                     0.000000, 0.000000, 1.000000, 1.000000
                 ],
                 log_category: Name = "VisLogBP",
                 add_to_message_log: bool = False,
                 wireframe: bool = False) -> None
```

X.log_cylinder(world_context_object, start, end, radius, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], log_category="VisLogBP", add_to_message_log=False, wireframe=False) -> None
Logs cylinder shape - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    start (Vector): 
    end (Vector): 
    radius (float): 
    text (str): 
    object_color (LinearColor): 
    log_category (Name): 
    add_to_message_log (bool): 
    wireframe (bool):

<a id="unreal.VisualLoggerLibrary.log_cone"></a>

#### log_cone

```python
@classmethod
def log_cone(cls,
             world_context_object: Object,
             origin: Vector,
             direction: Vector,
             length: float,
             angle: float,
             text: str,
             object_color: LinearColor = [
                 0.000000, 0.000000, 1.000000, 1.000000
             ],
             log_category: Name = "VisLogBP",
             add_to_message_log: bool = False,
             wireframe: bool = False) -> None
```

X.log_cone(world_context_object, origin, direction, length, angle, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], log_category="VisLogBP", add_to_message_log=False, wireframe=False) -> None
Logs cone shape - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    length (float): 
    angle (float): 
    text (str): 
    object_color (LinearColor): 
    log_category (Name): 
    add_to_message_log (bool): 
    wireframe (bool):

<a id="unreal.VisualLoggerLibrary.log_circle"></a>

#### log_circle

```python
@classmethod
def log_circle(cls,
               world_context_object: Object,
               center: Vector,
               up_axis: Vector,
               radius: float,
               text: str,
               object_color: LinearColor = [
                   0.000000, 0.000000, 1.000000, 1.000000
               ],
               thickness: float = 0.000000,
               category_name: Name = "VisLogBP",
               add_to_message_log: bool = False) -> None
```

X.log_circle(world_context_object, center, up_axis, radius, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], thickness=0.000000, category_name="VisLogBP", add_to_message_log=False) -> None
Logs circle - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    center (Vector): 
    up_axis (Vector): 
    radius (float): 
    text (str): 
    object_color (LinearColor): 
    thickness (float): 
    category_name (Name): 
    add_to_message_log (bool):

<a id="unreal.VisualLoggerLibrary.log_capsule"></a>

#### log_capsule

```python
@classmethod
def log_capsule(cls,
                world_context_object: Object,
                base: Vector,
                half_height: float,
                radius: float,
                rotation: Quat,
                text: str,
                object_color: LinearColor = [
                    0.000000, 0.000000, 1.000000, 1.000000
                ],
                log_category: Name = "VisLogBP",
                add_to_message_log: bool = False,
                wireframe: bool = False) -> None
```

X.log_capsule(world_context_object, base, half_height, radius, rotation, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], log_category="VisLogBP", add_to_message_log=False, wireframe=False) -> None
Logs capsule shape - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    base (Vector): 
    half_height (float): 
    radius (float): 
    rotation (Quat): 
    text (str): 
    object_color (LinearColor): 
    log_category (Name): 
    add_to_message_log (bool): 
    wireframe (bool):

<a id="unreal.VisualLoggerLibrary.log_box"></a>

#### log_box

```python
@classmethod
def log_box(cls,
            world_context_object: Object,
            box_shape: Box,
            text: str,
            object_color: LinearColor = [
                0.000000, 0.000000, 1.000000, 1.000000
            ],
            log_category: Name = "VisLogBP",
            add_to_message_log: bool = False,
            wireframe: bool = False) -> None
```

X.log_box(world_context_object, box_shape, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], log_category="VisLogBP", add_to_message_log=False, wireframe=False) -> None
Logs box shape - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    box_shape (Box): 
    text (str): 
    object_color (LinearColor): 
    log_category (Name): 
    add_to_message_log (bool): 
    wireframe (bool):

<a id="unreal.VisualLoggerLibrary.log_arrow"></a>

#### log_arrow

```python
@classmethod
def log_arrow(cls,
              world_context_object: Object,
              segment_start: Vector,
              segment_end: Vector,
              text: str,
              object_color: LinearColor = [
                  0.000000, 0.000000, 1.000000, 1.000000
              ],
              category_name: Name = "VisLogBP",
              add_to_message_log: bool = False) -> None
```

X.log_arrow(world_context_object, segment_start, segment_end, text, object_color=[0.000000, 0.000000, 1.000000, 1.000000], category_name="VisLogBP", add_to_message_log=False) -> None
Logs arrow - recording for Visual Logs has to be enabled to record this data

Args:
    world_context_object (Object): 
    segment_start (Vector): 
    segment_end (Vector): 
    text (str): 
    object_color (LinearColor): 
    category_name (Name): 
    add_to_message_log (bool):

<a id="unreal.VisualLoggerLibrary.enable_recording"></a>

#### enable_recording

```python
@classmethod
def enable_recording(cls, enabled: bool) -> None
```

X.enable_recording(enabled) -> None
Enable Recording

Args:
    enabled (bool):

<a id="unreal.VOIPTalker"></a>