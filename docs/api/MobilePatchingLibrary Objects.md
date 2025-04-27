## MobilePatchingLibrary Objects

```python
class MobilePatchingLibrary(BlueprintFunctionLibrary)
```

Mobile Patching Library

**C++ Source:**

- **Plugin**: MobilePatchingUtils
- **Module**: MobilePatchingUtils
- **File**: MobilePatchingLibrary.h

<a id="unreal.MobilePatchingLibrary.request_content"></a>

#### request_content

```python
@classmethod
def request_content(cls, remote_manifest_url: str, cloud_url: str,
                    install_directory: str,
                    on_succeeded: OnRequestContentSucceeded,
                    on_failed: OnRequestContentFailed) -> None
```

X.request_content(remote_manifest_url, cloud_url, install_directory, on_succeeded, on_failed) -> None
Attempt to download manifest file using specified manifest URL.
On success it will return an object that represents remote content. This object can be queried for additional information, like total content size, download size, etc.
User can choose to download and install remote content.

Args:
    remote_manifest_url (str): : URL from where manifest file can be downloaded. (http://my-server.com/awesomecontent.manifest)
    cloud_url (str): :  URL from where content chunk data can be downloaded. (http://my-server.com/awesomecontent/clouddir)
    install_directory (str): 
    on_succeeded (OnRequestContentSucceeded): 
    on_failed (OnRequestContentFailed):

<a id="unreal.MobilePatchingLibrary.has_active_wi_fi_connection"></a>

#### has_active_wi_fi_connection

```python
@classmethod
def has_active_wi_fi_connection(cls) -> bool
```

X.has_active_wi_fi_connection() -> bool
Whether WiFi connection is currently available

Returns:
    bool:

<a id="unreal.MobilePatchingLibrary.get_supported_platform_names"></a>

#### get_supported_platform_names

```python
@classmethod
def get_supported_platform_names(cls) -> Array[str]
```

X.get_supported_platform_names() -> Array[str]
Get the list of supported platform names on this device. Example: Android_ETC2, Android_ASTC

Returns:
    Array[str]:

<a id="unreal.MobilePatchingLibrary.get_installed_content"></a>

#### get_installed_content

```python
@classmethod
def get_installed_content(cls,
                          install_directory: str) -> MobileInstalledContent
```

X.get_installed_content(install_directory) -> MobileInstalledContent
Get the installed content. Will return non-null object if there is an installed content at specified directory
User can choose to mount installed content into the game

Args:
    install_directory (str): 

Returns:
    MobileInstalledContent:

<a id="unreal.MobilePatchingLibrary.get_active_device_profile_name"></a>

#### get_active_device_profile_name

```python
@classmethod
def get_active_device_profile_name(cls) -> str
```

X.get_active_device_profile_name() -> str
Get the name of currently selected device profile name

Returns:
    str:

<a id="unreal.MVVMBlueprintViewExtension"></a>