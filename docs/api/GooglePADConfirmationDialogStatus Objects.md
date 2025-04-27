## GooglePADConfirmationDialogStatus Objects

```python
class GooglePADConfirmationDialogStatus(EnumBase)
```

The status associated with a request to display a confirmation dialog.

**C++ Source:**

- **Plugin**: GooglePAD
- **Module**: GooglePAD
- **File**: GooglePADFunctionLibrary.h

<a id="unreal.GooglePADConfirmationDialogStatus.ASSET_PACK_CONFIRMATION_DIALOG_UNKNOWN"></a>

#### ASSET_PACK_CONFIRMATION_DIALOG_UNKNOWN

0: AssetPackManager_showConfirmationDialog() has not been called.

<a id="unreal.GooglePADConfirmationDialogStatus.ASSET_PACK_CONFIRMATION_DIALOG_PENDING"></a>

#### ASSET_PACK_CONFIRMATION_DIALOG_PENDING

1: AssetPackManager_showConfirmationDialog() has been called, but the user hasn't made a choice.

<a id="unreal.GooglePADConfirmationDialogStatus.ASSET_PACK_CONFIRMATION_DIALOG_APPROVED"></a>

#### ASSET_PACK_CONFIRMATION_DIALOG_APPROVED

2: The user approved of downloading asset packs.

<a id="unreal.GooglePADConfirmationDialogStatus.ASSET_PACK_CONFIRMATION_DIALOG_CANCELED"></a>

#### ASSET_PACK_CONFIRMATION_DIALOG_CANCELED

3: The user declined to download asset packs.

<a id="unreal.FCEase"></a>