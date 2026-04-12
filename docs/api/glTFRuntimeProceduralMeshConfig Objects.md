## glTFRuntimeProceduralMeshConfig Objects

```python
class glTFRuntimeProceduralMeshConfig(StructBase)
```

Gl TFRuntime Procedural Mesh Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box_collisions`` (Array[Box]):  [Read-Write]
- ``build_simple_collision`` (bool):  [Read-Write]
- ``materials_config`` (glTFRuntimeMaterialsConfig):  [Read-Write]
- ``pivot_position`` (EglTFRuntimePivotPosition):  [Read-Write]
- ``reverse_winding`` (bool):  [Read-Write]
- ``sphere_collisions`` (Array[Vector4]):  [Read-Write]
- ``use_complex_as_simple_collision`` (bool):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    reverse_winding: bool = False,
    build_simple_collision: bool = False,
    box_collisions: Array[Box] = [],
    sphere_collisions: Array[Vector4] = [],
    use_complex_as_simple_collision: bool = False,
    pivot_position: EglTFRuntimePivotPosition = EglTFRuntimePivotPosition.
    ASSET,
    materials_config: glTFRuntimeMaterialsConfig = [
        EglTFRuntimeCacheMode.READ_WRITE, {}, {}, {}, {}, {}, False, False,
        False, 0.000000, False, {},
        [
            TextureCompressionSettings.TC_DEFAULT,
            TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False,
            False, 0
        ], "", False, None, {}, False, None, True,
        EglTFRuntimePointsTriangulationMode.
        OPENED_TETRAHEDRON_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, True,
        EglTFRuntimeLinesTriangulationMode.
        OPENED_TRIANGULAR_PRISM_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, {},
        {}, {}
    ]
) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.reverse_winding"></a>

#### reverse\_winding

```python
@property
def reverse_winding() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.reverse_winding"></a>

#### reverse\_winding

```python
@reverse_winding.setter
def reverse_winding(value: bool) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.build_simple_collision"></a>

#### build\_simple\_collision

```python
@property
def build_simple_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.build_simple_collision"></a>

#### build\_simple\_collision

```python
@build_simple_collision.setter
def build_simple_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.box_collisions"></a>

#### box\_collisions

```python
@property
def box_collisions() -> Array[Box]
```

(Array[Box]):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.box_collisions"></a>

#### box\_collisions

```python
@box_collisions.setter
def box_collisions(value: Array[Box]) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.sphere_collisions"></a>

#### sphere\_collisions

```python
@property
def sphere_collisions() -> Array[Vector4]
```

(Array[Vector4]):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.sphere_collisions"></a>

#### sphere\_collisions

```python
@sphere_collisions.setter
def sphere_collisions(value: Array[Vector4]) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.use_complex_as_simple_collision"></a>

#### use\_complex\_as\_simple\_collision

```python
@property
def use_complex_as_simple_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.use_complex_as_simple_collision"></a>

#### use\_complex\_as\_simple\_collision

```python
@use_complex_as_simple_collision.setter
def use_complex_as_simple_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.pivot_position"></a>

#### pivot\_position

```python
@property
def pivot_position() -> EglTFRuntimePivotPosition
```

(EglTFRuntimePivotPosition):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.pivot_position"></a>

#### pivot\_position

```python
@pivot_position.setter
def pivot_position(value: EglTFRuntimePivotPosition) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig.materials_config"></a>

#### materials\_config

```python
@property
def materials_config() -> glTFRuntimeMaterialsConfig
```

(glTFRuntimeMaterialsConfig):  [Read-Write]

<a id="unreal.glTFRuntimeProceduralMeshConfig.materials_config"></a>

#### materials\_config

```python
@materials_config.setter
def materials_config(value: glTFRuntimeMaterialsConfig) -> None
```

<a id="unreal.glTFRuntimeLightConfig"></a>