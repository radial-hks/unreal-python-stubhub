## GooglePADDownloadStatus Objects

```python
class GooglePADDownloadStatus(EnumBase)
```

The status associated with Asset Pack download operations.

**C++ Source:**

- **Plugin**: GooglePAD
- **Module**: GooglePAD
- **File**: GooglePADFunctionLibrary.h

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_UNKNOWN"></a>

#### ASSET_PACK_UNKNOWN

0: Nothing is known about the Asset Pack.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_PENDING"></a>

#### ASSET_PACK_DOWNLOAD_PENDING

1: An AssetPackManager_requestDownload() async request is pending.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOADING"></a>

#### ASSET_PACK_DOWNLOADING

2: The Asset Pack download is in progress.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_TRANSFERRING"></a>

#### ASSET_PACK_TRANSFERRING

3: The Asset Pack is being transferred to the app.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_COMPLETED"></a>

#### ASSET_PACK_DOWNLOAD_COMPLETED

4: Download and transfer are complete; the assets are available to the app.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_FAILED"></a>

#### ASSET_PACK_DOWNLOAD_FAILED

5: An AssetPackManager_requestDownload() has failed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_CANCELED"></a>

#### ASSET_PACK_DOWNLOAD_CANCELED

6: Asset Pack download has been canceled.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_WAITING_FOR_WIFI"></a>

#### ASSET_PACK_WAITING_FOR_WIFI

7: The Asset Pack download is waiting for Wi-Fi to proceed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_NOT_INSTALLED"></a>

#### ASSET_PACK_NOT_INSTALLED

8: The Asset Pack isn't installed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_INFO_PENDING"></a>

#### ASSET_PACK_INFO_PENDING

9: An AssetPackManager_requestInfo() async request started, but the result isn't known yet.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_INFO_FAILED"></a>

#### ASSET_PACK_INFO_FAILED

10: An AssetPackManager_requestInfo() async request has failed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_REMOVAL_PENDING"></a>

#### ASSET_PACK_REMOVAL_PENDING

11: An AssetPackManager_requestRemoval() async request started.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_REMOVAL_FAILED"></a>

#### ASSET_PACK_REMOVAL_FAILED

12: An AssetPackManager_requestRemoval() async request has failed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_REQUIRES_USER_CONFIRMATION"></a>

#### ASSET_PACK_REQUIRES_USER_CONFIRMATION

13: The Asset Pack download is waiting for user confirmation to proceed.

<a id="unreal.GooglePADStorageMethod"></a>