## GisInfo Objects

```python
class GisInfo(TableRowBase)
```

Gis Info

**C++ Source:**

- **Plugin**: GDALForUnreal
- **Module**: GDALForUnreal
- **File**: GISFunctionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lat`` (str):  [Read-Write]
- ``lng`` (str):  [Read-Write]
- ``location`` (Vector):  [Read-Write]

<a id="unreal.GisInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(lng: str = "",
             lat: str = "",
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GisInfo.lng"></a>

#### lng

```python
@property
def lng() -> str
```

(str):  [Read-Write]

<a id="unreal.GisInfo.lng"></a>

#### lng

```python
@lng.setter
def lng(value: str) -> None
```

<a id="unreal.GisInfo.lat"></a>

#### lat

```python
@property
def lat() -> str
```

(str):  [Read-Write]

<a id="unreal.GisInfo.lat"></a>

#### lat

```python
@lat.setter
def lat(value: str) -> None
```

<a id="unreal.GisInfo.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GisInfo.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WdpCurve2D"></a>