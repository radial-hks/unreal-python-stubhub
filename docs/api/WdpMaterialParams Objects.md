## WdpMaterialParams Objects

```python
class WdpMaterialParams(StructBase)
```

Wdp Material Params

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpMaterial
- **File**: WdpMaterialDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_channel_control`` (ML_Material_Channel_Control):  [Read-Write]
- ``uv_control`` (ML_UV_Control):  [Read-Write]

<a id="unreal.WdpMaterialParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    uv_control: ML_UV_Control = [
        1.000000, 1.000000, 1.000000, 0.000000, 0.000000, 0.000000
    ],
    material_channel_control: ML_Material_Channel_Control = [
        "", [0, 0, 0, 0], 1.000000, 1.000000, "", 1.000000,
        "", 0.500000, "", 0.000000, "", 1.000000, "", 1.000000, "", "",
        [0, 0, 0, 0], "", 1.000000, 0.100000, [0, 0, 0, 0], 1.000000
    ]
) -> None
```

<a id="unreal.WdpMaterialParams.uv_control"></a>

#### uv\_control

```python
@property
def uv_control() -> ML_UV_Control
```

(ML_UV_Control):  [Read-Write]

<a id="unreal.WdpMaterialParams.uv_control"></a>

#### uv\_control

```python
@uv_control.setter
def uv_control(value: ML_UV_Control) -> None
```

<a id="unreal.WdpMaterialParams.material_channel_control"></a>

#### material\_channel\_control

```python
@property
def material_channel_control() -> ML_Material_Channel_Control
```

(ML_Material_Channel_Control):  [Read-Write]

<a id="unreal.WdpMaterialParams.material_channel_control"></a>

#### material\_channel\_control

```python
@material_channel_control.setter
def material_channel_control(value: ML_Material_Channel_Control) -> None
```

<a id="unreal.WdpMaterialObject"></a>