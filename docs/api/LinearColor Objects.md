## LinearColor Objects

```python
class LinearColor(StructBase)
```

A linear, 32-bit/component floating point RGBA color.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Color.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (float):  [Read-Write]
- ``b`` (float):  [Read-Write]
- ``g`` (float):  [Read-Write]
- ``r`` (float):  [Read-Write]

<a id="unreal.LinearColor.__init__"></a>

#### __init__

```python
def __init__(r: float = 0.000000,
             g: float = 0.000000,
             b: float = 0.000000,
             a: float = 0.000000) -> None
```

<a id="unreal.LinearColor.r"></a>

#### r

```python
@property
def r() -> float
```

(float):  [Read-Write]

<a id="unreal.LinearColor.r"></a>

#### r

```python
@r.setter
def r(value: float) -> None
```

<a id="unreal.LinearColor.g"></a>

#### g

```python
@property
def g() -> float
```

(float):  [Read-Write]

<a id="unreal.LinearColor.g"></a>

#### g

```python
@g.setter
def g(value: float) -> None
```

<a id="unreal.LinearColor.b"></a>

#### b

```python
@property
def b() -> float
```

(float):  [Read-Write]

<a id="unreal.LinearColor.b"></a>

#### b

```python
@b.setter
def b(value: float) -> None
```

<a id="unreal.LinearColor.a"></a>

#### a

```python
@property
def a() -> float
```

(float):  [Read-Write]

<a id="unreal.LinearColor.a"></a>

#### a

```python
@a.setter
def a(value: float) -> None
```

<a id="unreal.LinearColor.subtract"></a>

#### subtract

```python
def subtract(b: LinearColor) -> LinearColor
```

x.subtract(b) -> LinearColor
Element-wise subtraction of two linear colors (R-R, G-G, B-B, A-A)

Args:
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.rgb_into_hsv"></a>

#### rgb_into_hsv

```python
def rgb_into_hsv() -> LinearColor
```

x.rgb_into_hsv() -> LinearColor
Converts a RGB linear color to HSV (where H is in R (0..360), S is in G (0..1), and V is in B (0..1))

Returns:
    LinearColor: 

    hsv (LinearColor):

<a id="unreal.LinearColor.rgb_into_hsv_components"></a>

#### rgb_into_hsv_components

```python
def rgb_into_hsv_components() -> Tuple[float, float, float, float]
```

x.rgb_into_hsv_components() -> (h=float, s=float, v=float, a=float)
Breaks apart a color into individual HSV components (as well as alpha) (Hue is [0..360) while Saturation and Value are 0..1)

Returns:
    tuple: 

    h (float): 

    s (float): 

    v (float): 

    a (float):

<a id="unreal.LinearColor.rgb_to_hsv"></a>

#### rgb_to_hsv

```python
def rgb_to_hsv() -> LinearColor
```

x.rgb_to_hsv() -> LinearColor
Converts a RGB linear color to HSV (where H is in R, S is in G, and V is in B)

Returns:
    LinearColor:

<a id="unreal.LinearColor.not_equal"></a>

#### not_equal

```python
def not_equal(b: LinearColor) -> bool
```

x.not_equal(b) -> bool
Returns true if linear color A is not equal to linear color B (A != B) within a specified error tolerance

Args:
    b (LinearColor): 

Returns:
    bool:

<a id="unreal.LinearColor.multiply"></a>

#### multiply

```python
def multiply(b: LinearColor) -> LinearColor
```

x.multiply(b) -> LinearColor
Element-wise multiplication of two linear colors (R*R, G*G, B*B, A*A)

Args:
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.multiply_float"></a>

#### multiply_float

```python
def multiply_float(b: float) -> LinearColor
```

x.multiply_float(b) -> LinearColor
Element-wise multiplication of a linear color by a float (F*R, F*G, F*B, F*A)

Args:
    b (float): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.lerp_using_hsv_to"></a>

#### lerp_using_hsv_to

```python
def lerp_using_hsv_to(b: LinearColor, alpha: float) -> LinearColor
```

x.lerp_using_hsv_to(b, alpha) -> LinearColor
Linearly interpolates between two colors by the specified Alpha amount (100% of A when Alpha=0 and 100% of B when Alpha=1).  The interpolation is performed in HSV color space taking the shortest path to the new color's hue.  This can give better results than a normal lerp, but is much more expensive.  The incoming colors are in RGB space, and the output color will be RGB.  The alpha value will also be interpolated.

Args:
    b (LinearColor): The color and alpha to interpolate to as linear RGBA
    alpha (float): Scalar interpolation amount (usually between 0.0 and 1.0 inclusive)

Returns:
    LinearColor: The interpolated color in linear RGB space along with the interpolated alpha value

<a id="unreal.LinearColor.lerp_to"></a>

#### lerp_to

```python
def lerp_to(b: LinearColor, alpha: float) -> LinearColor
```

x.lerp_to(b, alpha) -> LinearColor
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    b (LinearColor): 
    alpha (float): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.to_rgbe"></a>

#### to_rgbe

