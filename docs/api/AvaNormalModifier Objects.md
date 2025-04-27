## AvaNormalModifier Objects

```python
class AvaNormalModifier(AvaGeometryBaseModifier)
```

Ava Normal Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaNormalModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle_threshold`` (float):  [Read-Write] Angle to compare and split normal when threshold method is chosen
- ``angle_weighted`` (bool):  [Read-Write] Recompute normals and weight them by angle
- ``area_weighted`` (bool):  [Read-Write] Recompute normals and weight them by area
- ``invert`` (bool):  [Read-Write] Recompute normals and invert normals and triangles
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``poly_group_layer`` (str):  [Read-Write] PolyGroup to use to split normal from when PolyGroup method is chosen
- ``split_method`` (AvaNormalModifierSplitMethod):  [Read-Write] Recompute normals and use a split method

<a id="unreal.AvaNormalModifier.set_split_method"></a>

#### set_split_method

```python
def set_split_method(split_method: AvaNormalModifierSplitMethod) -> None
```

x.set_split_method(split_method) -> None
Set Split Method

Args:
    split_method (AvaNormalModifierSplitMethod):

<a id="unreal.AvaNormalModifier.set_poly_group_layer_idx"></a>

#### set_poly_group_layer_idx

```python
def set_poly_group_layer_idx(poly_group_layer: int) -> None
```

x.set_poly_group_layer_idx(poly_group_layer) -> None
Set Poly Group Layer Idx

Args:
    poly_group_layer (int32):

<a id="unreal.AvaNormalModifier.set_invert"></a>

#### set_invert

```python
def set_invert(invert: bool) -> None
```

x.set_invert(invert) -> None
Set Invert

Args:
    invert (bool):

<a id="unreal.AvaNormalModifier.set_area_weighted"></a>

#### set_area_weighted

```python
def set_area_weighted(area_weighted: bool) -> None
```

x.set_area_weighted(area_weighted) -> None
Set Area Weighted

Args:
    area_weighted (bool):

<a id="unreal.AvaNormalModifier.set_angle_weighted"></a>

#### set_angle_weighted

```python
def set_angle_weighted(angle_weighted: bool) -> None
```

x.set_angle_weighted(angle_weighted) -> None
Set Angle Weighted

Args:
    angle_weighted (bool):

<a id="unreal.AvaNormalModifier.set_angle_threshold"></a>

#### set_angle_threshold

```python
def set_angle_threshold(angle_threshold: float) -> None
```

x.set_angle_threshold(angle_threshold) -> None
Set Angle Threshold

Args:
    angle_threshold (float):

<a id="unreal.AvaNormalModifier.get_split_method"></a>

#### get_split_method

```python
def get_split_method() -> AvaNormalModifierSplitMethod
```

x.get_split_method() -> AvaNormalModifierSplitMethod
Get Split Method

Returns:
    AvaNormalModifierSplitMethod:

<a id="unreal.AvaNormalModifier.get_poly_group_layer_idx"></a>

#### get_poly_group_layer_idx

```python
def get_poly_group_layer_idx() -> int
```

x.get_poly_group_layer_idx() -> int32
Get Poly Group Layer Idx

Returns:
    int32:

<a id="unreal.AvaNormalModifier.get_invert"></a>

#### get_invert

```python
def get_invert() -> bool
```

x.get_invert() -> bool
Get Invert

Returns:
    bool:

<a id="unreal.AvaNormalModifier.get_area_weighted"></a>

#### get_area_weighted

```python
def get_area_weighted() -> bool
```

x.get_area_weighted() -> bool
Get Area Weighted

Returns:
    bool:

<a id="unreal.AvaNormalModifier.get_angle_weighted"></a>

#### get_angle_weighted

```python
def get_angle_weighted() -> bool
```

x.get_angle_weighted() -> bool
Get Angle Weighted

Returns:
    bool:

<a id="unreal.AvaNormalModifier.get_angle_threshold"></a>

#### get_angle_threshold

```python
def get_angle_threshold() -> float
```

x.get_angle_threshold() -> float
Get Angle Threshold

Returns:
    float:

<a id="unreal.AvaOutlineModifier"></a>