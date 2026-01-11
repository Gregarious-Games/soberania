"""
Soberanía-Mesh - Decentralized Agricultural Logistics
======================================================

A resilient mesh network for off-grid food sovereignty.

Modules:
    soberania_phiguard: Bidirectional multi-language safety dynamics
    mesh_bridge: Main LoRa/Meshtastic bridge
    orbitdb_sync: P2P persistence layer
    starlink_bridge: Satellite uplink
    kill_switch: Forensic data sanitization
"""

__version__ = "1.0.0"
__author__ = "Gregarious Games"
__license__ = "All Rights Reserved"

from .soberania_phiguard import (
    SoberaniaPhiGuard,
    Direction,
    Language,
    PHI,
    GAMMA,
    CLAMP_HIGH,
    CLAMP_LOW,
)

from .mesh_bridge import (
    SoberaniaMeshBridge,
    COMMODITY_CODES,
    PANIC_CODES,
)

__all__ = [
    # Core classes
    "SoberaniaPhiGuard",
    "SoberaniaMeshBridge",

    # Enums
    "Direction",
    "Language",

    # Constants
    "PHI",
    "GAMMA",
    "CLAMP_HIGH",
    "CLAMP_LOW",
    "COMMODITY_CODES",
    "PANIC_CODES",
]
