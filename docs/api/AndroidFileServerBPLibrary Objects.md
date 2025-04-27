## AndroidFileServerBPLibrary Objects

```python
class AndroidFileServerBPLibrary(BlueprintFunctionLibrary)
```

Android File Server BPLibrary

**C++ Source:**

- **Plugin**: AndroidFileServer
- **Module**: AndroidFileServer
- **File**: AndroidFileServerBPLibrary.h

<a id="unreal.AndroidFileServerBPLibrary.stop_file_server"></a>

#### stop_file_server

```python
@classmethod
def stop_file_server(cls, usb: bool = True, network: bool = True) -> bool
```

X.stop_file_server(usb=True, network=True) -> bool
Request termination of Android FileServer

Args:
    usb (bool): 
    network (bool): 

Returns:
    bool:

<a id="unreal.AndroidFileServerBPLibrary.start_file_server"></a>

#### start_file_server

```python
@classmethod
def start_file_server(cls,
                      usb: bool = True,
                      network: bool = False,
                      port: int = 57099) -> bool
```

X.start_file_server(usb=True, network=False, port=57099) -> bool
Request startup of Android FileServer

Args:
    usb (bool): 
    network (bool): 
    port (int32): 

Returns:
    bool:

<a id="unreal.AndroidFileServerBPLibrary.is_file_server_running"></a>

#### is_file_server_running

```python
@classmethod
def is_file_server_running(cls) -> AFSActiveType
```

X.is_file_server_running() -> AFSActiveType
Check if Android FileServer is running

Returns:
    AFSActiveType:

<a id="unreal.SuperAPI_JSONToolsBPLibrary"></a>