## GooglePADErrorCode Objects

```python
class GooglePADErrorCode(EnumBase)
```

An error code associated with Asset Pack operations.

**C++ Source:**

- **Plugin**: GooglePAD
- **Module**: GooglePAD
- **File**: GooglePADFunctionLibrary.h

<a id="unreal.GooglePADErrorCode.ASSET_PACK_NO_ERROR"></a>

#### ASSET\_PACK\_NO\_ERROR

0: There was no error with the request.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_APP_UNAVAILABLE"></a>

#### ASSET\_PACK\_APP\_UNAVAILABLE

1: The requesting app is unavailable.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_UNAVAILABLE"></a>

#### ASSET\_PACK\_UNAVAILABLE

2: The requested Asset Pack isn't available for this app version.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_INVALID_REQUEST"></a>

#### ASSET\_PACK\_INVALID\_REQUEST

3: The request is invalid.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_DOWNLOAD_NOT_FOUND"></a>

#### ASSET\_PACK\_DOWNLOAD\_NOT\_FOUND

4: The requested download isn't found.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_API_NOT_AVAILABLE"></a>

#### ASSET\_PACK\_API\_NOT\_AVAILABLE

5: The Asset Pack API is unavailable.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_NETWORK_ERROR"></a>

#### ASSET\_PACK\_NETWORK\_ERROR

6: Network error. Unable to obtain Asset Pack details.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_ACCESS_DENIED"></a>

#### ASSET\_PACK\_ACCESS\_DENIED

7: Download not permitted under current device circumstances, e.g. app in
background or device not signed into a Google account.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_INSUFFICIENT_STORAGE"></a>

#### ASSET\_PACK\_INSUFFICIENT\_STORAGE

8: Asset Packs download failed due to insufficient storage.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_PLAY_STORE_NOT_FOUND"></a>

#### ASSET\_PACK\_PLAY\_STORE\_NOT\_FOUND

9: The Play Store app is either not installed or not the official version.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_NETWORK_UNRESTRICTED"></a>

#### ASSET\_PACK\_NETWORK\_UNRESTRICTED

10: Returned if showCellularDataConfirmation is called but no Asset Packs are waiting for Wi-Fi.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_INTERNAL_ERROR"></a>

#### ASSET\_PACK\_INTERNAL\_ERROR

11: Unknown error downloading Asset Pack.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_INITIALIZATION_NEEDED"></a>

#### ASSET\_PACK\_INITIALIZATION\_NEEDED

12: The requested operation failed: need to call AssetPackManager_init() first.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_INITIALIZATION_FAILED"></a>

#### ASSET\_PACK\_INITIALIZATION\_FAILED

13: There was an error initializing the Asset Pack API.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_APP_NOT_OWNED"></a>

#### ASSET\_PACK\_APP\_NOT\_OWNED

14: The app isn't owned by any user on this device. An app is "owned" if it has been acquired from the Play Store.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_CONFIRMATION_NOT_REQUIRED"></a>

#### ASSET\_PACK\_CONFIRMATION\_NOT\_REQUIRED

15: Returned if showConfirmationDialog is called but no asset packs are waiting for user confirmation.

<a id="unreal.GooglePADErrorCode.ASSET_PACK_UNRECOGNIZED_INSTALLATION"></a>

#### ASSET\_PACK\_UNRECOGNIZED\_INSTALLATION

16: Returned if the app was not installed by Play.

<a id="unreal.GooglePADDownloadStatus"></a>