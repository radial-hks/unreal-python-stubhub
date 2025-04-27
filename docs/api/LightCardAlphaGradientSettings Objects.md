## LightCardAlphaGradientSettings Objects

```python
class LightCardAlphaGradientSettings(StructBase)
```

Light Card Alpha Gradient Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterLightCardActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write] The angle (degrees) determines the gradient direction.
- ``enable_alpha_gradient`` (bool):  [Read-Write] Enables/disables alpha gradient effect
- ``ending_alpha`` (float):  [Read-Write] Ending alpha value in the gradient
- ``starting_alpha`` (float):  [Read-Write] Starting alpha value in the gradient

<a id="unreal.LightCardAlphaGradientSettings.__init__"></a>

#### __init__

```python
def __init__(enable_alpha_gradient: bool = False,
             starting_alpha: float = 0.000000,
             ending_alpha: float = 0.000000,
             angle: float = 0.000000) -> None
```

<a id="unreal.LightCardAlphaGradientSettings.enable_alpha_gradient"></a>

#### enable_alpha_gradient

```python
@property
def enable_alpha_gradient() -> bool
```

(bool):  [Read-Write] Enables/disables alpha gradient effect

<a id="unreal.LightCardAlphaGradientSettings.enable_alpha_gradient"></a>

#### enable_alpha_gradient

```python
@enable_alpha_gradient.setter
def enable_alpha_gradient(value: bool) -> None
```

<a id="unreal.LightCardAlphaGradientSettings.starting_alpha"></a>

#### starting_alpha

```python
@property
def starting_alpha() -> float
```

(float):  [Read-Write] Starting alpha value in the gradient

<a id="unreal.LightCardAlphaGradientSettings.starting_alpha"></a>

#### starting_alpha

```python
@starting_alpha.setter
def starting_alpha(value: float) -> None
```

<a id="unreal.LightCardAlphaGradientSettings.ending_alpha"></a>

#### ending_alpha

```python
@property
def ending_alpha() -> float
```

(float):  [Read-Write] Ending alpha value in the gradient

<a id="unreal.LightCardAlphaGradientSettings.ending_alpha"></a>

#### ending_alpha

```python
@ending_alpha.setter
def ending_alpha(value: float) -> None
```

<a id="unreal.LightCardAlphaGradientSettings.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write] The angle (degrees) determines the gradient direction.

<a id="unreal.LightCardAlphaGradientSettings.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.MPCDIGeometryImportData"></a>