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

#### ASSET\_PACK\_UNKNOWN

0: Nothing is known about the Asset Pack.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_PENDING"></a>

#### ASSET\_PACK\_DOWNLOAD\_PENDING

1: An AssetPackManager_requestDownload() async request is pending.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOADING"></a>

#### ASSET\_PACK\_DOWNLOADING

2: The Asset Pack download is in progress.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_TRANSFERRING"></a>

#### ASSET\_PACK\_TRANSFERRING

3: The Asset Pack is being transferred to the app.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_COMPLETED"></a>

#### ASSET\_PACK\_DOWNLOAD\_COMPLETED

4: Download and transfer are complete; the assets are available to the app.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_FAILED"></a>

#### ASSET\_PACK\_DOWNLOAD\_FAILED

5: An AssetPackManager_requestDownload() has failed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_DOWNLOAD_CANCELED"></a>

#### ASSET\_PACK\_DOWNLOAD\_CANCELED

6: Asset Pack download has been canceled.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_WAITING_FOR_WIFI"></a>

#### ASSET\_PACK\_WAITING\_FOR\_WIFI

7: The Asset Pack download is waiting for Wi-Fi to proceed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_NOT_INSTALLED"></a>

#### ASSET\_PACK\_NOT\_INSTALLED

8: The Asset Pack isn't installed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_INFO_PENDING"></a>

#### ASSET\_PACK\_INFO\_PENDING

9: An AssetPackManager_requestInfo() async request started, but the result isn't known yet.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_INFO_FAILED"></a>

#### ASSET\_PACK\_INFO\_FAILED

10: An AssetPackManager_requestInfo() async request has failed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_REMOVAL_PENDING"></a>

#### ASSET\_PACK\_REMOVAL\_PENDING

11: An AssetPackManager_requestRemoval() async request started.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_REMOVAL_FAILED"></a>

#### ASSET\_PACK\_REMOVAL\_FAILED

12: An AssetPackManager_requestRemoval() async request has failed.

<a id="unreal.GooglePADDownloadStatus.ASSET_PACK_REQUIRES_USER_CONFIRMATION"></a>

#### ASSET\_PACK\_REQUIRES\_USER\_CONFIRMATION

13: The Asset Pack download is waiting for user confirmation to proceed.

<a id="unreal.GooglePADStorageMethod"></a>