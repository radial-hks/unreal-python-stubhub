## MaterialInstanceParams Objects

```python
class MaterialInstanceParams(StructBase)
```

Material Instance Params

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpMaterial
- **File**: WdpMaterialDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_channel_control`` (WdpJsonObjectWrapper):  [Read-Write]
- ``uv_control`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.MaterialInstanceParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(uv_control: WdpJsonObjectWrapper = [],
             material_channel_control: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.MaterialInstanceParams.uv_control"></a>

#### uv\_control

```python
@property
def uv_control() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.MaterialInstanceParams.uv_control"></a>

#### uv\_control

```python
@uv_control.setter
def uv_control(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.MaterialInstanceParams.material_channel_control"></a>

#### material\_channel\_control

```python
@property
def material_channel_control() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.MaterialInstanceParams.material_channel_control"></a>

#### material\_channel\_control

```python
@material_channel_control.setter
def material_channel_control(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.WdpMaterialInstanceObject"></a>