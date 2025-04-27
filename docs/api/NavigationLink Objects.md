## NavigationLink Objects

```python
class NavigationLink(NavigationLinkBase)
```

Navigation Link

**C++ Source:**

- **Module**: Engine
- **File**: NavLinkDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_class`` (type(Class)):  [Read-Write] Area type of this link (empty = default)
- ``description`` (str):  [Read-Write] this is an editor-only property to put descriptions in navlinks setup, to be able to identify it easier
- ``direction`` (NavLinkDirection):  [Read-Write]
- ``left`` (Vector):  [Read-Write]
- ``left_project_height`` (float):  [Read-Write] if greater than 0 nav system will attempt to project navlink's start point on geometry below
- ``max_fall_down_length`` (float):  [Read-Write] if greater than 0 nav system will attempt to project navlink's end point on geometry below
- ``right`` (Vector):  [Read-Write]
- ``snap_height`` (float):  [Read-Write]
- ``snap_radius`` (float):  [Read-Write]
- ``snap_to_cheapest_area`` (bool):  [Read-Write] If set, link will try to snap to the cheapest area in given radius
- ``supported_agents`` (NavAgentSelector):  [Read-Write] restrict link only to specified agents
- ``use_snap_height`` (bool):  [Read-Write]

<a id="unreal.NavigationLink.__init__"></a>

#### __init__

```python
def __init__(direction: NavLinkDirection = NavLinkDirection.BOTH_WAYS,
             left: Vector = [0.000000, 0.000000, 0.000000],
             right: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.NavigationLink.left"></a>

#### left

```python
@property
def left() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.NavigationLink.left"></a>

#### left

```python
@left.setter
def left(value: Vector) -> None
```

<a id="unreal.NavigationLink.right"></a>

#### right

```python
@property
def right() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.NavigationLink.right"></a>

#### right

```python
@right.setter
def right(value: Vector) -> None
```

<a id="unreal.NavigationSegmentLink"></a>