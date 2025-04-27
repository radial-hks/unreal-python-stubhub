## AvaShapeParametricMaterial Objects

```python
class AvaShapeParametricMaterial(StructBase)
```

Ava Shape Parametric Material

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeParametricMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_a`` (LinearColor):  [Read-Write] Primary colour for the material
- ``color_b`` (LinearColor):  [Read-Write] Secondary colour for the material
- ``gradient_offset`` (float):  [Read-Write] Offset for gradient style material
- ``style`` (AvaShapeParametricMaterialStyle):  [Read-Write] Default style for the material
- ``use_auto_translucency`` (bool):  [Read-Write]
- ``use_two_sided_material`` (bool):  [Read-Write] whether the material is one sided or two sided
- ``use_unlit_material`` (bool):  [Read-Write] whether the material is unlit or default lit

<a id="unreal.AvaShapeParametricMaterial.__init__"></a>

#### __init__

```python
def __init__(
        use_auto_translucency: bool = False,
        style: AvaShapeParametricMaterialStyle = AvaShapeParametricMaterialStyle
    .SOLID,
        color_a: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        color_b: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        gradient_offset: float = 0.000000,
        use_unlit_material: bool = False,
        use_two_sided_material: bool = False) -> None
```

<a id="unreal.AvaShapeParametricMaterial.use_auto_translucency"></a>

#### use_auto_translucency

```python
@property
def use_auto_translucency() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaShapeParametricMaterial.use_auto_translucency"></a>

#### use_auto_translucency

```python
@use_auto_translucency.setter
def use_auto_translucency(value: bool) -> None
```

<a id="unreal.AvaShapeParametricMaterial.style"></a>

#### style

```python
@property
def style() -> AvaShapeParametricMaterialStyle
```

(AvaShapeParametricMaterialStyle):  [Read-Write] Default style for the material

<a id="unreal.AvaShapeParametricMaterial.style"></a>

#### style

```python
@style.setter
def style(value: AvaShapeParametricMaterialStyle) -> None
```

<a id="unreal.AvaShapeParametricMaterial.color_a"></a>

#### color_a

```python
@property
def color_a() -> LinearColor
```

(LinearColor):  [Read-Write] Primary colour for the material

<a id="unreal.AvaShapeParametricMaterial.color_a"></a>

#### color_a

```python
@color_a.setter
def color_a(value: LinearColor) -> None
```

<a id="unreal.AvaShapeParametricMaterial.color_b"></a>

#### color_b

```python
@property
def color_b() -> LinearColor
```

(LinearColor):  [Read-Write] Secondary colour for the material

<a id="unreal.AvaShapeParametricMaterial.color_b"></a>

#### color_b

```python
@color_b.setter
def color_b(value: LinearColor) -> None
```

<a id="unreal.AvaShapeParametricMaterial.gradient_offset"></a>

#### gradient_offset

```python
@property
def gradient_offset() -> float
```

(float):  [Read-Write] Offset for gradient style material

<a id="unreal.AvaShapeParametricMaterial.gradient_offset"></a>

#### gradient_offset

```python
@gradient_offset.setter
def gradient_offset(value: float) -> None
```

<a id="unreal.AvaShapeParametricMaterial.use_unlit_material"></a>

#### use_unlit_material

```python
@property
def use_unlit_material() -> bool
```

(bool):  [Read-Write] whether the material is unlit or default lit

<a id="unreal.AvaShapeParametricMaterial.use_unlit_material"></a>

#### use_unlit_material

```python
@use_unlit_material.setter
def use_unlit_material(value: bool) -> None
```

<a id="unreal.AvaShapeParametricMaterial.use_two_sided_material"></a>

#### use_two_sided_material

```python
@property
def use_two_sided_material() -> bool
```

(bool):  [Read-Write] whether the material is one sided or two sided

<a id="unreal.AvaShapeParametricMaterial.use_two_sided_material"></a>

#### use_two_sided_material

```python
@use_two_sided_material.setter
def use_two_sided_material(value: bool) -> None
```

<a id="unreal.AvaToolboxParametricMaterial"></a>