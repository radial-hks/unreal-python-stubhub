## ML\_Material\_Channel\_Control Objects

```python
class ML_Material_Channel_Control(StructBase)
```

ML Material Channel Control

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpMaterial
- **File**: WdpMaterialDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (str):  [Read-Write]
- ``ao`` (str):  [Read-Write]
- ``ao_intensity`` (float):  [Read-Write]
- ``diffuse`` (str):  [Read-Write]
- ``diffuse_color`` (Color):  [Read-Write]
- ``diffuse_desaturation`` (float):  [Read-Write]
- ``diffuse_intensity`` (float):  [Read-Write]
- ``indoor_tex`` (str):  [Read-Write]
- ``inner_color`` (Color):  [Read-Write]
- ``metallic`` (str):  [Read-Write]
- ``metallic_intensity`` (float):  [Read-Write]
- ``morning_em`` (float):  [Read-Write]
- ``morning_em_power`` (float):  [Read-Write]
- ``morning_em_tex`` (str):  [Read-Write]
- ``normal`` (str):  [Read-Write]
- ``normal_intensity`` (float):  [Read-Write]
- ``opacity`` (float):  [Read-Write]
- ``roughness`` (str):  [Read-Write]
- ``roughness_intensity`` (float):  [Read-Write]
- ``specular`` (str):  [Read-Write]
- ``specular_intensity`` (float):  [Read-Write]
- ``window_interior_color`` (Color):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.__init__"></a>

#### \_\_init\_\_

```python
def __init__(diffuse: str = "",
             diffuse_color: Color = [0, 0, 0, 0],
             diffuse_intensity: float = 0.000000,
             diffuse_desaturation: float = 0.000000,
             normal: str = "",
             normal_intensity: float = 0.000000,
             specular: str = "",
             specular_intensity: float = 0.000000,
             ao: str = "",
             ao_intensity: float = 0.000000,
             metallic: str = "",
             metallic_intensity: float = 0.000000,
             roughness: str = "",
             roughness_intensity: float = 0.000000,
             indoor_tex: str = "",
             alpha: str = "",
             inner_color: Color = [0, 0, 0, 0],
             morning_em_tex: str = "",
             morning_em_power: float = 0.000000,
             morning_em: float = 0.000000,
             window_interior_color: Color = [0, 0, 0, 0],
             opacity: float = 0.000000) -> None
```

<a id="unreal.ML_Material_Channel_Control.diffuse"></a>

#### diffuse

```python
@property
def diffuse() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.diffuse"></a>

#### diffuse

```python
@diffuse.setter
def diffuse(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.diffuse_color"></a>

#### diffuse\_color

```python
@property
def diffuse_color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.diffuse_color"></a>

#### diffuse\_color

```python
@diffuse_color.setter
def diffuse_color(value: Color) -> None
```

<a id="unreal.ML_Material_Channel_Control.diffuse_intensity"></a>

#### diffuse\_intensity

```python
@property
def diffuse_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.diffuse_intensity"></a>

#### diffuse\_intensity

```python
@diffuse_intensity.setter
def diffuse_intensity(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.diffuse_desaturation"></a>

#### diffuse\_desaturation

```python
@property
def diffuse_desaturation() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.diffuse_desaturation"></a>

#### diffuse\_desaturation

```python
@diffuse_desaturation.setter
def diffuse_desaturation(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.normal"></a>

#### normal

```python
@property
def normal() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.normal"></a>

#### normal

```python
@normal.setter
def normal(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.normal_intensity"></a>

#### normal\_intensity

```python
@property
def normal_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.normal_intensity"></a>

#### normal\_intensity

```python
@normal_intensity.setter
def normal_intensity(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.specular"></a>

#### specular

```python
@property
def specular() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.specular"></a>

#### specular

```python
@specular.setter
def specular(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.specular_intensity"></a>

#### specular\_intensity

```python
@property
def specular_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.specular_intensity"></a>

#### specular\_intensity

```python
@specular_intensity.setter
def specular_intensity(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.ao"></a>

#### ao

```python
@property
def ao() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.ao"></a>

#### ao

```python
@ao.setter
def ao(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.ao_intensity"></a>

#### ao\_intensity

```python
@property
def ao_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.ao_intensity"></a>

#### ao\_intensity

```python
@ao_intensity.setter
def ao_intensity(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.metallic"></a>

#### metallic

```python
@property
def metallic() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.metallic"></a>

#### metallic

```python
@metallic.setter
def metallic(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.metallic_intensity"></a>

#### metallic\_intensity

```python
@property
def metallic_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.metallic_intensity"></a>

#### metallic\_intensity

```python
@metallic_intensity.setter
def metallic_intensity(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.roughness"></a>

#### roughness

```python
@property
def roughness() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.roughness"></a>

#### roughness

```python
@roughness.setter
def roughness(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.roughness_intensity"></a>

#### roughness\_intensity

```python
@property
def roughness_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.roughness_intensity"></a>

#### roughness\_intensity

```python
@roughness_intensity.setter
def roughness_intensity(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.indoor_tex"></a>

#### indoor\_tex

```python
@property
def indoor_tex() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.indoor_tex"></a>

#### indoor\_tex

```python
@indoor_tex.setter
def indoor_tex(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.alpha"></a>

#### alpha

```python
@property
def alpha() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.inner_color"></a>

#### inner\_color

```python
@property
def inner_color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.inner_color"></a>

#### inner\_color

```python
@inner_color.setter
def inner_color(value: Color) -> None
```

<a id="unreal.ML_Material_Channel_Control.morning_em_tex"></a>

#### morning\_em\_tex

```python
@property
def morning_em_tex() -> str
```

(str):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.morning_em_tex"></a>

#### morning\_em\_tex

```python
@morning_em_tex.setter
def morning_em_tex(value: str) -> None
```

<a id="unreal.ML_Material_Channel_Control.morning_em_power"></a>

#### morning\_em\_power

```python
@property
def morning_em_power() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.morning_em_power"></a>

#### morning\_em\_power

```python
@morning_em_power.setter
def morning_em_power(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.morning_em"></a>

#### morning\_em

```python
@property
def morning_em() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.morning_em"></a>

#### morning\_em

```python
@morning_em.setter
def morning_em(value: float) -> None
```

<a id="unreal.ML_Material_Channel_Control.window_interior_color"></a>

#### window\_interior\_color

```python
@property
def window_interior_color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.window_interior_color"></a>

#### window\_interior\_color

```python
@window_interior_color.setter
def window_interior_color(value: Color) -> None
```

<a id="unreal.ML_Material_Channel_Control.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.ML_Material_Channel_Control.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.ML_UV_Control"></a>