```python
def to_rgbe() -> Color
```

x.to_rgbe() -> Color
Converts from linear to 8-bit RGBE as outlined in Gregory Ward's Real Pixels article, Graphics Gems II, page 80.

Returns:
    Color:

<a id="unreal.LinearColor.to_new_opacity"></a>

#### to_new_opacity

```python
def to_new_opacity(opacity: float) -> LinearColor
```

x.to_new_opacity(opacity) -> LinearColor
Returns a copy of this color using the specified opacity/alpha.

Args:
    opacity (float): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.set_temperature"></a>

#### set_temperature

```python
def set_temperature(temperature: float) -> None
```

x.set_temperature(temperature) -> None
Converts temperature in Kelvins of a black body radiator to RGB chromaticity.

Args:
    temperature (float):

<a id="unreal.LinearColor.set_rgba"></a>

#### set_rgba

```python
def set_rgba(r: float, g: float, b: float, a: float = 1.000000) -> None
```

x.set_rgba(r, g, b, a=1.000000) -> None
Assign individual linear RGBA components.

Args:
    r (float): 
    g (float): 
    b (float): 
    a (float):

<a id="unreal.LinearColor.set_random_hue"></a>

#### set_random_hue

```python
def set_random_hue() -> None
```

x.set_random_hue() -> None
Sets to a random color. Choses a quite nice color based on a random hue.

<a id="unreal.LinearColor.set_from_srgb"></a>

#### set_from_srgb

```python
def set_from_srgb(srgb: Color) -> None
```

x.set_from_srgb(srgb) -> None
Assigns an FColor coming from an observed sRGB output, into a linear color.

Args:
    srgb (Color): The sRGB color that needs to be converted into linear space.

<a id="unreal.LinearColor.set_from_pow22"></a>

#### set_from_pow22

```python
def set_from_pow22(color: Color) -> None
```

x.set_from_pow22(color) -> None
Assigns an FColor coming from an observed Pow(1/2.2) output, into a linear color.

Args:
    color (Color): The Pow(1/2.2) color that needs to be converted into linear space.

<a id="unreal.LinearColor.set_from_hsv"></a>

#### set_from_hsv

```python
def set_from_hsv(h: float, s: float, v: float, a: float = 1.000000) -> None
```

x.set_from_hsv(h, s, v, a=1.000000) -> None
Assigns an HSV color to a linear space RGB color

Args:
    h (float): 
    s (float): 
    v (float): 
    a (float):

<a id="unreal.LinearColor.set"></a>

#### set

```python
def set(color: LinearColor) -> None
```

x.set(color) -> None
Assign contents of InColor

Args:
    color (LinearColor):

<a id="unreal.LinearColor.quantize_round"></a>

#### quantize_round

```python
def quantize_round() -> Color
```

x.quantize_round() -> Color
Quantizes the linear color with rounding and returns the result as an 8-bit color.  This bypasses the SRGB conversion.

Returns:
    Color:

<a id="unreal.LinearColor.quantize"></a>

#### quantize

```python
def quantize() -> Color
```

x.quantize() -> Color
Quantizes the linear color and returns the result as an 8-bit color.  This bypasses the SRGB conversion.
deprecated: Use LinearColor_QuantizeRound instead for correct color conversion.

Returns:
    Color:

<a id="unreal.LinearColor.is_near_equal"></a>

#### is_near_equal

```python
def is_near_equal(b: LinearColor, tolerance: float = 0.000100) -> bool
```

x.is_near_equal(b, tolerance=0.000100) -> bool
Returns true if linear color A is equal to linear color B (A == B) within a specified error tolerance

Args:
    b (LinearColor): 
    tolerance (float): 

Returns:
    bool:

<a id="unreal.LinearColor.get_min"></a>

#### get_min

```python
def get_min() -> float
```

x.get_min() -> float
Returns the minimum color channel value in this color structure

Returns:
    float: The minimum color channel value

<a id="unreal.LinearColor.get_max"></a>

#### get_max

```python
def get_max() -> float
```

x.get_max() -> float
Returns the maximum color channel value in this color structure

Returns:
    float: The maximum color channel value

<a id="unreal.LinearColor.get_luminance"></a>

#### get_luminance

```python
def get_luminance() -> float
```

x.get_luminance() -> float
Returns the perceived brightness of a color on a display taking into account the impact on the human eye per color channel: green > red > blue.

Returns:
    float:

<a id="unreal.LinearColor.distance"></a>

#### distance

```python
def distance(c2: LinearColor) -> float
```

x.distance(c2) -> float
Euclidean distance between two color points.

Args:
    c2 (LinearColor): 

Returns:
    float:

<a id="unreal.LinearColor.desaturated"></a>

#### desaturated

```python
def desaturated(desaturation: float) -> LinearColor
```

x.desaturated(desaturation) -> LinearColor
Returns a desaturated color, with 0 meaning no desaturation and 1 == full desaturation

Args:
    desaturation (float): 

Returns:
    LinearColor: Desaturated color

<a id="unreal.LinearColor.hsv_to_rgb"></a>

