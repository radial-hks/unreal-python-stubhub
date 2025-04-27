## DMMaterialValueColorAtlas Objects

```python
class DMMaterialValueColorAtlas(DMMaterialValue)
```

Component representing a color atlas value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueColorAtlas.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atlas`` (CurveLinearColorAtlas):  [Read-Write]
- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``curve`` (CurveLinearColor):  [Read-Write]
- ``default_value`` (float):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (float):  [Read-Write]

<a id="unreal.DMMaterialValueColorAtlas.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.DMMaterialValueColorAtlas.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.DMMaterialValueColorAtlas.default_value"></a>

#### default_value

```python
@property
def default_value() -> float
```

(float):  [Read-Write]

<a id="unreal.DMMaterialValueColorAtlas.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: float) -> None
```

<a id="unreal.DMMaterialValueColorAtlas.atlas"></a>

#### atlas

```python
@property
def atlas() -> CurveLinearColorAtlas
```

(CurveLinearColorAtlas):  [Read-Write]

<a id="unreal.DMMaterialValueColorAtlas.atlas"></a>

#### atlas

```python
@atlas.setter
def atlas(value: CurveLinearColorAtlas) -> None
```

<a id="unreal.DMMaterialValueColorAtlas.curve"></a>

#### curve

```python
@property
def curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueColorAtlas.curve"></a>

#### curve

```python
@curve.setter
def curve(value: CurveLinearColor) -> None
```

<a id="unreal.DMMaterialValueColorAtlas.set_value"></a>

#### set_value

```python
def set_value(value: float) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (float):

<a id="unreal.DMMaterialValueColorAtlas.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: float) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (float):

<a id="unreal.DMMaterialValueColorAtlas.set_curve"></a>

#### set_curve

```python
def set_curve(curve: CurveLinearColor) -> None
```

x.set_curve(curve) -> None
Set Curve

Args:
    curve (CurveLinearColor):

<a id="unreal.DMMaterialValueColorAtlas.set_atlas"></a>

#### set_atlas

```python
def set_atlas(atlas: CurveLinearColorAtlas) -> None
```

x.set_atlas(atlas) -> None
Set Atlas

Args:
    atlas (CurveLinearColorAtlas):

<a id="unreal.DMMaterialValueColorAtlas.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Get Value

Returns:
    float:

<a id="unreal.DMMaterialValueColorAtlas.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> float
```

x.get_default_value() -> float
Get Default Value

Returns:
    float:

<a id="unreal.DMMaterialValueColorAtlas.get_curve"></a>

#### get_curve

```python
def get_curve() -> CurveLinearColor
```

x.get_curve() -> CurveLinearColor
Get Curve

Returns:
    CurveLinearColor:

<a id="unreal.DMMaterialValueColorAtlas.get_atlas"></a>

#### get_atlas

```python
def get_atlas() -> CurveLinearColorAtlas
```

x.get_atlas() -> CurveLinearColorAtlas
Get Atlas

Returns:
    CurveLinearColorAtlas:

<a id="unreal.AvaInteractiveToolsModeDetailsObjectProvider"></a>