## GetText3DParams Objects

```python
class GetText3DParams(ResultBase)
```

Get Text 3DParams

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Text3DAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``text3d_style`` (Text3DStyle):  [Read-Write]

<a id="unreal.GetText3DParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             point_entity_eid: str = "",
             text3d_style: Text3DStyle = [
                 "51WORLD", "CF4300FF", "plain", 0.200000, False, 1.000000
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.GetText3DParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GetText3DParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.GetText3DParams.text3d_style"></a>

#### text3d\_style

```python
@property
def text3d_style() -> Text3DStyle
```

(Text3DStyle):  [Read-Write]

<a id="unreal.GetText3DParams.text3d_style"></a>

#### text3d\_style

```python
@text3d_style.setter
def text3d_style(value: Text3DStyle) -> None
```

<a id="unreal.GetText3DParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.GetText3DParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateText3DsParams"></a>