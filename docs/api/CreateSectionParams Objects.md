## CreateSectionParams Objects

```python
class CreateSectionParams(ParamsBase)
```

Create Section Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: SectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``invert`` (bool):  [Read-Write]
- ``stroke_color`` (str):  [Read-Write]
- ``stroke_weight`` (float):  [Read-Write]
- ``transform`` (SectionTransformParams):  [Read-Write]

<a id="unreal.CreateSectionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    coord_z_ref: str = "",
    stroke_color: str = "",
    stroke_weight: float = 0.000000,
    invert: bool = False,
    transform: SectionTransformParams = [[0.000000, 0.000000, 0.000000],
                                         [0.000000, 0.000000, 0.000000],
                                         [100.000000, 100.000000, 100.000000]]
) -> None
```

<a id="unreal.CreateSectionParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateSectionParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: str) -> None
```

<a id="unreal.CreateSectionParams.stroke_color"></a>

#### stroke\_color

```python
@property
def stroke_color() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateSectionParams.stroke_color"></a>

#### stroke\_color

```python
@stroke_color.setter
def stroke_color(value: str) -> None
```

<a id="unreal.CreateSectionParams.stroke_weight"></a>

#### stroke\_weight

```python
@property
def stroke_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.CreateSectionParams.stroke_weight"></a>

#### stroke\_weight

```python
@stroke_weight.setter
def stroke_weight(value: float) -> None
```

<a id="unreal.CreateSectionParams.invert"></a>

#### invert

```python
@property
def invert() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CreateSectionParams.invert"></a>

#### invert

```python
@invert.setter
def invert(value: bool) -> None
```

<a id="unreal.CreateSectionParams.transform"></a>

#### transform

```python
@property
def transform() -> SectionTransformParams
```

(SectionTransformParams):  [Read-Write]

<a id="unreal.CreateSectionParams.transform"></a>

#### transform

```python
@transform.setter
def transform(value: SectionTransformParams) -> None
```

<a id="unreal.GetSectionParams"></a>