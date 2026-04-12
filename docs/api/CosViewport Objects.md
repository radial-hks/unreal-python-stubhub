## CosViewport Objects

```python
class CosViewport(StructBase)
```

Cos Viewport

**C++ Source:**

- **Plugin**: CustomProgram
- **Module**: CustomProgram
- **File**: CustomViewportType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bind_to_controller`` (BindToController):  [Read-Write]
- ``bind_to_view_target`` (BindToViewTarget):  [Read-Write]
- ``location_offset_of_view_port`` (Vector):  [Read-Write]
- ``origin`` (Vector2D):  [Read-Write] 分配给这个玩家的主视口子区域的左上角坐标。 0 - 1
- ``rotation_offset_of_view_port`` (Rotator):  [Read-Write]
- ``size`` (Vector2D):  [Read-Write] 主视口分区分配给这个播放器的大小。 0 - 1
- ``view_name`` (Name):  [Read-Write] 具有唯一性
- ``view_point_type`` (ViewPointType):  [Read-Write]

<a id="unreal.CosViewport.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    view_name: Name = "None",
    view_point_type: ViewPointType = ViewPointType.EVPT_BIND_TO_CONTROLLER,
    bind_to_controller: BindToController = [],
    bind_to_view_target: BindToViewTarget = [None],
    origin: Vector2D = [0.000000, 0.000000],
    size: Vector2D = [0.000000, 0.000000],
    location_offset_of_view_port: Vector = [0.000000, 0.000000, 0.000000],
    rotation_offset_of_view_port: Rotator = [0.000000, 0.000000, 0.000000]
) -> None
```

<a id="unreal.CosViewport.view_name"></a>

#### view\_name

```python
@property
def view_name() -> Name
```

(Name):  [Read-Write] 具有唯一性

<a id="unreal.CosViewport.view_name"></a>

#### view\_name

```python
@view_name.setter
def view_name(value: Name) -> None
```

<a id="unreal.CosViewport.view_point_type"></a>

#### view\_point\_type

```python
@property
def view_point_type() -> ViewPointType
```

(ViewPointType):  [Read-Write]

<a id="unreal.CosViewport.view_point_type"></a>

#### view\_point\_type

```python
@view_point_type.setter
def view_point_type(value: ViewPointType) -> None
```

<a id="unreal.CosViewport.bind_to_controller"></a>

#### bind\_to\_controller

```python
@property
def bind_to_controller() -> BindToController
```

(BindToController):  [Read-Write]

<a id="unreal.CosViewport.bind_to_controller"></a>

#### bind\_to\_controller

```python
@bind_to_controller.setter
def bind_to_controller(value: BindToController) -> None
```

<a id="unreal.CosViewport.bind_to_view_target"></a>

#### bind\_to\_view\_target

```python
@property
def bind_to_view_target() -> BindToViewTarget
```

(BindToViewTarget):  [Read-Write]

<a id="unreal.CosViewport.bind_to_view_target"></a>

#### bind\_to\_view\_target

```python
@bind_to_view_target.setter
def bind_to_view_target(value: BindToViewTarget) -> None
```

<a id="unreal.CosViewport.origin"></a>

#### origin

```python
@property
def origin() -> Vector2D
```

(Vector2D):  [Read-Write] 分配给这个玩家的主视口子区域的左上角坐标。 0 - 1

<a id="unreal.CosViewport.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector2D) -> None
```

<a id="unreal.CosViewport.size"></a>

#### size

```python
@property
def size() -> Vector2D
```

(Vector2D):  [Read-Write] 主视口分区分配给这个播放器的大小。 0 - 1

<a id="unreal.CosViewport.size"></a>

#### size

```python
@size.setter
def size(value: Vector2D) -> None
```

<a id="unreal.CosViewport.location_offset_of_view_port"></a>

#### location\_offset\_of\_view\_port

```python
@property
def location_offset_of_view_port() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.CosViewport.location_offset_of_view_port"></a>

#### location\_offset\_of\_view\_port

```python
@location_offset_of_view_port.setter
def location_offset_of_view_port(value: Vector) -> None
```

<a id="unreal.CosViewport.rotation_offset_of_view_port"></a>

#### rotation\_offset\_of\_view\_port

```python
@property
def rotation_offset_of_view_port() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.CosViewport.rotation_offset_of_view_port"></a>

#### rotation\_offset\_of\_view\_port

```python
@rotation_offset_of_view_port.setter
def rotation_offset_of_view_port(value: Rotator) -> None
```

<a id="unreal.ViewportsManager"></a>