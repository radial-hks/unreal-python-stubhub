## DCPClickSinglePointResult Objects

```python
class DCPClickSinglePointResult(EventArgsBase)
```

DCPClick Single Point Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPSwitchAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gis_coord`` (Vector):  [Read-Write]
- ``ue_coord`` (Vector):  [Read-Write]

<a id="unreal.DCPClickSinglePointResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(gis_coord: Vector = [0.000000, 0.000000, 0.000000],
             ue_coord: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPClickSinglePointResult.gis_coord"></a>

#### gis\_coord

```python
@property
def gis_coord() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPClickSinglePointResult.gis_coord"></a>

#### gis\_coord

```python
@gis_coord.setter
def gis_coord(value: Vector) -> None
```

<a id="unreal.DCPClickSinglePointResult.ue_coord"></a>

#### ue\_coord

```python
@property
def ue_coord() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPClickSinglePointResult.ue_coord"></a>

#### ue\_coord

```python
@ue_coord.setter
def ue_coord(value: Vector) -> None
```

<a id="unreal.DCPClickPointResult"></a>