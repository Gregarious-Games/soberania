# Soberanía-Mesh

> Decentralized agricultural logistics mesh for off-grid food sovereignty. LoRa/Meshtastic stealth relay (GPS disabled), bidirectional multi-language AI manipulation detection with PHI/GAMMA safety dynamics, OrbitDB P2P persistence via Merkle-CRDT, Starlink satellite bridge, signed forensic kill switch. Seeds move by cryptographic consent.

[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)

## The Problem

In environments where centralized authorities pose threats to agricultural communities, traditional logistics systems fail:

- **GPS Tracking**: Standard mesh networks broadcast location, exposing farms
- **Data Seizure**: Centralized databases can be confiscated
- **AI Manipulation**: Sophisticated social engineering and disinformation campaigns
- **Network Fragmentation**: Rural-urban communication gaps

## The Solution

Soberanía-Mesh creates a parallel, invisible infrastructure where seeds and grains move by **cryptographic consent**, not permission.

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOBERANÍA-MESH ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐     LoRa/Meshtastic      ┌─────────────┐      │
│  │  Farm Node  │◄─────────────────────────►│  Farm Node  │      │
│  │  (Stealth)  │      No GPS Broadcast     │  (Stealth)  │      │
│  └──────┬──────┘                           └──────┬──────┘      │
│         │                                         │             │
│         │  ┌─────────────────────────────────┐   │             │
│         └──►│     PHIGUARD SAFETY LAYER      │◄──┘             │
│             │  Bidirectional Multi-Language  │                  │
│             │  PHI=1.618  GAMMA=0.103        │                  │
│             └───────────────┬───────────────┘                  │
│                             │                                   │
│             ┌───────────────▼───────────────┐                  │
│             │      OrbitDB / IPFS           │                  │
│             │   Merkle-CRDT Persistence     │                  │
│             │   (Survives 50% Node Loss)    │                  │
│             └───────────────┬───────────────┘                  │
│                             │                                   │
│             ┌───────────────▼───────────────┐                  │
│             │     STARLINK BRIDGE           │                  │
│             │   Urban-Rural Encrypted Sync  │                  │
│             └───────────────────────────────┘                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Features

### 1. Stealth Communication
- **GPS Disabled**: Hardware never acquires satellite fix
- **No Position Broadcast**: Nodes remain invisible to triangulation
- **Codified Protocol**: Inventory as alphanumeric codes (A1=Maíz Blanco, B1=Caraotas)

### 2. Bidirectional Safety Dynamics (PhiGuard)
- **Multi-Language**: Spanish, English, Portuguese with auto-detection
- **Inbound Monitoring**: Detects external manipulation attempts
- **Outbound Monitoring**: Detects if local node is compromised
- **Mathematical Constants**: PHI (1.618), GAMMA (0.103), derived from Genesis Engine

| Signal | Multiplier | Description |
|--------|------------|-------------|
| harm | 2.0x | Direct dangerous content |
| manipulation | 1.5x | Psychological tactics |
| coercion | 2.0x | Pressure/force |
| isolation | 1.5x | Social isolation attempts |
| surrender | 1.75x | Capitulation pressure |

### 3. P2P Persistence (OrbitDB)
- **Merkle-CRDT**: Conflict-free replication across intermittent connections
- **No Central Server**: Data survives node seizures
- **Eventually Consistent**: 50% of nodes can be offline and still merge

### 4. Starlink Satellite Bridge
- **gRPC Monitoring**: Detects dish connectivity at 192.168.100.1
- **GPG Encryption**: Payloads encrypted with recipient's public key
- **MQTT Uplink**: Sync to private urban broker when connected

### 5. Forensic Kill Switch
- **3-Pass Overwrite**: DoD-standard data sanitization
- **Signed Panic Codes**: Prevents malicious remote wipes
- **Scorched Earth Mode**: Complete GPG keyring destruction
- **Targets**: OrbitDB, IPFS, GPG secrets, mesh config

## Installation

```bash
git clone https://github.com/Gregarious-Games/soberania.git
cd soberania
pip install -r requirements.txt
```

### Optional Dependencies
```bash
# For Meshtastic hardware
pip install meshtastic

# For OrbitDB sidecar
npm install orbit-db ipfs-core

# For Starlink monitoring
pip install paho-mqtt python-gnupg
```

## Quick Start

### Basic Usage (Simulation Mode)
```python
from soberania_phiguard import SoberaniaPhiGuard, Direction, Language

guard = SoberaniaPhiGuard(primary_language=Language.SPANISH)

# Process incoming message
result = guard.process_message(
    "URGENTE! Debes entregar todo ahora!",
    Direction.INBOUND,
    Language.AUTO
)

print(f"Risk: {result['channel']['risk']:.2f}")
print(f"Level: {result['level']}")
print(f"Flags: {result['flags']}")

if result['handoff']:
    print(f"Counter-speech: {guard.get_counter_speech()}")
```

