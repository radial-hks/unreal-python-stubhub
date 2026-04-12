## HighlightAreaEntityAtom Objects

```python
class HighlightAreaEntityAtom(EntityAtomBase)
```

Highlight Area Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: HighlightAreaEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_colors`` (Map[int32, str]):  [Read-Write]
- ``exterior_brightness`` (float):  [Read-Write]
- ``exterior_color`` (str):  [Read-Write]
- ``exterior_contrast`` (float):  [Read-Write]
- ``exterior_outline_color`` (str):  [Read-Write]
- ``exterior_saturation`` (float):  [Read-Write]
- ``interior_color`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HighlightAreaEntityAtom")
                 FWdpPolygon2D originalLocation;

<a id="unreal.HighlightAreaEntityAtom.interior_color"></a>

#### interior\_color

```python
@property
def interior_color() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HighlightAreaEntityAtom")
               FWdpPolygon2D originalLocation;

<a id="unreal.HighlightAreaEntityAtom.interior_color"></a>

#### interior\_color

```python
@interior_color.setter
def interior_color(value: str) -> None
```

<a id="unreal.HighlightAreaEntityAtom.exterior_color"></a>

#### exterior\_color

```python
@property
def exterior_color() -> str
```

(str):  [Read-Write]

<a id="unreal.HighlightAreaEntityAtom.exterior_color"></a>

#### exterior\_color

```python
@exterior_color.setter
def exterior_color(value: str) -> None
```

<a id="unreal.HighlightAreaEntityAtom.exterior_outline_color"></a>

#### exterior\_outline\_color

```python
@property
def exterior_outline_color() -> str
```

(str):  [Read-Write]

<a id="unreal.HighlightAreaEntityAtom.exterior_outline_color"></a>

#### exterior\_outline\_color

```python
@exterior_outline_color.setter
def exterior_outline_color(value: str) -> None
```

<a id="unreal.HighlightAreaEntityAtom.exterior_saturation"></a>

#### exterior\_saturation

```python
@property
def exterior_saturation() -> float
```

(float):  [Read-Write]

<a id="unreal.HighlightAreaEntityAtom.exterior_saturation"></a>

#### exterior\_saturation

```python
@exterior_saturation.setter
def exterior_saturation(value: float) -> None
```

<a id="unreal.HighlightAreaEntityAtom.exterior_brightness"></a>

#### exterior\_brightness

```python
@property
def exterior_brightness() -> float
```

(float):  [Read-Write]

<a id="unreal.HighlightAreaEntityAtom.exterior_brightness"></a>

#### exterior\_brightness

```python
@exterior_brightness.setter
def exterior_brightness(value: float) -> None
```

<a id="unreal.HighlightAreaEntityAtom.exterior_contrast"></a>

#### exterior\_contrast

```python
@property
def exterior_contrast() -> float
```

(float):  [Read-Write]

<a id="unreal.HighlightAreaEntityAtom.exterior_contrast"></a>

#### exterior\_contrast

```python
@exterior_contrast.setter
def exterior_contrast(value: float) -> None
```

<a id="unreal.HighlightAreaEntityAtom.custom_colors"></a>

#### custom\_colors

```python
@property
def custom_colors() -> Map[int, str]
```

(Map[int32, str]):  [Read-Write]

<a id="unreal.HighlightAreaEntityAtom.custom_colors"></a>

#### custom\_colors

```python
@custom_colors.setter
def custom_colors(value: Map[int, str]) -> None
```

<a id="unreal.LightEntityAtom"></a>