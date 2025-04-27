## MVVMEventField Objects

```python
class MVVMEventField(StructBase)
```

Generic structure to notify when an event occurs.

class UMyViewmodel : public UMVVMViewModelBase
{
  UPROPERTY(FieldNotify)
  FMVVMEventField SomeEvent;

  void OnSomeEvent()
  {
    UE_MVVM_BROADCAST_FIELD_VALUE_CHANGED(SomeEvent);
  }
};
};

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMEventField.h

<a id="unreal.MVVMEventField.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMViewModelContext"></a>