#### hsv_to_rgb

```python
def hsv_to_rgb() -> LinearColor
```

x.hsv_to_rgb() -> LinearColor
Converts a HSV linear color (where H is in R, S is in G, and V is in B) to linear RGB

Returns:
    LinearColor:

<a id="unreal.LinearColor.hsv_into_rgb"></a>

#### hsv_into_rgb

```python
def hsv_into_rgb() -> LinearColor
```

x.hsv_into_rgb() -> LinearColor
Converts a HSV linear color (where H is in R (0..360), S is in G (0..1), and V is in B (0..1)) to RGB

Returns:
    LinearColor: 

    rgb (LinearColor):

<a id="unreal.LinearColor.equals"></a>

#### equals

```python
def equals(b: LinearColor) -> bool
```

x.equals(b) -> bool
Returns true if linear color A is equal to linear color B (A == B) within a specified error tolerance

Args:
    b (LinearColor): 

Returns:
    bool:

<a id="unreal.LinearColor.divide"></a>

#### divide

```python
def divide(b: LinearColor) -> LinearColor
```

x.divide(b) -> LinearColor
Element-wise multiplication of two linear colors (R/R, G/G, B/B, A/A)

Args:
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.to_rgb_vector"></a>

#### to_rgb_vector

```python
def to_rgb_vector() -> Vector
```

x.to_rgb_vector() -> Vector
Converts a LinearColor to a vector

Returns:
    Vector:

<a id="unreal.LinearColor.to_color"></a>

#### to_color

```python
def to_color(use_srgb: bool = True) -> Color
```

x.to_color(use_srgb=True) -> Color
Quantizes the linear color and returns the result as a FColor with optional sRGB conversion and quality as goal.

Args:
    use_srgb (bool): 

Returns:
    Color:

<a id="unreal.LinearColor.interpolate_to"></a>

#### interpolate_to

```python
def interpolate_to(target: LinearColor, delta_time: float,
                   interp_speed: float) -> LinearColor
```

x.interpolate_to(target, delta_time, interp_speed) -> LinearColor
Interpolate Linear Color from Current to Target. Scaled by distance to Target, so it has a strong start speed and ease out.

Args:
    target (LinearColor): Target Color
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    LinearColor: New interpolated Color

<a id="unreal.LinearColor.add"></a>

#### add

```python
def add(b: LinearColor) -> LinearColor
```

x.add(b) -> LinearColor
Element-wise addition of two linear colors (R+R, G+G, B+B, A+A)

Args:
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.LinearColor.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``LinearColor`` Returns true if linear color A is equal to linear color B (A == B) within a specified error tolerance
- ``LinearColor`` Returns true if linear color A is equal to linear color B (A == B) within a specified error tolerance

<a id="unreal.LinearColor.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``LinearColor`` Returns true if linear color A is not equal to linear color B (A != B) within a specified error tolerance

<a id="unreal.LinearColor.__add__"></a>

#### __add__

```python
def __add__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise addition of two linear colors (R+R, G+G, B+B, A+A)

<a id="unreal.LinearColor.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise addition of two linear colors (R+R, G+G, B+B, A+A)

<a id="unreal.LinearColor.__sub__"></a>

#### __sub__

```python
def __sub__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise subtraction of two linear colors (R-R, G-G, B-B, A-A)

<a id="unreal.LinearColor.__isub__"></a>

#### __isub__

```python
def __isub__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise subtraction of two linear colors (R-R, G-G, B-B, A-A)

<a id="unreal.LinearColor.__mul__"></a>

#### __mul__

```python
def __mul__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise multiplication of two linear colors (R*R, G*G, B*B, A*A)

<a id="unreal.LinearColor.__imul__"></a>

#### __imul__

```python
def __imul__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise multiplication of two linear colors (R*R, G*G, B*B, A*A)

<a id="unreal.LinearColor.__truediv__"></a>

#### __truediv__

```python
def __truediv__(other: LinearColor) -> None
```

**Overloads:**

- ``LinearColor`` Element-wise multiplication of two linear colors (R/R, G/G, B/B, A/A)

<a id="unreal.LinearColor.YELLOW"></a>

#### YELLOW

(LinearColor): Yellow linear color

<a id="unreal.LinearColor.WHITE"></a>

#### WHITE

(LinearColor): White linear color

<a id="unreal.LinearColor.TRANSPARENT"></a>

#### TRANSPARENT

(LinearColor): Transparent linear color - black with 0 opacity/alpha

<a id="unreal.LinearColor.RED"></a>

#### RED

(LinearColor): Red linear color

<a id="unreal.LinearColor.GREEN"></a>

#### GREEN

(LinearColor): Green linear color

<a id="unreal.LinearColor.GRAY"></a>

#### GRAY

(LinearColor): Grey linear color

<a id="unreal.LinearColor.BLUE"></a>

#### BLUE

(LinearColor): Blue linear color

<a id="unreal.LinearColor.BLACK"></a>

#### BLACK

(LinearColor): Black linear color

<a id="unreal.InterpCurvePointQuat"></a>