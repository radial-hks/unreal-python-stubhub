## ColorGradePerRangeSettings Objects

```python
class ColorGradePerRangeSettings(StructBase)
```

Color Grade Per Range Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``contrast`` (Vector4):  [Read-Write]
- ``gain`` (Vector4):  [Read-Write]
- ``gamma`` (Vector4):  [Read-Write]
- ``offset`` (Vector4):  [Read-Write]
- ``saturation`` (Vector4):  [Read-Write]

<a id="unreal.ColorGradePerRangeSettings.__init__"></a>

#### __init__

```python
def __init__(
        saturation: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        contrast: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        gamma: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        gain: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        offset: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.ColorGradePerRangeSettings.saturation"></a>

#### saturation

```python
@property
def saturation() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.ColorGradePerRangeSettings.saturation"></a>

#### saturation

```python
@saturation.setter
def saturation(value: Vector4) -> None
```

<a id="unreal.ColorGradePerRangeSettings.contrast"></a>

#### contrast

```python
@property
def contrast() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.ColorGradePerRangeSettings.contrast"></a>

#### contrast

```python
@contrast.setter
def contrast(value: Vector4) -> None
```

<a id="unreal.ColorGradePerRangeSettings.gamma"></a>

#### gamma

```python
@property
def gamma() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.ColorGradePerRangeSettings.gamma"></a>

#### gamma

```python
@gamma.setter
def gamma(value: Vector4) -> None
```

<a id="unreal.ColorGradePerRangeSettings.gain"></a>

#### gain

```python
@property
def gain() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.ColorGradePerRangeSettings.gain"></a>

#### gain

```python
@gain.setter
def gain(value: Vector4) -> None
```

<a id="unreal.ColorGradePerRangeSettings.offset"></a>

#### offset

```python
@property
def offset() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.ColorGradePerRangeSettings.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector4) -> None
```

<a id="unreal.ColorGradingSettings"></a>