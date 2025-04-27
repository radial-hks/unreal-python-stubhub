## AvaBroadcast Objects

```python
class AvaBroadcast(Object)
```

Single Instance Class that manages all the Output Channels

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaBroadcast.h

<a id="unreal.AvaBroadcast.stop_broadcast"></a>

#### stop_broadcast

```python
def stop_broadcast() -> None
```

x.stop_broadcast() -> None
Stop Broadcast

<a id="unreal.AvaBroadcast.start_broadcast"></a>

#### start_broadcast

```python
def start_broadcast() -> None
```

x.start_broadcast() -> None
Start Broadcast

<a id="unreal.AvaBroadcast.is_broadcasting_any_channel"></a>

#### is_broadcasting_any_channel

```python
def is_broadcasting_any_channel() -> bool
```

x.is_broadcasting_any_channel() -> bool
Is Broadcasting Any Channel

Returns:
    bool:

<a id="unreal.AvaBroadcast.is_broadcasting_all_channels"></a>

#### is_broadcasting_all_channels

```python
def is_broadcasting_all_channels() -> bool
```

x.is_broadcasting_all_channels() -> bool
Is Broadcasting All Channels

Returns:
    bool:

<a id="unreal.AvaBroadcast.get_broadcast"></a>

#### get_broadcast

```python
@classmethod
def get_broadcast(cls) -> AvaBroadcast
```

X.get_broadcast() -> AvaBroadcast
Get Broadcast

Returns:
    AvaBroadcast:

<a id="unreal.AvaBroadcast.get_avalanche_broadcast"></a>

#### get_avalanche_broadcast

```python
@classmethod
def get_avalanche_broadcast(cls) -> AvaBroadcast
```

deprecated: 'get_avalanche_broadcast' was renamed to 'get_broadcast'.

<a id="unreal.AvalancheBroadcast"></a>