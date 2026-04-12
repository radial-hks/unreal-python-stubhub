## PointGraphicsData Objects

```python
class PointGraphicsData(StructBase)
```

Point Graphics Data

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PointWidget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (Coord_Z_Ref):  [Read-Write]
- ``guid`` (Guid):  [Read-Write]
- ``label`` (str):  [Read-Write]
- ``name`` (str):  [Read-Write]
- ``point`` (Vector):  [Read-Write]
- ``style`` (PointGraphicsStyle):  [Read-Write]

<a id="unreal.PointGraphicsData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point: Vector = [0.000000, 0.000000, 0.000000],
             guid: Guid = [],
             name: str = "",
             label: str = "",
             style: PointGraphicsStyle = [False, False, True, True],
             coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.SURFACE,
             coord_z: float = 0.000000) -> None
```

<a id="unreal.PointGraphicsData.point"></a>

#### point

```python
@property
def point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PointGraphicsData.point"></a>

#### point

```python
@point.setter
def point(value: Vector) -> None
```

<a id="unreal.PointGraphicsData.guid"></a>

#### guid

```python
@property
def guid() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.PointGraphicsData.guid"></a>

#### guid

```python
@guid.setter
def guid(value: Guid) -> None
```

<a id="unreal.PointGraphicsData.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.PointGraphicsData.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.PointGraphicsData.label"></a>

#### label

```python
@property
def label() -> str
```

(str):  [Read-Write]

<a id="unreal.PointGraphicsData.label"></a>

#### label

```python
@label.setter
def label(value: str) -> None
```

<a id="unreal.PointGraphicsData.style"></a>

#### style

```python
@property
def style() -> PointGraphicsStyle
```

(PointGraphicsStyle):  [Read-Write]

<a id="unreal.PointGraphicsData.style"></a>

#### style

```python
@style.setter
def style(value: PointGraphicsStyle) -> None
```

<a id="unreal.PointGraphicsData.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> Coord_Z_Ref
```

(Coord_Z_Ref):  [Read-Write]

<a id="unreal.PointGraphicsData.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: Coord_Z_Ref) -> None
```

<a id="unreal.PointGraphicsData.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.PointGraphicsData.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.PolygonGraphicsData"></a>