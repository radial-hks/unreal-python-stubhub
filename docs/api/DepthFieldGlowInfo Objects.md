## DepthFieldGlowInfo Objects

```python
class DepthFieldGlowInfo(StructBase)
```

Info for glow when using depth field rendering

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_glow`` (bool):  [Read-Write] Whether to turn on the outline glow (depth field fonts only)
- ``glow_color`` (LinearColor):  [Read-Write] Base color to use for the glow
- ``glow_inner_radius`` (Vector2D):  [Read-Write] If bEnableGlow, outline glow inner radius (0 to 1, 0.5 is edge of character silhouette)
  glow influence will be 1 at GlowInnerRadius.X and 0 at GlowInnerRadius.Y
- ``glow_outer_radius`` (Vector2D):  [Read-Write] If bEnableGlow, outline glow outer radius (0 to 1, 0.5 is edge of character silhouette)
  glow influence will be 0 at GlowOuterRadius.X and 1 at GlowOuterRadius.Y

<a id="unreal.DepthFieldGlowInfo.__init__"></a>

#### __init__

```python
def __init__(enable_glow: bool = False,
             glow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             glow_outer_radius: Vector2D = [0.000000, 0.000000],
             glow_inner_radius: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.DepthFieldGlowInfo.enable_glow"></a>

#### enable_glow

```python
@property
def enable_glow() -> bool
```

(bool):  [Read-Write] Whether to turn on the outline glow (depth field fonts only)

<a id="unreal.DepthFieldGlowInfo.enable_glow"></a>

#### enable_glow

```python
@enable_glow.setter
def enable_glow(value: bool) -> None
```

<a id="unreal.DepthFieldGlowInfo.glow_color"></a>

#### glow_color

```python
@property
def glow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Base color to use for the glow

<a id="unreal.DepthFieldGlowInfo.glow_color"></a>

#### glow_color

```python
@glow_color.setter
def glow_color(value: LinearColor) -> None
```

<a id="unreal.DepthFieldGlowInfo.glow_outer_radius"></a>

#### glow_outer_radius

```python
@property
def glow_outer_radius() -> Vector2D
```

(Vector2D):  [Read-Write] If bEnableGlow, outline glow outer radius (0 to 1, 0.5 is edge of character silhouette)
glow influence will be 0 at GlowOuterRadius.X and 1 at GlowOuterRadius.Y

<a id="unreal.DepthFieldGlowInfo.glow_outer_radius"></a>

#### glow_outer_radius

```python
@glow_outer_radius.setter
def glow_outer_radius(value: Vector2D) -> None
```

<a id="unreal.DepthFieldGlowInfo.glow_inner_radius"></a>

#### glow_inner_radius

```python
@property
def glow_inner_radius() -> Vector2D
```

(Vector2D):  [Read-Write] If bEnableGlow, outline glow inner radius (0 to 1, 0.5 is edge of character silhouette)
glow influence will be 1 at GlowInnerRadius.X and 0 at GlowInnerRadius.Y

<a id="unreal.DepthFieldGlowInfo.glow_inner_radius"></a>

#### glow_inner_radius

```python
@glow_inner_radius.setter
def glow_inner_radius(value: Vector2D) -> None
```

<a id="unreal.FontRenderInfo"></a>