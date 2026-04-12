## WdpGetPickedPointsParams Objects

```python
class WdpGetPickedPointsParams(ParamsBase)
```

Wdp Get Picked Points Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPointAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (Coord_Z_Ref):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WdpGetPickedPointsParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.SURFACE) -> None
```

<a id="unreal.WdpGetPickedPointsParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> Coord_Z_Ref
```

(Coord_Z_Ref):  [Read-Write]

<a id="unreal.WdpGetPickedPointsParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: Coord_Z_Ref) -> None
```

<a id="unreal.WdpGetPickedPointsResult"></a>