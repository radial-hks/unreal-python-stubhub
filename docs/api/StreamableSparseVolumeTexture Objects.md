## StreamableSparseVolumeTexture Objects

```python
class StreamableSparseVolumeTexture(SparseVolumeTexture)
```

Represents a streamable SparseVolumeTexture asset and serves as base class for UStaticSparseVolumeTexture and UAnimatedSparseVolumeTexture. It has an array of USparseVolumeTextureFrame.

**C++ Source:**

- **Module**: Engine
- **File**: SparseVolumeTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``address_x`` (TextureAddress):  [Read-Write] The addressing mode to use for the X axis.
- ``address_y`` (TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.
- ``address_z`` (TextureAddress):  [Read-Write] The addressing mode to use for the Z axis.
- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``fallback_value_a`` (Vector4f):  [Read-Only]
- ``fallback_value_b`` (Vector4f):  [Read-Only]
- ``format_a`` (PixelFormat):  [Read-Only]
- ``format_b`` (PixelFormat):  [Read-Only]
- ``local_ddc_only`` (bool):  [Read-Write] If enabled, the SparseVolumeTexture is only going to use the local DDC. For certain assets it might be reasonable to also use the remote DDC, but for larger assets this will mean long up- and download times.
- ``num_frames`` (int32):  [Read-Only]
- ``num_mip_levels`` (int32):  [Read-Only]
- ``number_of_prefetch_frames`` (int32):  [Read-Write] When using non-blocking streaming requests, upcoming frames are loaded into memory in advance. This property controls how many frames to prefetch.
- ``prefetch_percentage_bias`` (float):  [Read-Write] When using non-blocking streaming requests, upcoming frames are loaded into memory in advance. This property applies a bias in percent to how much data is prefetched for every frame.
  A value of 20.0 adds 20% to all prefetch percentages. So if PrefetchPercentageStepSize is set to 20.0, frame N+1 is prefetched at 80% + 20% = 100%, frame N+2 at 60% + 20% = 80%, N+3 at 40% + 20% = 60% etc.
- ``prefetch_percentage_step_size`` (float):  [Read-Write] When using non-blocking streaming requests, upcoming frames are loaded into memory in advance. This property controls the size reduction in percent of each additional prefetched frames.
  A value of 20.0 would prefetch frame N+1 at 80%, N+2 at 60%, N+3 at 40% etc.
- ``streaming_pool_size_factor`` (float):  [Read-Write] The SVT streaming pool is sized such that it can hold the largest frame multiplied by this value. There should be some slack to allow for prefetching frames.
- ``volume_resolution`` (IntVector):  [Read-Only]

<a id="unreal.StreamableSparseVolumeTexture.address_x"></a>

#### address_x

```python
@property
def address_x() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the X axis.

<a id="unreal.StreamableSparseVolumeTexture.address_x"></a>

#### address_x

```python
@address_x.setter
def address_x(value: TextureAddress) -> None
```

<a id="unreal.StreamableSparseVolumeTexture.address_y"></a>

#### address_y

```python
@property
def address_y() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.

<a id="unreal.StreamableSparseVolumeTexture.address_y"></a>

#### address_y

```python
@address_y.setter
def address_y(value: TextureAddress) -> None
```

<a id="unreal.StreamableSparseVolumeTexture.address_z"></a>

#### address_z

```python
@property
def address_z() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the Z axis.

<a id="unreal.StreamableSparseVolumeTexture.address_z"></a>

#### address_z

```python
@address_z.setter
def address_z(value: TextureAddress) -> None
```

<a id="unreal.StreamableSparseVolumeTexture.local_ddc_only"></a>

#### local_ddc_only

```python
@property
def local_ddc_only() -> bool
```

(bool):  [Read-Write] If enabled, the SparseVolumeTexture is only going to use the local DDC. For certain assets it might be reasonable to also use the remote DDC, but for larger assets this will mean long up- and download times.

<a id="unreal.StreamableSparseVolumeTexture.local_ddc_only"></a>

#### local_ddc_only

```python
@local_ddc_only.setter
def local_ddc_only(value: bool) -> None
```

<a id="unreal.StreamableSparseVolumeTexture.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.StreamableSparseVolumeTexture.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.StreamableSparseVolumeTexture.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.StaticSparseVolumeTexture"></a>