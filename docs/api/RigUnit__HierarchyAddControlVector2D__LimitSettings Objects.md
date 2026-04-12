## RigUnit\_HierarchyAddControlVector2D\_LimitSettings Objects

```python
class RigUnit_HierarchyAddControlVector2D_LimitSettings(StructBase)
```

Rig Unit Hierarchy Add Control Vector 2D Limit Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_limits`` (bool):  [Read-Write]
- ``limit_x`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_y`` (RigControlLimitEnabled):  [Read-Write]
- ``max_value`` (Vector2D):  [Read-Write]
- ``min_value`` (Vector2D):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(limit_x: RigControlLimitEnabled = [False, False],
             limit_y: RigControlLimitEnabled = [False, False],
             min_value: Vector2D = [0.000000, 0.000000],
             max_value: Vector2D = [0.000000, 0.000000],
             draw_limits: bool = False) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.limit_x"></a>

#### limit\_x

```python
@property
def limit_x() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.limit_x"></a>

#### limit\_x

```python
@limit_x.setter
def limit_x(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.limit_y"></a>

#### limit\_y

```python
@property
def limit_y() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.limit_y"></a>

#### limit\_y

```python
@limit_y.setter
def limit_y(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.min_value"></a>

#### min\_value

```python
@property
def min_value() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.min_value"></a>

#### min\_value

```python
@min_value.setter
def min_value(value: Vector2D) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.max_value"></a>

#### max\_value

```python
@property
def max_value() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.max_value"></a>

#### max\_value

```python
@max_value.setter
def max_value(value: Vector2D) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.draw_limits"></a>

#### draw\_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.draw_limits"></a>

#### draw\_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings"></a>