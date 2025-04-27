## GooglePADCellularDataConfirmStatus Objects

```python
class GooglePADCellularDataConfirmStatus(EnumBase)
```

The status associated with a request to display a cellular data confirmation dialog.

**C++ Source:**

- **Plugin**: GooglePAD
- **Module**: GooglePAD
- **File**: GooglePADFunctionLibrary.h

<a id="unreal.GooglePADCellularDataConfirmStatus.ASSET_PACK_CONFIRM_UNKNOWN"></a>

#### ASSET_PACK_CONFIRM_UNKNOWN

0: AssetPackManager_showCellularDataConfirmation() has not been called.

<a id="unreal.GooglePADCellularDataConfirmStatus.ASSET_PACK_CONFIRM_PENDING"></a>

#### ASSET_PACK_CONFIRM_PENDING

1: AssetPackManager_showCellularDataConfirmation() has been called, but the user hasn't made a choice.

<a id="unreal.GooglePADCellularDataConfirmStatus.ASSET_PACK_CONFIRM_USER_APPROVED"></a>

#### ASSET_PACK_CONFIRM_USER_APPROVED

2: The user approved of downloading Asset Packs over cellular data.

<a id="unreal.GooglePADCellularDataConfirmStatus.ASSET_PACK_CONFIRM_USER_CANCELED"></a>

#### ASSET_PACK_CONFIRM_USER_CANCELED

3: The user declined to download Asset Packs over cellular data.

<a id="unreal.GooglePADConfirmationDialogStatus"></a>