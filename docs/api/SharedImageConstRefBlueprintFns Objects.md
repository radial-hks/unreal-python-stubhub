## SharedImageConstRefBlueprintFns Objects

```python
class SharedImageConstRefBlueprintFns(Object)
```

Shared Image Const Ref Blueprint Fns

**C++ Source:**

- **Module**: ImageCore
- **File**: ImageCoreBP.h

<a id="unreal.SharedImageConstRefBlueprintFns.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(cls, image: SharedImageConstRefBlueprint) -> bool
```

X.is_valid(image) -> bool
Is Valid

Args:
    image (SharedImageConstRefBlueprint): 

Returns:
    bool:

<a id="unreal.SharedImageConstRefBlueprintFns.get_width"></a>

#### get_width

```python
@classmethod
def get_width(cls, image: SharedImageConstRefBlueprint) -> int
```

X.get_width(image) -> int32
Returns -1 if Image is invalid

Args:
    image (SharedImageConstRefBlueprint): 

Returns:
    int32:

<a id="unreal.SharedImageConstRefBlueprintFns.get_size"></a>

#### get_size

```python
@classmethod
def get_size(cls, image: SharedImageConstRefBlueprint) -> Vector2f
```

X.get_size(image) -> Vector2f
Returns (-1, -1) if Image is invalid

Args:
    image (SharedImageConstRefBlueprint): 

Returns:
    Vector2f:

<a id="unreal.SharedImageConstRefBlueprintFns.get_pixel_value"></a>

#### get_pixel_value

```python
@classmethod
def get_pixel_value(cls, image: SharedImageConstRefBlueprint, x: int,
                    y: int) -> Tuple[Vector4f, bool]
```

X.get_pixel_value(image, x, y) -> (Vector4f, valid=bool)
Returns the value in the texture for the given pixel as a float vector. If the input position is invalid, the format is invalid,
or the reference isn't set, bValid will be false and the function will return FVector4(0,0,0,0).

Pixel values are directly returned with no gamma transformation to allow for lookup tables. Also note that
8 bit formats that you might normally expect to be normalized to 0..1 will return their values directly as 0..256.

This supports all image formats.

G8 is replicated to X/Y/Z/1.
R16/R32 is returned as R/0/0/1.

Do not use this for full image processing as it will be extremely slow, contact support if you need such
functionality.

Args:
    image (SharedImageConstRefBlueprint): 
    x (int32): 
    y (int32): 

Returns:
    bool: 

    valid (bool):

<a id="unreal.SharedImageConstRefBlueprintFns.get_pixel_linear_color"></a>

#### get_pixel_linear_color

```python
@classmethod
def get_pixel_linear_color(
    cls,
    image: SharedImageConstRefBlueprint,
    x: int,
    y: int,
    failure_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000]
) -> Tuple[LinearColor, bool]
```

X.get_pixel_linear_color(image, x, y, failure_color=[0.000000, 0.000000, 0.000000, 1.000000]) -> (LinearColor, valid=bool)
Returns the color value for the given pixel. If the input position is invalid, the format is invalid,
or the reference isn't set, bValid will be false and the function will return FailureColor. The color
is converted using the image's gamma space in to linear space.

Do not use this for full image processing as it will be extremely slow, contact support if you need such
functionality.

Args:
    image (SharedImageConstRefBlueprint): 
    x (int32): 
    y (int32): 
    failure_color (LinearColor): 

Returns:
    bool: 

    valid (bool):

<a id="unreal.SharedImageConstRefBlueprintFns.get_height"></a>

#### get_height

```python
@classmethod
def get_height(cls, image: SharedImageConstRefBlueprint) -> int
```

X.get_height(image) -> int32
Returns -1 if Image is invalid

Args:
    image (SharedImageConstRefBlueprint): 

Returns:
    int32:

<a id="unreal.AssetRegistryHelpers"></a>