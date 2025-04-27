## AndroidPermissionFunctionLibrary Objects

```python
class AndroidPermissionFunctionLibrary(BlueprintFunctionLibrary)
```

Android Permission Function Library

**C++ Source:**

- **Plugin**: AndroidPermission
- **Module**: AndroidPermission
- **File**: AndroidPermissionFunctionLibrary.h

<a id="unreal.AndroidPermissionFunctionLibrary.check_permission"></a>

#### check_permission

```python
@classmethod
def check_permission(cls, permission: str) -> bool
```

X.check_permission(permission) -> bool
check if the permission is already granted

Args:
    permission (str): 

Returns:
    bool:

<a id="unreal.AndroidPermissionFunctionLibrary.acquire_permissions"></a>

#### acquire_permissions

```python
@classmethod
def acquire_permissions(
        cls, permissions: Array[str]) -> AndroidPermissionCallbackProxy
```

X.acquire_permissions(permissions) -> AndroidPermissionCallbackProxy
try to acquire permissions and return a singleton callback proxy object containing OnPermissionsGranted delegate

Args:
    permissions (Array[str]): 

Returns:
    AndroidPermissionCallbackProxy:

<a id="unreal.ArchVisCharacter"></a>