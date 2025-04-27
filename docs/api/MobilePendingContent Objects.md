## MobilePendingContent Objects

```python
class MobilePendingContent(MobileInstalledContent)
```

Mobile Pending Content

**C++ Source:**

- **Plugin**: MobilePatchingUtils
- **Module**: MobilePatchingUtils
- **File**: MobilePatchingLibrary.h

<a id="unreal.MobilePendingContent.start_install"></a>

#### start_install

```python
def start_install(on_succeeded: OnContentInstallSucceeded,
                  on_failed: OnContentInstallFailed) -> None
```

x.start_install(on_succeeded, on_failed) -> None
Attempt to download and install remote content.
User can choose to mount installed content into the game.

Args:
    on_succeeded (OnContentInstallSucceeded): 
    on_failed (OnContentInstallFailed):

<a id="unreal.MobilePendingContent.get_total_downloaded_size"></a>

#### get_total_downloaded_size

```python
def get_total_downloaded_size() -> float
```

x.get_total_downloaded_size() -> float
Get the total downloaded size in megabytes. Valid during installation

Returns:
    float:

<a id="unreal.MobilePendingContent.get_required_disk_space"></a>

#### get_required_disk_space

```python
def get_required_disk_space() -> float
```

x.get_required_disk_space() -> float
Get the required disk space in megabytes for this content installation

Returns:
    float:

<a id="unreal.MobilePendingContent.get_install_progress"></a>

#### get_install_progress

```python
def get_install_progress() -> float
```

x.get_install_progress() -> float
Get the current installation progress. Between 0 and 1 for known progress, or less than 0 for unknown progress

Returns:
    float:

<a id="unreal.MobilePendingContent.get_download_status_text"></a>

#### get_download_status_text

```python
def get_download_status_text() -> Text
```

x.get_download_status_text() -> Text
Get Download Status Text

Returns:
    Text:

<a id="unreal.MobilePendingContent.get_download_speed"></a>

#### get_download_speed

```python
def get_download_speed() -> float
```

x.get_download_speed() -> float
Get the current download speed in megabytes per second. Valid during installation

Returns:
    float:

<a id="unreal.MobilePendingContent.get_download_size"></a>

#### get_download_size

```python
def get_download_size() -> float
```

x.get_download_size() -> float
Get the total download size for this content installation

Returns:
    float:

<a id="unreal.MobilePatchingLibrary"></a>