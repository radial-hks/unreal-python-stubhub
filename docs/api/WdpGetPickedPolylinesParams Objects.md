## WdpGetPickedPolylinesParams Objects

```python
class WdpGetPickedPolylinesParams(ParamsBase)
```

Wdp Get Picked Polylines Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPolylineAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WdpGetPickedPolylinesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(coord_z_ref: int = 0) -> None
```

<a id="unreal.WdpGetPickedPolylinesParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.WdpGetPickedPolylinesParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.WdpGetPickedPolylinesResult"></a>