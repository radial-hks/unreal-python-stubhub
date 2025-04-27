## RegionScaleFactors Objects

```python
class RegionScaleFactors(StructBase)
```

Region Scale Factors

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SphericalPoseReader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``negative_height`` (float):  [Read-Write] Scale the region in the NEGATIVE height direction. Range is 0-1. Default is 1.0.
- ``negative_width`` (float):  [Read-Write] Scale the region in the NEGATIVE width direction. Range is 0-1. Default is 1.0.
- ``positive_height`` (float):  [Read-Write] Scale the region in the POSITIVE height direction. Range is 0-1. Default is 1.0.
- ``positive_width`` (float):  [Read-Write] Scale the region in the POSITIVE width direction. Range is 0-1. Default is 1.0.

<a id="unreal.RegionScaleFactors.__init__"></a>

#### __init__

```python
def __init__(positive_width: float = 0.000000,
             negative_width: float = 0.000000,
             positive_height: float = 0.000000,
             negative_height: float = 0.000000) -> None
```

<a id="unreal.RegionScaleFactors.positive_width"></a>

#### positive_width

```python
@property
def positive_width() -> float
```

(float):  [Read-Write] Scale the region in the POSITIVE width direction. Range is 0-1. Default is 1.0.

<a id="unreal.RegionScaleFactors.positive_width"></a>

#### positive_width

```python
@positive_width.setter
def positive_width(value: float) -> None
```

<a id="unreal.RegionScaleFactors.negative_width"></a>

#### negative_width

```python
@property
def negative_width() -> float
```

(float):  [Read-Write] Scale the region in the NEGATIVE width direction. Range is 0-1. Default is 1.0.

<a id="unreal.RegionScaleFactors.negative_width"></a>

#### negative_width

```python
@negative_width.setter
def negative_width(value: float) -> None
```

<a id="unreal.RegionScaleFactors.positive_height"></a>

#### positive_height

```python
@property
def positive_height() -> float
```

(float):  [Read-Write] Scale the region in the POSITIVE height direction. Range is 0-1. Default is 1.0.

<a id="unreal.RegionScaleFactors.positive_height"></a>

#### positive_height

```python
@positive_height.setter
def positive_height(value: float) -> None
```

<a id="unreal.RegionScaleFactors.negative_height"></a>

#### negative_height

```python
@property
def negative_height() -> float
```

(float):  [Read-Write] Scale the region in the NEGATIVE height direction. Range is 0-1. Default is 1.0.

<a id="unreal.RegionScaleFactors.negative_height"></a>

#### negative_height

```python
@negative_height.setter
def negative_height(value: float) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings"></a>