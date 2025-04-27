## PhysicalMaterialMask Objects

```python
class PhysicalMaterialMask(Object)
```

Physical material masks are used to map multiple physical materials to a single rendering material

**C++ Source:**

- **Module**: Engine
- **File**: PhysicalMaterialMask.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``address_x`` (TextureAddress):  [Read-Write] The addressing mode to use for the X axis.
- ``address_y`` (TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.
- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``mask_texture`` (Texture):  [Read-Only] Mask input texture, square aspect ratio recommended. Recognized mask colors include: white, black, red, green, yellow, cyan, turquoise, and magenta.
- ``uv_channel_index`` (int32):  [Read-Write] StaticMesh UV channel index to use when performing lookups with this mask.

<a id="unreal.PhysicalMaterialMask.mask_texture"></a>

#### mask_texture

```python
@property
def mask_texture() -> Texture
```

(Texture):  [Read-Only] Mask input texture, square aspect ratio recommended. Recognized mask colors include: white, black, red, green, yellow, cyan, turquoise, and magenta.

<a id="unreal.PhysicalMaterialMask.uv_channel_index"></a>

#### uv_channel_index

```python
@property
def uv_channel_index() -> int
```

(int32):  [Read-Write] StaticMesh UV channel index to use when performing lookups with this mask.

<a id="unreal.PhysicalMaterialMask.uv_channel_index"></a>

#### uv_channel_index

```python
@uv_channel_index.setter
def uv_channel_index(value: int) -> None
```

<a id="unreal.PhysicalMaterialMask.address_x"></a>

#### address_x

```python
@property
def address_x() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the X axis.

<a id="unreal.PhysicalMaterialMask.address_x"></a>

#### address_x

```python
@address_x.setter
def address_x(value: TextureAddress) -> None
```

<a id="unreal.PhysicalMaterialMask.address_y"></a>

#### address_y

```python
@property
def address_y() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.

<a id="unreal.PhysicalMaterialMask.address_y"></a>

#### address_y

```python
@address_y.setter
def address_y(value: TextureAddress) -> None
```

<a id="unreal.PhysicsAsset"></a>