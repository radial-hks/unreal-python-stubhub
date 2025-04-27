## GooglePADStorageMethod Objects

```python
class GooglePADStorageMethod(EnumBase)
```

The method used to store an Asset Pack on the device.

**C++ Source:**

- **Plugin**: GooglePAD
- **Module**: GooglePAD
- **File**: GooglePADFunctionLibrary.h

<a id="unreal.GooglePADStorageMethod.ASSET_PACK_STORAGE_FILES"></a>

#### ASSET_PACK_STORAGE_FILES

0: The Asset Pack is unpacked into a folder containing individual asset files. Assets can be accessed via standard File APIs.

<a id="unreal.GooglePADStorageMethod.ASSET_PACK_STORAGE_APK"></a>

#### ASSET_PACK_STORAGE_APK

1: The Asset Pack is installed as an APK containing packed asset files. Assets can be accessed via AAssetManager.

<a id="unreal.GooglePADStorageMethod.ASSET_PACK_STORAGE_UNKNOWN"></a>

#### ASSET_PACK_STORAGE_UNKNOWN

2: Nothing is known, perhaps due to an error.

<a id="unreal.GooglePADStorageMethod.ASSET_PACK_STORAGE_NOT_INSTALLED"></a>

#### ASSET_PACK_STORAGE_NOT_INSTALLED

3: The Asset Pack is not installed.

<a id="unreal.GooglePADCellularDataConfirmStatus"></a>