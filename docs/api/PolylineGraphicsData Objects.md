## PolylineGraphicsData Objects

```python
class PolylineGraphicsData(StructBase)
```

Polyline Graphics Data

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PolylinesWidget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (Coord_Z_Ref):  [Read-Write]
- ``guid`` (Guid):  [Read-Write]
- ``is_loop`` (bool):  [Read-Write]
- ``loop`` (WdpLoop):  [Read-Write]
- ``polyline`` (WdpPolyline):  [Read-Write]

<a id="unreal.PolylineGraphicsData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(polyline: WdpPolyline = [[]],
             loop: WdpLoop = [[]],
             is_loop: bool = False,
             guid: Guid = [],
             coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.SURFACE,
             coord_z: float = 0.000000) -> None
```

<a id="unreal.PolylineGraphicsData.polyline"></a>

#### polyline

```python
@property
def polyline() -> WdpPolyline
```

(WdpPolyline):  [Read-Write]

<a id="unreal.PolylineGraphicsData.polyline"></a>

#### polyline

```python
@polyline.setter
def polyline(value: WdpPolyline) -> None
```

<a id="unreal.PolylineGraphicsData.loop"></a>

#### loop

```python
@property
def loop() -> WdpLoop
```

(WdpLoop):  [Read-Write]

<a id="unreal.PolylineGraphicsData.loop"></a>

#### loop

```python
@loop.setter
def loop(value: WdpLoop) -> None
```

<a id="unreal.PolylineGraphicsData.is_loop"></a>

#### is\_loop

```python
@property
def is_loop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PolylineGraphicsData.is_loop"></a>

#### is\_loop

```python
@is_loop.setter
def is_loop(value: bool) -> None
```

<a id="unreal.PolylineGraphicsData.guid"></a>

#### guid

```python
@property
def guid() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.PolylineGraphicsData.guid"></a>

#### guid

```python
@guid.setter
def guid(value: Guid) -> None
```

<a id="unreal.PolylineGraphicsData.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> Coord_Z_Ref
```

(Coord_Z_Ref):  [Read-Write]

<a id="unreal.PolylineGraphicsData.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: Coord_Z_Ref) -> None
```

<a id="unreal.PolylineGraphicsData.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.PolylineGraphicsData.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.ParamsBase"></a>