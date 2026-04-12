## DCPSectionParam Objects

```python
class DCPSectionParam(EidParams)
```

DCPSection Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPSectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (str):  [Read-Write]
- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``invert`` (bool):  [Read-Write]
- ``show_location`` (bool):  [Read-Write]
- ``status`` (bool):  [Read-Write]
- ``stroke_color`` (str):  [Read-Write]
- ``stroke_weight`` (float):  [Read-Write]
- ``transform`` (DCPSectionTransformParams):  [Read-Write]

<a id="unreal.DCPSectionParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    status: bool = False,
    coord_z_ref: str = "",
    stroke_color: str = "",
    stroke_weight: float = 0.000000,
    invert: bool = False,
    show_location: bool = False,
    transform: DCPSectionTransformParams = [[0.000000, 0.000000, 0.000000],
                                            [0.000000, 0.000000, 0.000000],
                                            [50.000000, 50.000000, 50.000000]]
) -> None
```

<a id="unreal.DCPSectionParam.status"></a>

#### status

```python
@property
def status() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPSectionParam.status"></a>

#### status

```python
@status.setter
def status(value: bool) -> None
```

<a id="unreal.DCPSectionParam.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPSectionParam.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: str) -> None
```

<a id="unreal.DCPSectionParam.stroke_color"></a>

#### stroke\_color

```python
@property
def stroke_color() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPSectionParam.stroke_color"></a>

#### stroke\_color

```python
@stroke_color.setter
def stroke_color(value: str) -> None
```

<a id="unreal.DCPSectionParam.stroke_weight"></a>

#### stroke\_weight

```python
@property
def stroke_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPSectionParam.stroke_weight"></a>

#### stroke\_weight

```python
@stroke_weight.setter
def stroke_weight(value: float) -> None
```

<a id="unreal.DCPSectionParam.invert"></a>

#### invert

```python
@property
def invert() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPSectionParam.invert"></a>

#### invert

```python
@invert.setter
def invert(value: bool) -> None
```

<a id="unreal.DCPSectionParam.show_location"></a>

#### show\_location

```python
@property
def show_location() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPSectionParam.show_location"></a>

#### show\_location

```python
@show_location.setter
def show_location(value: bool) -> None
```

<a id="unreal.DCPSectionParam.transform"></a>

#### transform

```python
@property
def transform() -> DCPSectionTransformParams
```

(DCPSectionTransformParams):  [Read-Write]

<a id="unreal.DCPSectionParam.transform"></a>

#### transform

```python
@transform.setter
def transform(value: DCPSectionTransformParams) -> None
```

<a id="unreal.DCPSwitchBaseParam"></a>