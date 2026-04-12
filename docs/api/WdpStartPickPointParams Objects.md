## WdpStartPickPointParams Objects

```python
class WdpStartPickPointParams(ParamsBase)
```

Wdp Start Pick Point Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPointAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (Coord_Z_Ref):  [Read-Write]
- ``coordinate_show`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``icon_show`` (bool):  [Read-Write]

<a id="unreal.WdpStartPickPointParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(coordinate_show: bool = False,
             icon_show: bool = False,
             coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.SURFACE) -> None
```

<a id="unreal.WdpStartPickPointParams.coordinate_show"></a>

#### coordinate\_show

```python
@property
def coordinate_show() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpStartPickPointParams.coordinate_show"></a>

#### coordinate\_show

```python
@coordinate_show.setter
def coordinate_show(value: bool) -> None
```

<a id="unreal.WdpStartPickPointParams.icon_show"></a>

#### icon\_show

```python
@property
def icon_show() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpStartPickPointParams.icon_show"></a>

#### icon\_show

```python
@icon_show.setter
def icon_show(value: bool) -> None
```

<a id="unreal.WdpStartPickPointParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> Coord_Z_Ref
```

(Coord_Z_Ref):  [Read-Write]

<a id="unreal.WdpStartPickPointParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: Coord_Z_Ref) -> None
```

<a id="unreal.WdpGetPickedPointsParams"></a>