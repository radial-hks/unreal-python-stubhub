## PolygonGraphicsData Objects

```python
class PolygonGraphicsData(StructBase)
```

Polygon Graphics Data

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PolygonsGraphicsEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (Coord_Z_Ref):  [Read-Write]
- ``guid`` (Guid):  [Read-Write]
- ``polygon`` (WdpPolygon):  [Read-Write]

<a id="unreal.PolygonGraphicsData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(polygon: WdpPolygon = [[[]], []],
             guid: Guid = [],
             coord_z: float = 0.000000,
             coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.SURFACE) -> None
```

<a id="unreal.PolygonGraphicsData.polygon"></a>

#### polygon

```python
@property
def polygon() -> WdpPolygon
```

(WdpPolygon):  [Read-Write]

<a id="unreal.PolygonGraphicsData.polygon"></a>

#### polygon

```python
@polygon.setter
def polygon(value: WdpPolygon) -> None
```

<a id="unreal.PolygonGraphicsData.guid"></a>

#### guid

```python
@property
def guid() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.PolygonGraphicsData.guid"></a>

#### guid

```python
@guid.setter
def guid(value: Guid) -> None
```

<a id="unreal.PolygonGraphicsData.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.PolygonGraphicsData.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.PolygonGraphicsData.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> Coord_Z_Ref
```

(Coord_Z_Ref):  [Read-Write]

<a id="unreal.PolygonGraphicsData.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: Coord_Z_Ref) -> None
```

<a id="unreal.PolylineGraphicsData"></a>