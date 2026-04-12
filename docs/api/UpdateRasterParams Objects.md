## UpdateRasterParams Objects

```python
class UpdateRasterParams(ParamsBase)
```

Update Raster Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RasterAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``raster_style`` (RasterStyle):  [Read-Write]

<a id="unreal.UpdateRasterParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    eid: str = "",
    coord_z_ref: int = 0,
    coord_z: float = 0.000000,
    raster_style: RasterStyle = [
        "http://superapi.51hitech.com/doc-static/images/static/raster/raster.tif",
        "fit", ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"]
    ]
) -> None
```

<a id="unreal.UpdateRasterParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateRasterParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateRasterParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateRasterParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.UpdateRasterParams.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.UpdateRasterParams.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.UpdateRasterParams.raster_style"></a>

#### raster\_style

```python
@property
def raster_style() -> RasterStyle
```

(RasterStyle):  [Read-Write]

<a id="unreal.UpdateRasterParams.raster_style"></a>

#### raster\_style

```python
@raster_style.setter
def raster_style(value: RasterStyle) -> None
```

<a id="unreal.ClipRasterParam"></a>