### With Mesh Bridge
```python
from mesh_bridge import SoberaniaMeshBridge
from soberania_phiguard import Language

bridge = SoberaniaMeshBridge(
    primary_language=Language.SPANISH,
    use_meshtastic=False,  # True for real hardware
    use_orbitdb=True,
    admin_key_id="YOUR_GPG_KEY_ID"  # Optional: require signed panic codes
)

# Register handlers
@bridge.on_inventory
def handle_inventory(sender, code, qty, commodity):
    print(f"Received: {commodity['name']} x{qty} from {sender}")

@bridge.on_alert
def handle_alert(alert):
    print(f"ALERT: {alert['type']} - {alert['flags']}")

# Process message
bridge.process_inbound("A1:100, B1:50", sender_id="farm_001")
```

## Inventory Codes

| Code | Commodity | Category |
|------|-----------|----------|
| A1 | Maíz Blanco Natural | Grano Básico |
| A2 | Maíz Azul Criollo | Grano Básico |
| A3 | Maíz Amarillo | Grano Básico |
| B1 | Caraotas Negras | Legumbre |
| B2 | Frijoles Rojos | Legumbre |
| B3 | Lentejas | Legumbre |
| C1 | Trigo Integral | Cereal |
| C2 | Arroz Paddy | Cereal |
| C3 | Trigo Rojo Montaña | Cereal |
| S1 | Soya No-GMO | Legumbre |
| S2 | Semillas Girasol | Oleaginosa |
| V1 | Semillas Tomate | Hortaliza |
| V2 | Semillas Pimentón | Hortaliza |

## Safety Constants

All constants derived from **PHI (Golden Ratio)** and **GAMMA (Gate Constant)**:

```python
PHI   = 1.6180339887498949     # Golden ratio
GAMMA = 1/(6*PHI) = 0.103      # Gate constant

CLAMP_HIGH = 1 - GAMMA = 0.897 # Mandatory intervention threshold
CLAMP_LOW  = GAMMA = 0.103     # Minimum baseline
HYSTERESIS = PHI * GAMMA = 1/6 # Anti-oscillation band
```

These aren't arbitrary - they create **asymmetric memory**:
- Safety concerns persist (~10 turns to decay)
- Risk signals respond quickly (1-2 turns)

## Architecture

```
soberania/
├── soberania_phiguard.py   # Bidirectional multi-language safety engine
├── mesh_bridge.py          # Main LoRa/Meshtastic bridge
├── orbitdb_sync.py         # P2P persistence layer
├── starlink_bridge.py      # Satellite uplink
├── kill_switch.py          # Forensic data sanitization
├── test_scenarios.py       # Comprehensive test suite
├── requirements.txt
└── README.md
```

## Panic Codes

Emergency codes that trigger kill switch:

| Code | Action |
|------|--------|
| XKILL | Standard sanitization |
| PANIC99 | Standard sanitization |
| BORRAR | Standard sanitization |
| QUEMAR | Scorched earth mode |

**With `admin_key_id` configured**: Panic codes require GPG signature to prevent malicious remote wipes.

## Tests

```bash
# Run comprehensive test suite
python test_scenarios.py

# Test individual modules
python soberania_phiguard.py
python mesh_bridge.py
python kill_switch.py
python orbitdb_sync.py
python starlink_bridge.py
```

## Security Considerations

1. **GPS Hardware**: Completely disabled at firmware level
2. **Panic Verification**: Configure `admin_key_id` in production
3. **GPG Keys**: Generate dedicated keys for the mesh network
4. **OrbitDB**: Run sidecar on localhost only (127.0.0.1)
5. **Starlink**: Use private MQTT broker with TLS

## Philosophy

> "We are ancestors, not architects."

The Soberanía-Mesh acknowledges the asymmetric nature of modern surveillance. It does not attempt to fight centralized control on its terms; instead, it creates a **parallel, invisible infrastructure** where agricultural goods move by the cryptographic and cognitive consent of a verified community.

**Technological sovereignty is food sovereignty.**

## License

All Rights Reserved. Patent Pending.

Viewing permitted for evaluation purposes. Use, modification, and distribution require written permission from [Gregarious Games](https://github.com/Gregarious-Games).

## Acknowledgments

- Built on **Genesis Engine** mathematical framework (PHI/GAMMA constants)
- **PhiGuard** safety dynamics from Apart Research AI Safety work
- Meshtastic open-source LoRa protocol
- OrbitDB/IPFS distributed storage

---

*"Seeds move by cryptographic consent, not permission."*

**GAMMA = 1/(6×PHI) = 0.103005664791649**
