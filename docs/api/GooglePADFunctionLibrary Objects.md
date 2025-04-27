## GooglePADFunctionLibrary Objects

```python
class GooglePADFunctionLibrary(BlueprintFunctionLibrary)
```

Google PADFunction Library

**C++ Source:**

- **Plugin**: GooglePAD
- **Module**: GooglePAD
- **File**: GooglePADFunctionLibrary.h

<a id="unreal.GooglePADFunctionLibrary.show_confirmation_dialog"></a>

#### show_confirmation_dialog

```python
@classmethod
def show_confirmation_dialog(cls) -> GooglePADErrorCode
```

X.show_confirmation_dialog() -> GooglePADErrorCode
Show confirmation dialog to start all asset pack downloads in either REQUIRES_USER_CONFIRMATION or WAITING_FOR_WIFI state.

Returns:
    GooglePADErrorCode:

<a id="unreal.GooglePADFunctionLibrary.show_cellular_data_confirmation"></a>

#### show_cellular_data_confirmation

```python
@classmethod
def show_cellular_data_confirmation(cls) -> GooglePADErrorCode
```

X.show_cellular_data_confirmation() -> GooglePADErrorCode
Show confirmation dialog requesting data download over cellular network (DEPRECIATED)

Returns:
    GooglePADErrorCode:

<a id="unreal.GooglePADFunctionLibrary.request_removal"></a>

#### request_removal

```python
@classmethod
def request_removal(cls, name: str) -> GooglePADErrorCode
```

X.request_removal(name) -> GooglePADErrorCode
Request removal of an asset pack

Args:
    name (str): 

Returns:
    GooglePADErrorCode:

<a id="unreal.GooglePADFunctionLibrary.request_info"></a>

#### request_info

```python
@classmethod
def request_info(cls, asset_packs: Array[str]) -> GooglePADErrorCode
```

X.request_info(asset_packs) -> GooglePADErrorCode
Request information about a set of asset packs

Args:
    asset_packs (Array[str]): 

Returns:
    GooglePADErrorCode:

<a id="unreal.GooglePADFunctionLibrary.request_download"></a>

#### request_download

```python
@classmethod
def request_download(cls, asset_packs: Array[str]) -> GooglePADErrorCode
```

X.request_download(asset_packs) -> GooglePADErrorCode
Request download of a set of asset packs

Args:
    asset_packs (Array[str]): 

Returns:
    GooglePADErrorCode:

<a id="unreal.GooglePADFunctionLibrary.release_download_state"></a>

#### release_download_state

```python
@classmethod
def release_download_state(cls, state: int) -> None
```

X.release_download_state(state) -> None
Release download state resources

Args:
    state (int32):

<a id="unreal.GooglePADFunctionLibrary.release_asset_pack_location"></a>

#### release_asset_pack_location

```python
@classmethod
def release_asset_pack_location(cls, location: int) -> None
```

X.release_asset_pack_location(location) -> None
Release location resources

Args:
    location (int32):

<a id="unreal.GooglePADFunctionLibrary.get_total_bytes_to_download"></a>

#### get_total_bytes_to_download

```python
@classmethod
def get_total_bytes_to_download(cls, state: int) -> int
```

X.get_total_bytes_to_download(state) -> int32
Get the total number of bytes to download from a download state

Args:
    state (int32): 

Returns:
    int32:

<a id="unreal.GooglePADFunctionLibrary.get_storage_method"></a>

#### get_storage_method

```python
@classmethod
def get_storage_method(cls, location: int) -> GooglePADStorageMethod
```

X.get_storage_method(location) -> GooglePADStorageMethod
Get storage method from location

Args:
    location (int32): 

Returns:
    GooglePADStorageMethod:

<a id="unreal.GooglePADFunctionLibrary.get_show_confirmation_dialog_status"></a>

#### get_show_confirmation_dialog_status

```python
@classmethod
def get_show_confirmation_dialog_status(
        cls) -> Tuple[GooglePADErrorCode, GooglePADConfirmationDialogStatus]
```

X.get_show_confirmation_dialog_status() -> (GooglePADErrorCode, status=GooglePADConfirmationDialogStatus)
Gets the status of confirmation dialog requests

Returns:
    GooglePADConfirmationDialogStatus: 

    status (GooglePADConfirmationDialogStatus):

<a id="unreal.GooglePADFunctionLibrary.get_show_cellular_data_confirmation_status"></a>

#### get_show_cellular_data_confirmation_status

```python
@classmethod
def get_show_cellular_data_confirmation_status(
        cls) -> Tuple[GooglePADErrorCode, GooglePADCellularDataConfirmStatus]
```

X.get_show_cellular_data_confirmation_status() -> (GooglePADErrorCode, status=GooglePADCellularDataConfirmStatus)
Get status of cellular confirmation dialog (DEPRECIATED)

Returns:
    GooglePADCellularDataConfirmStatus: 

    status (GooglePADCellularDataConfirmStatus):

<a id="unreal.GooglePADFunctionLibrary.get_download_status"></a>

#### get_download_status

```python
@classmethod
def get_download_status(cls, state: int) -> GooglePADDownloadStatus
```

X.get_download_status(state) -> GooglePADDownloadStatus
Get download status from a download state

Args:
    state (int32): 

Returns:
    GooglePADDownloadStatus:

<a id="unreal.GooglePADFunctionLibrary.get_download_state"></a>

#### get_download_state

```python
@classmethod
def get_download_state(cls, name: str) -> Tuple[GooglePADErrorCode, int]
```

X.get_download_state(name) -> (GooglePADErrorCode, state=int32)
Get download state handle of an asset pack (release when done)

Args:
    name (str): 

Returns:
    int32: 

    state (int32):

<a id="unreal.GooglePADFunctionLibrary.get_bytes_downloaded"></a>

#### get_bytes_downloaded

```python
@classmethod
def get_bytes_downloaded(cls, state: int) -> int
```

X.get_bytes_downloaded(state) -> int32
Get the number of bytes downloaded from a download state

Args:
    state (int32): 

Returns:
    int32:

<a id="unreal.GooglePADFunctionLibrary.get_assets_path"></a>

#### get_assets_path

```python
@classmethod
def get_assets_path(cls, location: int) -> str
```

X.get_assets_path(location) -> str
Get asset path from from location

Args:
    location (int32): 

Returns:
    str:

<a id="unreal.GooglePADFunctionLibrary.get_asset_pack_location"></a>

#### get_asset_pack_location

```python
@classmethod
def get_asset_pack_location(cls, name: str) -> Tuple[GooglePADErrorCode, int]
```

X.get_asset_pack_location(name) -> (GooglePADErrorCode, location=int32)
Get location handle of requested asset pack (release when done)

Args:
    name (str): 

Returns:
    int32: 

    location (int32):

<a id="unreal.GooglePADFunctionLibrary.cancel_download"></a>

#### cancel_download

```python
@classmethod
def cancel_download(cls, asset_packs: Array[str]) -> GooglePADErrorCode
```

X.cancel_download(asset_packs) -> GooglePADErrorCode
Cancel download of a set of asset packs

Args:
    asset_packs (Array[str]): 

Returns:
    GooglePADErrorCode:

<a id="unreal.OptimusGroomDataProvider"></a>